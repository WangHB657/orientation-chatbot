import openai
import requests
import numpy as np
from bs4 import BeautifulSoup
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# ----------------------------
# ✅ 抓取网页内容
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
        text = main_content.get_text(separator="\n", strip=True) if main_content else soup.get_text(separator="\n",
                                                                                                    strip=True)
        return text
    except:
        return ""


# ----------------------------
# ✅ 文本分段
# ----------------------------

def split_text(text, max_length=500):
    paragraphs = [p.strip() for p in text.split("\n") if len(p.strip()) > 50]
    return paragraphs


# ----------------------------
# ✅ 实体标注
# ----------------------------

def mark_entities(text):
    # Email
    text = re.sub(r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', r'[EMAIL] \1 [/EMAIL]', text)
    # Phone
    text = re.sub(r'(\+?\d[\d\s\-]{7,}\d)', r'[PHONE] \1 [/PHONE]', text)
    # Date
    text = re.sub(r'(\d{1,2}\s+\w+\s+\d{4})', r'[DATE] \1 [/DATE]', text)
    return text


# ----------------------------
# ✅ OpenAI Embedding
# ----------------------------

def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding


# ----------------------------
# ✅ 网页批量 embedding + 保存
# ----------------------------

def build_web_embedding(urls):
    results = []
    for url in urls:
        print(f"Fetching: {url}")
        text = fetch_website_text(url)
        paragraphs = split_text(text)
        for para in paragraphs:
            para = mark_entities(para)  # ✅ 实体增强
            embedding = get_embedding(para)
            results.append({
                "url": url,
                "text": para,
                "embedding": embedding
            })
            print(f"Embedded paragraph from {url}")
    with open("web_embedded.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("✅ Web embedding saved to web_embedded.json")
