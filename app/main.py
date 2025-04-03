from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup
from chatbot import Chatbot
from strategies.exact import ExactMatchStrategy
from strategies.keyword import KeywordMatchStrategy
from strategies.fuzzy import FuzzyMatchStrategy
import numpy as np
from fuzzywuzzy import process

app = FastAPI()


# ----------------------------
# ✅ FAQ数据
# ----------------------------

def load_faq():
    with open("faq.json", "r", encoding="utf-8") as f:
        return json.load(f)["faq"]


faq_data = load_faq()

# ----------------------------
# ✅ API KEY
# ----------------------------

openai.api_key = ""

# ----------------------------
# ✅ 网站
# ----------------------------

SCHOOL_WEBSITES = [
    "https://www.jcu.edu.sg/courses-and-study/orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/before-orientation/",
    "https://www.jcu.edu.sg/courses-and-study/orientation/during-orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/after-orientation",
    "https://www.jcu.edu.sg/events",
    "https://www.jcu.edu.sg/current-students/campus-maps-And-information",
]


# ----------------------------
# ✅ 爬虫
# ----------------------------

def fetch_website_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return ""
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "aside"]):
            tag.extract()
        main_content = soup.find("main") or soup.find("article") or soup.find("section")
        text_content = main_content.get_text(separator="\n", strip=True) if main_content else soup.get_text(
            separator="\n", strip=True)
        return text_content
    except requests.RequestException:
        return ""


def fetch_multiple_websites():
    return "\n\n".join(fetch_website_text(url) for url in SCHOOL_WEBSITES)


# ----------------------------
# ✅ FAQ 检索
# ----------------------------

def search_faq(query, top_k=3):
    bot = Chatbot(ExactMatchStrategy())
    matched_faqs = []

    for strategy in [ExactMatchStrategy(), KeywordMatchStrategy(), FuzzyMatchStrategy()]:
        bot.set_strategy(strategy)
        response = bot.get_response(query, faq_data)
        if response:
            for faq in faq_data:
                if response == faq["answer"]:
                    matched_faqs.append(faq)
                    break
        if len(matched_faqs) >= top_k:
            break

    return matched_faqs


# ----------------------------
# ✅ Embedding 检索函数
# ----------------------------


# 读取 embedding 后的 FAQ
with open("faq_embedded.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)["faq"]


def get_query_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response.data[0].embedding)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def search_faq_by_embedding(query, top_k=3):
    query_embedding = get_query_embedding(query)
    scored = []
    for faq in faq_data:
        sim = cosine_similarity(query_embedding, np.array(faq["embedding"]))
        scored.append((sim, faq))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [faq for sim, faq in scored[:top_k] if sim > 0.7]


# ----------------------------
# ✅ Prompt Template
# ----------------------------

prompt_template = '''
You are an Orientation Assistant Bot for James Cook University Singapore.

You will answer student questions using the following FAQ knowledge:

{faq_context}

When answering:
- Be friendly and helpful.
- Integrate relevant FAQ information naturally.
- Do not just copy FAQ, try to answer like a real person.
- Only answer questions related to JCU SG.
- If no information is available, say: "Sorry, I couldn't find precise information. Please check the official website."

Question: {user_question}

Answer:
'''


# ----------------------------
# ✅ FAQ context 构造
# ----------------------------

def build_faq_context(faqs):
    if not faqs:
        return "No related FAQs found."
    return "\n\n".join([f"Q: {faq['question']}\nA: {faq['answer']}" for faq in faqs])


# ----------------------------
# ✅ GPT 生成回答【已改为 openai >=1.0 的新写法】
# ----------------------------

def generate_answer(user_query, faq_matches, web_content):
    faq_context = build_faq_context(faq_matches)
    prompt = prompt_template.format(faq_context=faq_context, user_question=user_query)

    completion = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_query}
        ]
    )

    return completion.choices[0].message.content.strip()


# ----------------------------
# ✅ API Endpoint
# ----------------------------

@app.get("/chatbot/")
def chatbot_response(query: str):
    try:
        # ✅ 改成 embedding 检索
        faq_matches = search_faq_by_embedding(query)

        web_content = fetch_multiple_websites()
        if not web_content:
            web_content = "No valid web content."

        final_answer = generate_answer(query, faq_matches, web_content)
        return {"response": final_answer}

    except openai.AuthenticationError:
        return {"error": "Invalid OpenAI API key."}
    except openai.RateLimitError:
        return {"error": "OpenAI API quota exceeded."}
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}