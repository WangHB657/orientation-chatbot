import streamlit as st
import requests
import uuid

# -------------------------------
# 页面配置
# -------------------------------
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓", layout="wide")

# -------------------------------
# 初始化
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
# 去除 button 样式
# -------------------------------
st.markdown("""
<style>
div.stButton > button {
    background: transparent;
    border: none;
    text-align: left;
    padding: 5px 0;
}
div.stButton > button:hover {
    background: #f5f5f5;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Chat History
# -------------------------------
st.sidebar.title("💬 Chat History")

to_delete = None

for chat_id, chat in st.session_state.chats.items():
    cols = st.sidebar.columns([0.85, 0.15])
    with cols[0]:
        if st.session_state.editing_chat_id == chat_id:
            # 重命名输入框
            new_title = st.text_input("Rename", value=chat["title"], label_visibility="collapsed", key=f"input_{chat_id}")
            if new_title.strip():
                chat["title"] = new_title.strip()
            if st.button("✅", key=f"confirm_{chat_id}"):
                st.session_state.editing_chat_id = None
                st.rerun()
        else:
            # ✅ 这里修复为可点击的 button，去边框但能点击切换
            if st.button(chat["title"][:27] + ("..." if len(chat["title"]) > 30 else ""), key=f"select_{chat_id}"):
                st.session_state.current_chat_id = chat_id
                st.session_state.editing_chat_id = None
                st.rerun()

    with cols[1]:
        # ... 菜单
        with st.popover("⋯"):
            st.markdown("### Settings")
            # ✅ 重命名带图标
            if st.button("✏️ Rename", key=f"rename_{chat_id}"):
                st.session_state.editing_chat_id = chat_id
                st.rerun()
            # ✅ 删除带图标
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
