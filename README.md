# Orientation Chatbot for JCU Singapore

A smart, multilingual chatbot designed to assist new students during **Orientation Week** at **James Cook University Singapore**.  
It provides accurate event information, contact details, and supports both **FAQ-based** and **web-based** semantic retrieval with **ChatGPT integration**.

---

## 🚀 Features

- ✅ Flexible queries (event names, times, locations, registration)  
- ✅ Multi-turn conversation & session memory  
- ✅ Supports English and Chinese (auto-detects language)  
- ✅ Fuzzy matching & typo correction (`Did you mean...?`)  
- ✅ Provides verified contact info (email, phone)  
- ✅ Dual-retrieval system: FAQ + embedded website content  
- ✅ Entity recognition (emails, dates, phone numbers)

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/orientation-chatbot.git
cd orientation-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

```bash
cp .env.example .env
```

### 4. Add your OpenAI API Key to `.env`

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Run the Application

⚠️ Before running, make sure you are inside the **app directory**:

```bash
cd app
```

### 🔹 FastAPI backend

```bash
uvicorn main:app --reload
```

### 🔹 Streamlit frontend

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
.
├── app/
│   ├── image/                         # Logo and image assets
│   ├── strategies/                   # Matching strategies for FAQ queries
│   │   ├── __init__.py               # Init file for strategy module
│   │   ├── base.py                   # Base class for all strategies
│   │   ├── exact.py                  # Exact match strategy
│   │   ├── fuzzy.py                  # Fuzzy match strategy
│   │   ├── keyword.py                # Keyword match strategy
│   ├── app.py                        # Streamlit frontend UI
│   ├── background_info.json          # Static info for orientation (e.g., contacts, campus info)
│   ├── chatbot.py                    # Main chatbot logic and response generation
│   ├── embed_faq.py                  # Script to embed FAQ JSON data
│   ├── embedding_utils.py            # Helper functions for embeddings
│   ├── faq.json                      # Raw FAQ data (non-embedded)
│   ├── faq_embedded.json             # FAQ data with vector embeddings
│   ├── main.py                       # FastAPI backend entry point
│   ├── style.css                     # Custom CSS styles for the Streamlit app
│   ├── web_embed.py                  # Script to embed web content
│   ├── web_embedded.json             # Embedded web page data
│   ├── web_embedding_utils.py        # Web scraping + embedding helpers

```

---

## 🔐 Environment Variables

You should create a `.env` file in the root directory like this:

### ✅ `.env` file (NOT committed)

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 📄 `.env.example` (committed)

```env
# Copy this file to .env and replace with your actual OpenAI key
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🙅‍♂️ .gitignore Setup

Your project should include the following `.gitignore` file to avoid leaking sensitive files:

### 📄 `.gitignore`

```gitignore
# Byte-compiled / cache
__pycache__/
*.py[cod]

# Virtual environments
.venv/
env/
venv/

# Environment variables
.env
.env.*

# IDEs and OS files
.vscode/
.idea/
.DS_Store
Thumbs.db
```

---

## 🧠 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Chatbot Engine:** OpenAI GPT-4 API  
- **Embedding Model:** `text-embedding-ada-002`  
- **Retrieval Strategy:** FAQ + Web-based dual embedding  
- **Data Format:** JSON (for FAQ, embeddings)

---

## 🗺️ Future Features (Planned)

- 📬 Feedback collection system  
- 📅 Event subscription and alert system  
- 🛠️ Full admin interface to update FAQ/web embeddings  
- 🔗 Integration with student portal (optional)

---

## 👨‍💻 Authors

| Name         | Role                  |
|--------------|-----------------------|
| Wang Hongbo  | Backend Developer     |
| Kuang Ziye   | Frontend Developer    |

---

## 📚 Course Info

This chatbot is part of the **CP3407 Software Engineering Project**  
at **James Cook University Singapore**.
