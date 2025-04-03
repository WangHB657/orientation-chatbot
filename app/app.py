import streamlit as st
import requests
import uuid

# -------------------------------
# 页面配置
# -------------------------------
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓", layout="wide")

# -------------------------------
# 导入外部CSS
# -------------------------------
def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:  # ✅ 重点修复
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)

local_css("style.css")

# -------------------------------
# Session 初始化
# -------------------------------
def init_session():
    if "chats" not in st.session_state:
        st.session_state.chats = {}
    if "current_chat_id" not in st.session_state:
        st.session_state.current_chat_id = None
    if "editing_chat_id" not in st.session_state:
        st.session_state.editing_chat_id = None

init_session()

# -------------------------------
# 创建新聊天
# -------------------------------
def create_new_chat():
    new_chat_id = str(uuid.uuid4())
    st.session_state.chats[new_chat_id] = {"title": "New Chat", "messages": [], "cache": {}}
    st.session_state.current_chat_id = new_chat_id
    st.session_state.editing_chat_id = None

# -------------------------------
# Chat History
# -------------------------------
st.sidebar.title("💬 Chat History")

to_delete = None

for chat_id, chat in st.session_state.chats.items():
    cols = st.sidebar.columns([0.85, 0.15])
    with cols[0]:
        if st.session_state.editing_chat_id == chat_id:
            new_title = st.text_input("Rename", value=chat["title"], label_visibility="collapsed", key=f"input_{chat_id}")
            if new_title.strip():
                chat["title"] = new_title.strip()
            if st.button("✅", key=f"confirm_{chat_id}"):
                st.session_state.editing_chat_id = None
                st.rerun()
        else:
            if st.button(chat["title"][:27] + ("..." if len(chat["title"]) > 30 else ""), key=f"select_{chat_id}"):
                st.session_state.current_chat_id = chat_id
                st.session_state.editing_chat_id = None
                st.rerun()

    with cols[1]:
        with st.popover("⋯"):
            st.markdown("### Settings")
            if st.button("✏️ Rename", key=f"rename_{chat_id}"):
                st.session_state.editing_chat_id = chat_id
                st.rerun()
            if st.button("🗑️ Delete", key=f"delete_{chat_id}"):
                to_delete = chat_id

# -------------------------------
# 删除功能
# -------------------------------
if to_delete:
    del st.session_state.chats[to_delete]
    if st.session_state.current_chat_id == to_delete:
        st.session_state.current_chat_id = None
    st.session_state.editing_chat_id = None
    st.rerun()

# -------------------------------
# Create New Chat
# -------------------------------
if st.sidebar.button("➕ Create New Chat"):
    create_new_chat()
    st.rerun()

if not st.session_state.chats:
    create_new_chat()
if not st.session_state.current_chat_id:
    st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]

chat = st.session_state.chats[st.session_state.current_chat_id]

# -------------------------------
# Chat 内容区域
# -------------------------------
st.title(f"🎓 {chat['title']}")

for msg in chat["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# 用户输入处理
# -------------------------------
def handle_user_input(query):
    if not query.strip():
        return

    if chat["title"] == "New Chat":
        chat["title"] = query

    chat["messages"].append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    if query in chat["cache"]:
        bot_reply = chat["cache"][query]
    else:
        bot_reply = fetch_bot_response(query)
        chat["cache"][query] = bot_reply

    chat["messages"].append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.rerun()

def fetch_bot_response(query):
    try:
        response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={query}")
        if response.status_code == 200:
            data = response.json()
            return data.get("response", "⚠️ No valid response received.")
        return f"⚠️ Server Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"⚠️ Request failed: {str(e)}"

query = st.chat_input("Type your message...")
if query:
    handle_user_input(query)
