import streamlit as st
import requests
import uuid
import datetime

# -------------------------------
# 页面配置 Page Configuration
# -------------------------------
st.set_page_config(page_title="JCU Orientation Chatbot", page_icon="🎓", layout="wide")


# -------------------------------
# 导入外部CSS Importing external CSS
# -------------------------------
def local_css(file_name):
    with open(file_name, encoding="utf-8") as f:
        css = f"<style>{f.read()}</style>"
        st.markdown(css, unsafe_allow_html=True)


local_css("style.css")


# -------------------------------
# Session 初始化 Session Initialization
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
# 创建新聊天 Create New Chat
# -------------------------------
def create_new_chat():
    new_chat_id = str(uuid.uuid4())
    today = datetime.date.today()
    st.session_state.chats[new_chat_id] = {"title": "New Chat", "messages": [], "cache": {}, "date": str(today)}
    st.session_state.current_chat_id = new_chat_id
    st.session_state.editing_chat_id = None


# -------------------------------
# Chat History
# -------------------------------
with st.sidebar:
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.image("image/Logo.png", width=240)
    st.markdown("</div><br>", unsafe_allow_html=True)
    st.title("💬 Chat History")

to_delete = None

# -------------------------------
# 分组显示 grouping Today / Yesterday / Earlier
# -------------------------------
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

grouped_chats = {"Today": [], "Yesterday": [], "Earlier": []}

for chat_id, chat in st.session_state.chats.items():
    if "date" not in chat:
        chat["date"] = str(today)

    chat_date = datetime.date.fromisoformat(chat["date"])
    if chat_date == today:
        grouped_chats["Today"].append((chat_id, chat))
    elif chat_date == yesterday:
        grouped_chats["Yesterday"].append((chat_id, chat))
    else:
        grouped_chats["Earlier"].append((chat_id, chat))

# -------------------------------
# 渲染聊天分组 Rendering Chat Groups
# -------------------------------
for group, chats in grouped_chats.items():
    if not chats:
        continue
    st.sidebar.markdown(f"**{group}**")
    for chat_id, chat in chats:
        cols = st.sidebar.columns([0.85, 0.15])
        with cols[0]:
            if st.session_state.editing_chat_id == chat_id:
                new_title = st.text_input("Rename", value=chat["title"], label_visibility="collapsed",
                                          key=f"input_{chat_id}")
                if new_title.strip():
                    chat["title"] = new_title.strip()
                if st.button("✅Confirm", key=f"confirm_{chat_id}"):
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
# 删除功能 Delete function
# -------------------------------
if to_delete:
    del st.session_state.chats[to_delete]
    if st.session_state.current_chat_id == to_delete:
        st.session_state.current_chat_id = None
    st.session_state.editing_chat_id = None
    st.rerun()

# -------------------------------
# Create New Chat (只保留按钮)
# -------------------------------
if st.sidebar.button("➕ Create New Chat"):
    create_new_chat()
    st.rerun()

# -------------------------------
# 初始时不再自动创建 chat
# -------------------------------
if not st.session_state.current_chat_id and st.session_state.chats:
    st.session_state.current_chat_id = list(st.session_state.chats.keys())[0]

# -------------------------------
# Chat 内容
# -------------------------------
if st.session_state.current_chat_id:
    chat = st.session_state.chats[st.session_state.current_chat_id]

    st.title(f"🎓 {chat['title']}")

    for msg in chat["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


    def handle_user_input(query):
        if not query.strip():
            return

        chat["messages"].append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        # ✅ 这里改成 robust 版本
        try:
            response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={query}")
            if response.status_code == 200:
                data = response.json()
                if "response" in data:
                    bot_reply = data["response"]
                elif "error" in data:
                    bot_reply = f"⚠ Server Error: {data['error']}"
                else:
                    bot_reply = "⚠ Unknown server response."
            else:
                bot_reply = f"⚠ Server Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            bot_reply = f"⚠ Request failed: {str(e)}"

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
