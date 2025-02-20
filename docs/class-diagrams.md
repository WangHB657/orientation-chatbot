# 📌 Chatbot Project Class Diagram

## **📍 Project Overview**
This project is based on **FastAPI** (backend), **OpenAI API** (AI responses), **Web Scraping** (retrieving university website information), **FAQ Mechanism** (matching common questions), and **Streamlit** (frontend UI). The main functionalities include:

- Parsing FAQ data (`faq.json`)
- Accessing university websites for the latest content
- Using a combination of FAQ and website data to generate responses via OpenAI API
- Providing a Web UI where users can interact through Streamlit

---

## **📍 Class Diagram**
Below is the **class diagram** for this project, rendered using **Mermaid**:

```mermaid
classDiagram
    class ChatbotAPI {
        +chatbot_response(query: str) dict
    }

    class FAQHandler {
        +get_faq_response(query: str) str | None
    }

    class WebScraper {
        +fetch_multiple_websites() str
    }

    class GPTHandler {
        +get_gpt_response(query: str, context: str) str
    }

    class ChatbotFrontend {
        +display_ui()
    }

    ChatbotAPI --> FAQHandler : "Query FAQ"
    ChatbotAPI --> WebScraper : "Fetch Websites"
    ChatbotAPI --> GPTHandler : "Call GPT"
    ChatbotFrontend --> ChatbotAPI : "Call API"
