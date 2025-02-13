import openai

openai.api_key = "API-Key"

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "hi"}]
)

print(response.choices[0].message.content)  # ✅ 使用 .content 而不是 ["content"]

