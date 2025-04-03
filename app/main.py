from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup
import numpy as np

app = FastAPI()

# ----------------------------
# ✅ API KEY
# ----------------------------
openai.api_key = ""

# ----------------------------
# ✅ 读取 FAQ embedding 数据
# ----------------------------

with open("faq_embedded.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)["faq"]

# ----------------------------
# ✅ 读取 Web embedding 数据
# ----------------------------

with open("web_embedded.json", "r", encoding="utf-8") as f:
    web_data = json.load(f)


# ----------------------------
# ✅ Embedding 检索通用函数
# ----------------------------

def get_query_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response.data[0].embedding)


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


# ----------------------------
# ✅ FAQ embedding 检索
# ----------------------------

def search_faq_by_embedding(query, top_k=3):
    query_embedding = get_query_embedding(query)
    scored = []
    for faq in faq_data:
        sim = cosine_similarity(query_embedding, np.array(faq["embedding"]))
        scored.append((sim, faq))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [faq for sim, faq in scored[:top_k] if sim > 0.7]


# ----------------------------
# ✅ Web embedding 检索
# ----------------------------

def search_web_by_embedding(query, top_k=3):
    query_embedding = get_query_embedding(query)
    scored = []
    for item in web_data:
        sim = cosine_similarity(query_embedding, np.array(item["embedding"]))
        scored.append((sim, item))
    scored.sort(reverse=True, key=lambda x: x[0])
    return [item for sim, item in scored[:top_k] if sim > 0.7]


# ----------------------------
# ✅ Prompt Template
# ----------------------------

prompt_template = '''
You are an Orientation Assistant Bot for James Cook University Singapore.

You will answer student questions using the following FAQ and website information:

--- FAQ ---
{faq_context}

--- Website ---
{web_context}

When answering:
- If any email addresses (in format [EMAIL] xxx [/EMAIL]) are present in the context, you MUST include the most relevant email address in your answer.
- Only include emails if they are related to the user's question.
- Carefully read all provided FAQ and website information.
- If no information is available, say: "Sorry, I couldn't find precise information. Please check the official website."
- Only answer questions related to JCU SG.

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
# ✅ Web context 构造
# ----------------------------

def build_web_context(webs):
    if not webs:
        return "No related Website Information."
    return "\n\n".join([f"Source: {item['url']}\n{item['text']}" for item in webs])


# ----------------------------
# ✅ GPT 生成回答
# ----------------------------

def generate_answer(user_query, faq_matches, web_matches):
    faq_context = build_faq_context(faq_matches)
    web_context = build_web_context(web_matches)
    prompt = prompt_template.format(faq_context=faq_context, web_context=web_context, user_question=user_query)

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
        faq_matches = search_faq_by_embedding(query)
        web_matches = search_web_by_embedding(query)
        final_answer = generate_answer(query, faq_matches, web_matches)
        return {"response": final_answer}

    except openai.AuthenticationError:
        return {"error": "Invalid OpenAI API key."}
    except openai.RateLimitError:
        return {"error": "OpenAI API quota exceeded."}
    except Exception as e:
        return {"error": f"Server Error: {str(e)}"}
