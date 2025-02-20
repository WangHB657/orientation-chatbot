from fastapi import FastAPI
import json
import openai
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# 载入 FAQ 数据
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)["faq"]

# OpenAI API Key
openai.api_key = "API"

# 需要爬取的多个学校网站
SCHOOL_WEBSITES = [
    "https://www.jcu.edu.sg/courses-and-study/orientation",
    "https://www.jcu.edu.sg/courses-and-study/orientation/before-orientation/",  # JCU Before-orientation
    "https://www.jcu.edu.sg/courses-and-study/orientation/during-orientation",  # JCU During-orientation
    "https://www.jcu.edu.sg/courses-and-study/orientation/after-orientation",  # JCU After-orientation
    "https://www.jcu.edu.sg/events",
    "https://www.jcu.edu.sg/current-students/campus-maps-And-information",
]


# 爬取多个学校的网站
def fetch_multiple_websites():
    all_content = ""

    for url in SCHOOL_WEBSITES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"❌ 无法访问 {url}，状态码: {response.status_code}")
                continue  # 跳过这个网站

            # 解析 HTML
            soup = BeautifulSoup(response.text, "html.parser")

            # 获取主要内容（调整结构适应不同网站）
            main_content = soup.find("main")  # 网站主要内容
            if not main_content:
                main_content = soup.get_text()

            # 累加到总内容
            all_content += f"\n\n🔹 来源: {url}\n{main_content.get_text(strip=True)}"

        except requests.RequestException as e:
            print(f"❌ 访问 {url} 失败: {str(e)}")

    return all_content if all_content else "❌ 没有获取到任何网站内容。"


# 先查 FAQ
def get_faq_response(user_query):
    """根据 FAQ 数据匹配最佳答案"""
    for item in faq_data:
        if user_query.lower() in item["question"].lower():
            return item["answer"]
    return None


@app.get("/chatbot/")
def chatbot_response(query: str):
    """获取用户提问的回答"""
    try:
        # 1️⃣ 先尝试匹配 FAQ
        response = get_faq_response(query)
        if response:
            return {"response": response}

        # 2️⃣ 获取多个学校官网的内容
        all_websites_content = fetch_multiple_websites()
        if "❌" in all_websites_content:
            return {"error": all_websites_content}

        # 3️⃣ 调用 ChatGPT API，并提供多个学校网站的内容
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system",
                 "content": f"Use the following multiple university websites to answer questions: {all_websites_content}"},
                {"role": "user", "content": query}
            ]
        )

        gpt_response = completion.choices[0].message.content
        print(f"GPT Response: {gpt_response}")  # ✅ 打印 API 响应
        return {"response": gpt_response}

    except openai.AuthenticationError as e:
        print(f"OpenAI API Key 错误: {e}")
        return {"error": "Invalid OpenAI API key."}

    except openai.RateLimitError as e:
        print(f"OpenAI API 额度用完: {e}")
        return {"error": "OpenAI API quota exceeded."}

    except Exception as e:
        print(f"后端出错: {e}")
        return {"error": f"Server Error: {str(e)}"}

