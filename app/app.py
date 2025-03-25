import streamlit as st
import requests
import uuid

# 设置页面配置
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓", layout="wide")


# 初始化会话状态
def init_session():
    if "chats" not in st.session_state:
        st.session_state.chats = {}  # keep the history
    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = None  # chat ID


init_session()


# Create new chat
def create_new_chat():
    new_chat_id = str(uuid.uuid4())
    st.session_state.chats[new_chat_id] = {"title": "New Chat", "messages": [], "cache": {}}
    st.session_state.current_chat_id = new_chat_id


# display the history
st.sidebar.title("💬 Chat History")
for chat_id, chat in st.session_state.chats.items():
    if st.sidebar.button(chat["title"][:30], key=chat_id):  # 只显示前30个字符
        st.session_state.current_chat_id = chat_id
        st.rerun()

# The creation new chat bottom
if st.sidebar.button("➕ Create New Chat"):
    create_new_chat()
    st.rerun()

if not st.session_state.current_chat_id:
    create_new_chat()

# Catch the chat
chat = st.session_state.chats[st.session_state.current_chat_id]

# display chat title (Not finish)
st.title(f"🎓 {chat['title']}")

# display chat history
for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# user input solve
def handle_user_input(query):
    if not query.strip():
        return

    # display user input in chat board
    chat["messages"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # New
    if query in chat["cache"]:
        bot_reply = chat["cache"][query]
    else:
        bot_reply = fetch_bot_response(query)
        chat["cache"][query] = bot_reply

    # display reply
    chat["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.rerun()  # update communication


def fetch_bot_response(query):
    """ 通过 FastAPI 服务器获取 Chatbot 响应 """
    try:
        response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={query}")
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "⚠️ No valid response received.")
        return f"⚠️ Server Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Request failed: {str(e)}"


# get user input (display)
query = st.chat_input("Type your message...")
if query:
    handle_user_input(query)

