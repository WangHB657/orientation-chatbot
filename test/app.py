import streamlit as st
import requests

# 设置页面标题和图标
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓")

st.title("🎓 JCU Orientation Chatbot")
st.markdown("Ask me anything about the orientation!")

# 初始化 session_state 来存储聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天记录
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 用户输入
query = st.chat_input("Type your message...")

# 解决输入延迟问题
if query:
    # 先把用户的输入存入 session_state 并刷新 UI
    st.session_state.messages.append({"role": "user", "content": query})
    st.rerun()  # **强制重新运行，防止输入后延迟**

# 检查是否有新的消息（如果有，调用 API）
if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
    user_message = st.session_state.messages[-1]["content"]

    try:
        # 发送请求到 FastAPI
        response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={user_message}")

        # 处理服务器返回的错误
        if response.status_code != 200:
            bot_reply = f"Server Error: {response.status_code}"
        else:
            data = response.json()
            bot_reply = data.get("response", "Error: No response received.")

        # 将机器人回复存入 session_state
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.rerun()  # **强制刷新页面，确保立即显示回复**

    except requests.exceptions.RequestException as e:
        st.session_state.messages.append({"role": "assistant", "content": f"Request failed: {str(e)}"})
        st.rerun()
