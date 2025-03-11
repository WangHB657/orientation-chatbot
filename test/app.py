import streamlit as st
import requests
import uuid  # 生成唯一会话 ID

# 设置页面标题和图标
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓", layout="wide")

# 初始化会话状态
if "chats" not in st.session_state:
    st.session_state.chats = {}  # 存储多个聊天历史 {"chat_id": {"title": "...", "messages": [...] }}
if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None  # 当前选中的聊天 ID

# 侧边栏 - 显示聊天历史
st.sidebar.title("💬 Chat History")
for chat_id, chat in st.session_state.chats.items():
    if st.sidebar.button(chat["title"][:30], key=chat_id):  # 只显示前30个字符作为标题
        st.session_state.current_chat_id = chat_id  # 切换到该聊天
        st.experimental_rerun()

# 创建新聊天按钮
if st.sidebar.button("➕ Create New Chat"):
    new_chat_id = str(uuid.uuid4())  # 生成唯一聊天 ID
    st.session_state.chats[new_chat_id] = {"title": "New Chat", "messages": [], "cache": {}}  # 新对话的缓存
    st.session_state.current_chat_id = new_chat_id  # 切换到新对话
    st.experimental_rerun()

# 如果没有选择聊天，就创建一个新的
if not st.session_state.current_chat_id:
    new_chat_id = str(uuid.uuid4())
    st.session_state.chats[new_chat_id] = {"title": "New Chat", "messages": [], "cache": {}}
    st.session_state.current_chat_id = new_chat_id

# 选中的聊天
chat = st.session_state.chats[st.session_state.current_chat_id]

# 显示聊天标题
st.title(f"🎓 {chat['title']}")

# 显示聊天记录
for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 用户输入
query = st.chat_input("Type your message...")

# 处理用户输入
if query:
    # **立即显示用户输入**
    chat["messages"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # **优化：如果问题已被问过，直接返回缓存结果**
    if query in chat["cache"]:
        bot_reply = chat["cache"][query]
    else:
        try:
            # 发送请求到 FastAPI
            response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={query}")
            if response.status_code != 200:
                bot_reply = f"Server Error: {response.status_code}"
            else:
                data = response.json()
                bot_reply = data.get("response", "Error: No response received.")

            # 存入缓存
            chat["cache"][query] = bot_reply
        except requests.exceptions.RequestException as e:
            bot_reply = f"Request failed: {str(e)}"

    # **立即显示 AI 回复**
    chat["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # **延迟刷新**
    st.rerun()  # 确保整个对话流正常更新


