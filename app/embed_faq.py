import json
import openai
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding


# 加载 FAQ
with open("faq.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)["faq"]

# 生成 embedding
for faq in faqs:
    text = faq["question"] + " " + " ".join(faq.get("tags", []))
    faq["embedding"] = get_embedding(text)
    print(f"Embedded: {faq['question']}")

# 保存
with open("faq_embedded.json", "w", encoding="utf-8") as f:
    json.dump({"faq": faqs}, f, indent=2)
