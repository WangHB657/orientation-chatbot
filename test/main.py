from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process
import re
import time

app = FastAPI()


# 载入 FAQ 数据
def load_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)["faq"]


faq_data = load_faq()

# OpenAI API Key
openai.api_key = ""

# 学校网站列表
SCHOOL_WEBSITES = [
    "https://www.jcu.edu.sg/courses-and-study/orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/before-orientation/",
    "https://www.jcu.edu.sg/courses-and-study/orientation/during-orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/after-orientation",
    "https://www.jcu.edu.sg/events",
    "https://www.jcu.edu.sg/current-students/campus-maps-And-information",
]


def fetch_website_text(url):
    """爬取单个网站的文本内容"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"❌ 无法访问 {url}，状态码: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "aside"]):
            tag.extract()

        main_content = soup.find("main") or soup.find("article") or soup.find("section")
        text_content = main_content.get_text(separator="\n", strip=True) if main_content else soup.get_text(
            separator="\n", strip=True)
        return f"🔹 来源: {url}\n{text_content}"
    except requests.RequestException as e:
        return f"❌ 访问 {url} 失败: {str(e)}"


def fetch_multiple_websites():
    """爬取多个学校网站的完整文本"""
    return "\n\n".join(fetch_website_text(url) for url in SCHOOL_WEBSITES)


def get_faq_response(user_query):
    """基于 FAQ 进行关键字匹配和模糊匹配"""
    user_query_lower = user_query.lower()
    for item in faq_data:
        if user_query_lower == item["question"].lower():
            return item["answer"]

    user_keywords = set(re.findall(r'\w+', user_query_lower))
    best_match = max(faq_data,
                     key=lambda item: len(user_keywords & set(re.findall(r'\w+', item["question"].lower()))) / len(
                         user_keywords | set(re.findall(r'\w+', item["question"].lower()))), default=None)

    if best_match and len(user_keywords & set(re.findall(r'\w+', best_match["question"].lower()))) / len(
            user_keywords | set(re.findall(r'\w+', best_match["question"].lower()))) > 0.4:
        return best_match["answer"]

    best_match_fuzzy = process.extractOne(user_query, [item["question"] for item in faq_data])
    if best_match_fuzzy and best_match_fuzzy[1] > 75:
        return next(item["answer"] for item in faq_data if item["question"] == best_match_fuzzy[0])

    return None


def extract_relevant_content(user_query, content):
    """提取与用户问题相关的网页内容"""
    paragraphs = content.split("\n")
    best_matches = process.extract(user_query, paragraphs, limit=5)
    lists = "\n".join(p[0] for p in best_matches if any(symbol in p[0] for symbol in ["•", "✔", "-", "*"]))
    normal_text = "\n".join(p[0] for p in best_matches if p[1] > 60)
    return lists + "\n" + normal_text


@app.get("/chatbot/")
def chatbot_response(query: str):
    """获取用户提问的回答"""
    try:
        response = get_faq_response(query)
        if response:
            return {"response": response}

        all_websites_content = fetch_multiple_websites()
        if "❌" in all_websites_content or len(all_websites_content) < 50:
            return {"error": "网页爬取失败，未能获取有效内容。"}

        relevant_content = extract_relevant_content(query, all_websites_content)
        if not relevant_content or len(relevant_content) < 30:
            relevant_content = "No directly relevant information is available. However, based on general knowledge of JCU SG, I will provide my best answer."

        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Use the following multiple university websites to answer questions: {all_websites_content}\n\n"
                        "You are the AI assistant for James Cook University Singapore (JCU SG). "
                        "Your job is to provide accurate and helpful answers about JCU SG, including its courses, orientation programs, campus life, events, and other student-related topics. "
                        "Use the available university information to answer questions, but do not mention that you are extracting or analyzing data. "
                        "If the exact answer is not found, make a reasonable assumption based on JCU SG's academic and student policies."
                    ),
                },
                {"role": "user", "content": query}
            ]
        )

        return {"response": completion.choices[0].message.content}
    except openai.AuthenticationError:
        return {"error": "Invalid OpenAI API key."}
    except openai.RateLimitError:
        return {"error": "OpenAI API quota exceeded."}
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}

