## Week 2 CP 3407 Workshop 2

### Interview your target users for feedback on their requirements for your software project.

**A:**

- If we can search for more information about the school's “Orientation Week” on a website, I hope it will be simple and efficient. This means that the site is better able to provide the information that the user might need based on the keywords that the user enters. Additionally, summarize the activity content and time as much as possible.

- I hope the website can provide real-time updates so that I don't encounter any issues due to outdated information.

- I want the chatbot to allow users to have multiple rounds of communication and keep a record of those interactions. In addition, I also hope that the chatbot can answer in the language the user communicates in so that the user does not have difficulty reading the message.

---

### Write the requirements document for your project and provide estimation of each user story.

# Orientation Chatbot - User Stories

---

## User Story 1: Flexible Event Inquiry

**As a [new student], I want to ask the chatbot various types of questions about Orientation Week,  
so that I can get accurate and relevant information quickly without needing to follow a fixed query format.**

### Acceptance Criteria:
- The chatbot should understand and respond to different types of user queries related to Orientation Week, including:
  - **General inquiries:** “Tell me about Orientation Week.”
  - **Event-based queries:** “What events are happening on Monday?”
  - **Location-based queries:** “Where is the welcome ceremony?”
  - **Time-based queries:** “When does the networking session start?”
  - **Participation-related queries:** “Do I need to register for the campus tour?”
- The chatbot should be able to handle **fuzzy queries**, such as:
  - “What’s happening this afternoon?” → It should return **afternoon events**.
  - “Are there any fun activities today?” → It should suggest **social events**.
- If an event does not exist or information is missing, the chatbot should provide a **friendly fallback response**.
- The chatbot should support both **free-text input** and **menu-based selection**.

### Available Deliverables:
- The chatbot supports **free-text user queries** and understands **different question types**.
- The chatbot provides a **sorted list of events** for the queried date, including:
  - **Time, name, location, description, participation details.**
- If users request additional event details, the chatbot provides **expanded descriptions**.

---

## User Story 2: Multi-turn Conversation & Multilingual Support

**As a [new student], I want the chatbot to allow users to have multiple rounds of communication and keep a record of those interactions,  
so that I can continue my conversation seamlessly and not have to repeat my queries.**

### Acceptance Criteria:
- The chatbot retains **conversation history within the session**.
- If a user leaves and returns, the chatbot recalls the last **few interactions**.
- Users can refer to previous parts of the conversation:
  - *User:* “What about Tuesday’s events?”  
  - *Chatbot:* Infers the date from the earlier question.
- The chatbot automatically detects the user’s **language preference**.
- It supports **English**, **Mandarin**, and other university-supported languages.

### Available Deliverables:
- The chatbot keeps **short-term conversation history**.
- Conversations can **continue naturally** without repeated context.
- The chatbot **adapts language** based on user input.

---

## User Story 3: Contact Information Extraction

**As a [new student], I want the chatbot to provide official contact details (e.g., email, phone)  
so that I can reach the correct department without having to browse the website myself.**

### Acceptance Criteria:
- When asked about contacting a department, the chatbot returns:
  - **Relevant email addresses** using `[EMAIL]...[/EMAIL]`
  - **Phone numbers** if available
  - **Department/service names** for clarity
- The chatbot should not fabricate contact info.
- Example:
  - *User:* “How do I contact accommodation?”  
  - *Bot:* “You can email [EMAIL]accommodation-singapore@jcu.edu.au[/EMAIL].”

### Available Deliverables:
- Entity-tagged contact info is extracted from FAQ and website.
- The chatbot displays verified **emails and phones** clearly.
- Answers are tailored to the user’s intent.

---

## User Story 4: Fuzzy Suggestions for Similar Questions

**As a [new student], I want the chatbot to suggest related questions when it doesn’t understand mine,  
so that I can still get useful results even if I asked imprecisely.**

### Acceptance Criteria:
- When unsure, the chatbot offers **2–3 similar suggestions**:
  - “Did you mean: …?”
- Fuzzy matching is applied on FAQ and web content.
- Example:
  - *User:* “What is verifcation?”
  - *Bot:* “Did you mean: ‘What is the reporting and verification session?’”
- The chatbot allows the user to select a suggestion or rephrase.

### Available Deliverables:
- GPT or fuzzy matching suggests similar questions.
- Suggestions are based on **semantic similarity or string distance**.
- Users are never left with a dead end.

---

## User Story 5: Handling Misspelled Input Gracefully

**As a [new student], I want the chatbot to recognize common spelling mistakes in my queries  
so that I can still receive helpful responses even if I type something wrong.**

### Acceptance Criteria:
- When a user enters a misspelled keyword (e.g., “accomodaton”, “orientatoin”), the chatbot should:
  - Match it to the correct term using **fuzzy matching** or **semantic similarity**.
  - Suggest the correct version with a message like:  
    *“Did you mean: ‘accommodation’?”*
- If the bot is confident, it can proceed to answer directly but should still **confirm the interpretation**:
  - *“Answering for: ‘Orientation Week’. Let me know if you meant something else.”*
- If no high-confidence match is found, the chatbot should:
  - Offer up to **3 closest suggestions**, or ask the user to rephrase.

### Available Deliverables:
- The chatbot uses fuzzy or embedding-based similarity to match misspelled queries to valid topics.
- In cases of typos, the chatbot responds with:
  > “Sorry, I couldn’t find exact info for ‘verifcation’. Did you mean:  
  > - Verification session  
  > - Student pass formalities  
  > - Orientation registration?”
- This improves user experience and avoids “dead end” interactions.

---
