from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import process  # ✅ 引入模糊匹配库
import re  # ✅ 用于分词
import time

app = FastAPI()

# 载入 FAQ 数据
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)["faq"]

# OpenAI API Key
openai.api_key = ""

# 需要爬取的多个学校网站
SCHOOL_WEBSITES = [
    "https://www.jcu.edu.sg/courses-and-study/orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/before-orientation/",
    "https://www.jcu.edu.sg/courses-and-study/orientation/during-orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/after-orientation",
    "https://www.jcu.edu.sg/events",
    "https://www.jcu.edu.sg/current-students/campus-maps-And-information",
]


def fetch_website_text(url):
    """爬取单个网站的所有文本内容"""
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"❌ 无法访问 {url}，状态码: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")

        # **删除无关的 HTML 标签，避免爬到菜单、页脚**
        for tag in soup(["script", "style", "nav", "footer", "aside"]):
            tag.extract()

        # **尝试获取主要内容**
        main_content = soup.find("main") or soup.find("article") or soup.find("section")
        if main_content:
            text_content = main_content.get_text(separator="\n", strip=True)
        else:
            text_content = soup.get_text(separator="\n", strip=True)

        return f"🔹 来源: {url}\n{text_content}"

    except requests.RequestException as e:
        return f"❌ 访问 {url} 失败: {str(e)}"


def fetch_multiple_websites():
    """爬取多个学校网站的完整文本"""
    all_content = ""

    for url in SCHOOL_WEBSITES:
        all_content += fetch_website_text(url) + "\n\n"

    return all_content if all_content else "❌ 没有获取到任何网站内容。"


def get_faq_response(user_query):
    """优化版 FAQ 关键词匹配 + 模糊匹配"""
    for item in faq_data:
        if user_query.lower() == item["question"].lower():
            return item["answer"]

    user_keywords = set(re.findall(r'\w+', user_query.lower()))
    best_match = None
    best_score = 0

    for item in faq_data:
        faq_keywords = set(re.findall(r'\w+', item["question"].lower()))
        common_keywords = user_keywords & faq_keywords
        union_keywords = user_keywords | faq_keywords  # 求并集
        score = len(common_keywords) / len(union_keywords)  # Jaccard 相似度

        if score > best_score:
            best_score = score
            best_match = item

    if best_match and best_score > 0.4:
        return best_match["answer"]

    # 模糊匹配
    faq_questions = [item["question"] for item in faq_data]
    best_match_fuzzy = process.extractOne(user_query, faq_questions)

    if best_match_fuzzy and best_match_fuzzy[1] > 75:
        for item in faq_data:
            if item["question"] == best_match_fuzzy[0]:
                return item["answer"]

    return None


def extract_relevant_content(user_query, content):
    """使用模糊匹配提取网页内容，同时优先查找列表和表格"""
    paragraphs = content.split("\n")
    best_matches = process.extract(user_query, paragraphs, limit=5)

    # 提取列表内容
    lists = "\n".join([p[0] for p in best_matches if any(symbol in p[0] for symbol in ["•", "✔", "-", "*"])])
    normal_text = "\n".join([p[0] for p in best_matches if p[1] > 60])

    return lists + "\n" + normal_text


@app.get("/chatbot/")
def chatbot_response(query: str):
    """获取用户提问的回答"""
    try:
        # **1️⃣ 先尝试匹配 FAQ**
        response = get_faq_response(query)
        if response:
            return {"response": response}

        # **2️⃣ 获取学校官网的最新内容（每次都重新爬取）**
        all_websites_content = fetch_multiple_websites()
        if "❌" in all_websites_content or len(all_websites_content) < 50:
            return {"error": "网页爬取失败，未能获取有效内容。"}

        # **3️⃣ 只提取与用户问题相关的内容**
        relevant_content = extract_relevant_content(query, all_websites_content)
        if not relevant_content or len(relevant_content) < 30:
            relevant_content = "No directly relevant information is available. However, based on general knowledge of JCU SG, I will provide my best answer."

        # **4️⃣ 发送到 OpenAI ChatGPT**
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

        gpt_response = completion.choices[0].message.content
        return {"response": gpt_response}

    except openai.AuthenticationError:
        return {"error": "Invalid OpenAI API key."}
    except openai.RateLimitError:
        return {"error": "OpenAI API quota exceeded."}
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}
