from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup
import re
from chatbot import Chatbot
from strategies.exact import ExactMatchStrategy
from strategies.keyword import KeywordMatchStrategy
from strategies.fuzzy import FuzzyMatchStrategy
from fuzzywuzzy import process

app = FastAPI()


# 加载 FAQ 数据
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
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"❌ Cannot access {url}, status code: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "aside"]):
            tag.extract()
        main_content = soup.find("main") or soup.find("article") or soup.find("section")
        text_content = main_content.get_text(separator="\n", strip=True) if main_content else soup.get_text(
            separator="\n", strip=True)
        return f"🔹 Source: {url}\n{text_content}"
    except requests.RequestException as e:
        return f"❌ Failed to fetch {url}: {str(e)}"


def fetch_multiple_websites():
    return "\n\n".join(fetch_website_text(url) for url in SCHOOL_WEBSITES)


def get_faq_response(query: str) -> str:
    bot = Chatbot(ExactMatchStrategy())
    response = bot.get_response(query, faq_data)
    if response:
        return response

    bot.set_strategy(KeywordMatchStrategy())
    response = bot.get_response(query, faq_data)
    if response:
        return response

    bot.set_strategy(FuzzyMatchStrategy())
    response = bot.get_response(query, faq_data)
    if response:
        return response

    return None


def extract_relevant_content(user_query, content):
    paragraphs = content.split("\n")
    best_matches = process.extract(user_query, paragraphs, limit=5)
    lists = "\n".join(p[0] for p in best_matches if any(symbol in p[0] for symbol in ["•", "✔", "-", "*"]))
    normal_text = "\n".join(p[0] for p in best_matches if p[1] > 60)
    return lists + "\n" + normal_text


@app.get("/chatbot/")
def chatbot_response(query: str):
    try:
        response = get_faq_response(query)
        if response:
            return {"response": response}

        all_websites_content = fetch_multiple_websites()
        if "❌" in all_websites_content or len(all_websites_content) < 50:
            return {"error": "Failed to crawl websites or insufficient content."}

        relevant_content = extract_relevant_content(query, all_websites_content)
        if not relevant_content or len(relevant_content) < 30:
            relevant_content = "No directly relevant information is available."

        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"Use the following multiple university websites to answer questions: {all_websites_content}\n\n"
                        "IMPORTANT: You must strictly follow these rules while answering:\n"
                        "You are an AI assistant for James Cook University Singapore (JCU SG).\n"
                        "You can only answer questions related to JCU SG, such as courses, orientation programs, campus life, and events.\n"
                        "If you don't have an exact answer, respond with: 'Sorry, I couldn't find precise information. Please check the official website for confirmation.'\n"
                        "If the question is unrelated to JCU SG, respond: 'I can only answer questions related to JCU SG.'"
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
