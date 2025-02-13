import streamlit as st
import requests

st.title("🎓 JCU Orientation Chatbot")
st.markdown("Ask me anything about the orientation!")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query:
        try:
            response = requests.get(f"http://127.0.0.1:8000/chatbot/?query={query}")

            # 检查 HTTP 状态码
            if response.status_code != 200:
                st.error(f"Server Error: {response.status_code}")
            else:
                data = response.json()
                if "error" in data:
                    st.error(data["error"])
                else:
                    st.write("**Response:**", data["response"])

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {str(e)}")
    else:
        st.warning("Please enter a question.")
