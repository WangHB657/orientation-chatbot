# 📚 CP3407-Chatbot  
## Orientation Chatbot Application (Enhanced Version)

---

## 🚀 Project Overview

The **Orientation Chatbot Application** is an intelligent assistant developed for **James Cook University Singapore (JCU SG)**.  
It provides immediate and accurate answers to frequently asked questions regarding orientation schedules, enrolment, academic support, accommodation, and campus services.

By integrating **ChatGPT (GPT-4)** with semantic search (RAG-lite), the chatbot retrieves relevant information from two main sources:
- A structured **FAQ knowledge base**
- Official **JCU website content**, crawled and embedded

This ensures that students receive contextual, friendly, and fact-based responses throughout their orientation journey.

---

## 🎯 Objectives

- Build a **web-based chatbot** that answers questions about JCU SG orientation using natural language
- Combine **FAQ matching** and **website content embedding** for better coverage
- Automatically extract important contact details (email, phone, location, etc.)
- Provide a user-friendly interface and scalable architecture

---

## 💡 Features

### 🧠 Smart Q&A Support
- Embedding-based retrieval of top-matching **FAQs**
- Embedding-based retrieval of relevant **website paragraphs**
- Entity-enhanced context using `[EMAIL]`, `[PHONE]`, `[DATE]` tags
- GPT-4 generates conversational, contextual answers

### 📬 Accurate Contact Info Extraction
- Automatically detects and outputs email addresses, phone numbers, and dates when present in context
- Helps students know exactly whom to contact and how

### 📚 Orientation Information Coverage
- Orientation schedules, location and reporting procedures
- Enrolment status, study load reduction, academic caution
- Student accommodation, events, safety reporting

### 🧪 Feedback-Ready
- Modular backend structure for future feedback integration
- Easily extendable dataset and answer accuracy tracking

---

## 🧱 Technology Stack

| Layer         | Tools Used                                     |
|---------------|------------------------------------------------|
| **Frontend**  | `Streamlit` – for chatbot UI                   |
| **Backend**   | `FastAPI` – for API logic and GPT integration  |
| **LLM API**   | `OpenAI GPT-4` via `openai` Python SDK         |
| **Embedding** | `text-embedding-ada-002` – for FAQ and web content |
| **Data**      | `faq.json`, `faq_embedded.json`, `web_embedded.json` |
| **Versioning**| `Git`, `GitHub`                                |

---

## ⚙️ Retrieval + Prompt Logic

### 🧠 1. Dual Embedding-Based Retrieval

- User input is converted into a query embedding using `text-embedding-ada-002`
- The system retrieves top-matching content from:
  - ✅ **FAQ embeddings**
  - ✅ **Website paragraph embeddings**
- Top 3 results from each are selected to form the final context

### 🧾 2. Prompt Construction

The chatbot builds a GPT prompt using both FAQ and website content like this:

You are an Orientation Assistant Bot for James Cook University Singapore.

You will answer student questions using the following FAQ and website information:

--- FAQ --- Q: ... A: ...

--- Website --- Source: ... [EMAIL] ... [/EMAIL] [PHONE] ... [/PHONE]

Instructions:

If any contact information such as [EMAIL], [PHONE], or [DATE] is present, include it clearly in the response.

Only provide information relevant to the user's question.

Do not make up or guess answers.

Answer only about JCU SG.

Question: {user question}

Answer:

### 🤖 3. GPT-4 Response

- The prompt is passed to the GPT-4 API
- GPT generates a friendly, context-aware, and structured response
- Emails, dates, and phone numbers are clearly included if available

---

## 📦 Data Files

| File Name             | Description                                     |
|----------------------|-------------------------------------------------|
| `faq.json`            | Manually curated FAQ dataset                    |
| `faq_embedded.json`   | Vectorized embeddings of all FAQs               |
| `web_embedded.json`   | Embeddings from crawled and segmented JCU pages |

---

## 👥 Project Team

| Name         | Role                                           | Responsibilities                                                     |
|--------------|------------------------------------------------|----------------------------------------------------------------------|
| Wang Hongbo  | Team Lead, Full-Stack Developer, UI/UX Designer | Designed system architecture, frontend, GPT + embedding integration |
| Kuang Ziye   | Backend Developer, Data Engineer                | Developed backend API, handled data processing and embedding logic  |

---

## 📈 Future Improvements

- Add a **feedback collection system** for chatbot evaluation
- Support **multi-language interactions** (e.g., English + Chinese)
- Add **chat history and multi-turn conversations**
- Deploy to the cloud (e.g., Render, Railway, AWS)
- Visualize **retrieved FAQ / website chunks** for transparency

---
