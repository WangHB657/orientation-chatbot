# 🛠️ Iteration Plan for Orientation Chatbot

---

## ✅ Iteration 1: Flexible Event Inquiry

**Objective:**  
Allow the chatbot to answer a wide variety of event-related questions flexibly and clearly.

### Tasks:
- [x] Implement Orientation Week event data structure (FAQ + embedding-ready content).  
- [x] Enable flexible query types: time-based, location-based, general inquiries.  
- [x] Integrate fuzzy query handling (e.g., “fun activities today?” → social events).  
- [x] Format responses with sorted event lists and expandable details.

---

## ✅ Iteration 2: Multi-turn Conversation & Multilingual Support

**Objective:**  
Ensure the chatbot supports contextual follow-ups and understands different languages.

### Tasks:
- [x] Implement session memory for multi-turn conversations.  
- [x] Allow follow-up questions with context-aware handling (e.g., "What about Tuesday?").  
- [x] Add automatic language detection (English, Mandarin, etc.).  
- [x] Enable dynamic language switching during conversation.

---

## ✅ Iteration 3: Contact Information Extraction

**Objective:**  
Provide accurate contact information (email, phone) from verified sources.

### Tasks:
- [x] Tag contact info using entity markers like `[EMAIL]`, `[PHONE]`.  
- [x] Extract relevant info from FAQ and web embeddings.  
- [x] Display verified contact details based on user queries.  
- [x] Prevent fabricated or irrelevant information.

---

## ✅ Iteration 4: Fuzzy Suggestions for Similar Questions

**Objective:**  
Offer fallback suggestions when user input is vague or not understood.

### Tasks:
- [x] Apply semantic similarity and fuzzy matching to identify related questions.  
- [x] Generate “Did you mean...” suggestions based on best matches.  
- [x] Allow user to select a suggested alternative or rephrase.

---

## ✅ Iteration 5: Handling Misspelled Input Gracefully

**Objective:**  
Recognize and auto-correct misspelled or malformed queries.

### Tasks:
- [x] Integrate typo correction using fuzzy/embedding matching.  
- [x] Suggest corrected queries or closest FAQ matches (top 3).  
- [x] Continue answering if intent is confidently detected.  
- [x] Avoid failure due to minor spelling errors.

---
