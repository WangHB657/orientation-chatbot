from fastapi import FastAPI
import json
import openai

app = FastAPI()

# 载入 FAQ 数据
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)["faq"]

# OpenAI API Key
openai.api_key = "API Key"


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
        # 先尝试匹配 FAQ
        response = get_faq_response(query)
        if response:
            return {"response": response}

        # 调用 ChatGPT API（使用新版 OpenAI 语法）
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
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
