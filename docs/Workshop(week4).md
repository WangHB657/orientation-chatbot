# **User Story 1: Flexible Event Inquiry**

## **User Story**
As a **[new student]**, I want to ask the chatbot various types of questions about Orientation Week,  
so that I can get accurate and relevant information quickly without needing to follow a fixed query format.

---

## **Acceptance Criteria**
The chatbot should understand and respond to different types of user queries related to Orientation Week, including:

- **General inquiries:**  
  - _Example:_ "Tell me about Orientation Week."  
  - _Response:_ The chatbot provides an overview.

- **Event-based queries:**  
  - _Example:_ "What events are happening on Monday?"  
  - _Response:_ The chatbot lists all events for that day.

- **Location-based queries:**  
  - _Example:_ "Where is the welcome ceremony?"  
  - _Response:_ The chatbot provides location details.

- **Time-based queries:**  
  - _Example:_ "When does the networking session start?"  
  - _Response:_ The chatbot provides event timing.

- **Participation-related queries:**  
  - _Example:_ "Do I need to register for the campus tour?"  
  - _Response:_ The chatbot clarifies registration requirements.

### **Handling Fuzzy Queries**
The chatbot should be able to handle **unclear or flexible queries**, such as:

- _Example:_ "What’s happening this afternoon?"  
  - _Response:_ It should return only **afternoon events**.

- _Example:_ "Are there any fun activities today?"  
  - _Response:_ It should suggest **social events**.

### **Fallback Mechanism**
If an event **does not exist** or **information is missing**, the chatbot should provide a **friendly fallback response** instead of leaving the user without an answer.

### **Input Methods**
The chatbot should support both:
- **Free-text input** (users can type queries freely)
- **Menu-based selection** (predefined options for easier accessibility)

**So that** I can understand the arrangements for Orientation Week in advance and make full preparations.

---

## **Available Deliverables**
- ✅ The chatbot supports **free-text user queries** and understands **different question types**.
- ✅ The chatbot provides a **sorted list of events** for the queried date, including:
  - **Time, Name, Location, Description, Participation details** (e.g., registration required).
- ✅ If users request additional event details, the chatbot should provide **expanded descriptions** upon request.

---

# **Breakdown of Tasks**

## **1️⃣ Design the Chatbot Framework**
**Task:** Complete the basic functionalities of the chatbot.

### **Content:**
- Set up **FastAPI** as the backend.
- Define **API endpoints** to receive user input and return responses.
- Implement **basic conversation flow control** to ensure the chatbot can handle simple interactions.
- Enable the chatbot to have **basic conversation processing capabilities**.
- Allow the chatbot to **detect and interpret user input**.

**Estimate:** **3 days**

---

## **2️⃣ Build a Database to Handle Multiple Types of Query Responses**
**Task:** Ensure the database contains sufficient responses to handle various user queries. Try to ensure that the responses are relevant and match the user’s questions.

### **Content:**
- Create a structured FAQ database.
- Store **different types of queries** (_general, event-based, location-based_).
- The database should include at minimum:
  - **Event Name**
  - **Date & Time**
  - **Location**
  - **Description**

**Estimate:** **7 days**

---

## **3️⃣ User Input Parsing**
**Task:** Design a feature to parse user queries.

### **Content:**
- Implement **natural language processing** to break down user input.
- Detect **key components** such as:
  - **Date**
  - **Event**
  - **Location**
  - **Intent**
- Standardize input to **match the database structure** for accurate results.

**Estimate:** **3 days**

---

## **4️⃣ Keyword Search**
**Task:** Perform a search in the database based on **keywords provided by the user** (_e.g., time, location, event_) to retrieve relevant responses.

### **Content:**
- Implement **keyword extraction** from user input.
- Search the **FAQ or event database** for matches.
- Return **the most relevant event details**.
- Ensure that if **no exact match** is found, **similar results** are provided.

**Estimate:** **2 days**

---

## **5️⃣ Testing & Validation**
**Task:** Test various different questions to ensure the chatbot can provide appropriate responses.

### **Content:**
- **Test responses** for various question types (_time, location, contact information, lists, etc._).
- **Test the retrieval process** from the **FAQ database**.
- **Test scenarios** where the **question does not exist in the FAQ database**.
- **Test keyword-based queries**.

**Estimate:** **2 days**


---


## Class Diagram
![Class Diagram](../image/class-diagram(new).png)


---


## Sequence Diagram
![Sequence Diagram](../image/sequence-diagram(new).png)



# **User Story 2: Multi-turn Conversation & Multilingual Support**

## **User Story**  
As a **[new student]**, I want the chatbot to allow users to have multiple rounds of communication and keep a record of those interactions,  
so that I can continue my conversation seamlessly and not have to repeat my queries.

---

## **Acceptance Criteria**  
The chatbot should retain **session-based memory** and support multiple languages, enabling natural and personalized communication.

### **Conversation Continuity**
- The chatbot should remember key context from earlier messages in the same session.  
  - _Example:_  
    - **User:** “What events are on Monday?”  
    - **User (later):** “What about Tuesday?”  
    - _Response:_ The chatbot understands "Tuesday" refers to Orientation Week events.
- Users should not have to repeat the same context.

### **Session History**
- The chatbot retains **conversation history during a session**.
- If a user **refreshes or returns**, the chatbot can **recall the last few interactions**.
- Users can refer back to past responses.

### **Multilingual Support**
- The chatbot **automatically detects** the user’s input language.
- It supports **at least English and Mandarin** (other university-supported languages can be considered later).
- _Example:_  
  - **User (in Mandarin):** “有哪些活动是在星期二？”  
  - _Response (in Mandarin):_ “星期二的活动包括校园导览、学生证办理和欢迎晚会。”

**So that** international students can communicate comfortably in their preferred language and navigate orientation smoothly.

---

## **Available Deliverables**
- ✅ The chatbot stores and recalls short-term **session memory**.
- ✅ Multi-turn conversations continue **without repeated context**.
- ✅ Language detection is implemented for **automatic language switching**.

---

# **Breakdown of Tasks**

## **1️⃣ Implement Session Memory**
**Task:** Enable the chatbot to remember the current session’s dialogue context.

### **Content:**
- Store **chat history** within session state.
- Track the **most recent user intent** and parameters (e.g., date, event type).
- Support **follow-up messages** referencing earlier inputs.

**Estimate:** **3 days**

---

## **2️⃣ Build Context Parser**
**Task:** Interpret references in follow-up messages.

### **Content:**
- Identify follow-up patterns like “What about…” or “And then?”
- Resolve pronouns and vague terms using **prior interactions**.
- Enable chatbot to **fill in missing context** based on history.

**Estimate:** **3 days**

---

## **3️⃣ Implement Language Detection**
**Task:** Automatically detect language from user input.

### **Content:**
- Use a **language detection library** (e.g., `langdetect` or `fastText`).
- Identify language before each message is processed.
- Store user language preference in session state.

**Estimate:** **2 days**

---

## **4️⃣ Add Multilingual Support**
**Task:** Enable the chatbot to respond in the detected language.

### **Content:**
- Translate responses using **bilingual templates** or integrate **translation APIs** (optional for future).
- Include **Mandarin responses** in the database or templates.
- Make the response structure **language-agnostic** where possible.

**Estimate:** **3 days**

---

## **5️⃣ Testing & Validation**
**Task:** Ensure the chatbot functions correctly across languages and follow-up scenarios.

### **Content:**
- Test **follow-up queries** for contextual consistency.
- Test **language switching** with mixed and multilingual input.
- Confirm chatbot responses are accurate and coherent.

**Estimate:** **2 days**


# **User Story 3: Contact Information Extraction**

## **User Story**  
As a **[new student]**, I want the chatbot to provide official contact details (e.g., email, phone),  
so that I can reach the correct department without having to browse the website myself.

---

## **Acceptance Criteria**  
The chatbot should extract and return **verified contact information** when prompted by user queries.

### **Contact Retrieval**
- When asked about contacting a department or service, the chatbot should provide:
  - ✅ **Email addresses** using a standard format like:  
    _“You can email [EMAIL]accommodation-singapore@jcu.edu.au[/EMAIL]”_
  - ✅ **Phone numbers** if available
  - ✅ **Department/service names** to ensure clarity

- The chatbot **must not fabricate** any contact details.
- Contact information should be based on:
  - Existing FAQ data
  - Verified information from the university’s website
  - Embedded background knowledge

### **Query Examples**
- _User:_ “How do I contact accommodation?”  
  _Bot:_ “You can email [EMAIL]accommodation-singapore@jcu.edu.au[/EMAIL].”

- _User:_ “Who should I call about visa issues?”  
  _Bot:_ “Please contact the international student support team at +65 6709 3888.”

### **Fallback Handling**
- If contact info is **not available**, the chatbot should say:
  > “I’m sorry, I couldn’t find contact information for that department. Would you like me to search the website for you?”

**So that** students can save time and get in touch with the right department directly.

---

## **Available Deliverables**
- ✅ The chatbot can extract and display **entity-tagged contact details** (email, phone).
- ✅ Verified answers are displayed clearly in user-friendly format.
- ✅ Contact responses are **tailored to user intent** and based on real data.

---

# **Breakdown of Tasks**

## **1️⃣ Design Contact Entity Extractor**
**Task:** Create a function that identifies contact-related queries and extracts the intent.

### **Content:**
- Detect queries like “How to contact…” / “What’s the email for…” / “Phone number for…”
- Use **intent classification** or keyword rules to identify contact queries
- Store mappings of services → contact info

**Estimate:** **2 days**

---

## **2️⃣ Build Verified Contact Info Dataset**
**Task:** Prepare a structured dataset with verified contact details.

### **Content:**
- Extract emails and phone numbers from FAQ and official website
- Store each entry with:
  - **Service name**
  - **Email (if any)**
  - **Phone (if any)**
  - **Department type/category**

**Estimate:** **2 days**

---

## **3️⃣ Develop Query-to-Entity Matching**
**Task:** Implement logic to match user queries to contact entities.

### **Content:**
- Use **string similarity** and **semantic search** to map user input to known services
- Handle variations like:
  - “accomodaton” → “accommodation”
  - “international office” → “student support”

**Estimate:** **2 days**

---

## **4️⃣ Display Output in Clean Format**
**Task:** Format the chatbot’s reply with consistent contact info presentation.

### **Content:**
- Display email with `[EMAIL]...[/EMAIL]` format
- Show phone number clearly and consistently
- Highlight service name in the response
- Add fallback when data is missing

**Estimate:** **1 day**

---

## **5️⃣ Testing & Validation**
**Task:** Ensure chatbot returns correct contact info or appropriate fallback messages.

### **Content:**
- Test multiple phrasing variants:  
  _“How do I reach IT support?” → “IT Help Desk”_  
  _“Visa problems contact?” → “International Support”_
- Verify chatbot doesn’t make up contact data
- Confirm output is clean and readable

**Estimate:** **1 day**

# **User Story 4: Fuzzy Suggestions for Similar Questions**

## **User Story**  
As a **[new student]**, I want the chatbot to suggest related questions when it doesn’t understand mine,  
so that I can still get useful results even if I asked imprecisely.

---

## **Acceptance Criteria**  
The chatbot should provide **fuzzy suggestions** when it cannot match a user query exactly.

### **Suggestion System**
- If a user asks a question that doesn't match any FAQ or data exactly:
  - The chatbot suggests **2–3 similar questions** based on:
    - Semantic similarity
    - String distance
    - FAQ tag/category

- _Example:_  
  - **User:** “What is verifcation?”  
  - **Bot:**  
    > “Did you mean:  
    > • What is the reporting and verification session?  
    > • What documents do I need for verification?  
    > • Where is the reporting venue?”

### **User Selection Handling**
- The chatbot allows users to:
  - Click on a suggested question
  - Or rephrase their query

### **Confidence Threshold**
- If the chatbot is **uncertain**, it must **not guess the answer**.
- Instead, it should **ask for clarification** or **suggest similar questions**.

### **Fallback Option**
- If **no close matches** exist:
  - The chatbot should say:
    > “I’m not sure I understand. Could you rephrase that?”

**So that** I won’t be left confused when my query isn’t clear or properly phrased.

---

## **Available Deliverables**
- ✅ The chatbot provides **2–3 semantically similar question suggestions** when uncertain.
- ✅ Users can **click on a suggestion** to receive an answer.
- ✅ The chatbot **handles vague and imprecise inputs gracefully**.

---

# **Breakdown of Tasks**

## **1️⃣ Implement Fuzzy Matching Engine**
**Task:** Match user queries to existing questions using fuzzy logic.

### **Content:**
- Use libraries like `fuzzywuzzy` or `RapidFuzz`
- Integrate **Levenshtein distance** and **embedding similarity**
- Score all potential matches and return top 3

**Estimate:** **2 days**

---

## **2️⃣ Build Suggestion Renderer**
**Task:** Display the suggestions in a clean, clickable list format.

### **Content:**
- Render suggestions clearly in the chatbot
- Allow user to select a suggestion to continue
- Fallback option to rephrase the query

**Estimate:** **2 days**

---

## **3️⃣ Create Semantic Search Layer**
**Task:** Use pre-embedded vectors of FAQ questions for similarity search.

### **Content:**
- Precompute embeddings of all FAQs
- On new input, compute vector and find **nearest neighbors**
- Return the closest 2–3 matches

**Estimate:** **2 days**

---

## **4️⃣ Handle Edge Cases**
**Task:** Define behavior when no matches are found.

### **Content:**
- Set a **confidence threshold**
- If below threshold, say:  
  _“I couldn’t find anything similar. Could you try rephrasing it?”_
- Avoid suggesting irrelevant questions

**Estimate:** **1 day**

---

## **5️⃣ Testing & Validation**
**Task:** Ensure fuzzy suggestions work across varied scenarios.

### **Content:**
- Test for typos:  
  _“regstration” → “registration”_
- Test vague inputs:  
  _“activities?” → “What events are happening this week?”_
- Test multiple phrasing styles

**Estimate:** **1 day**

# **User Story 5: Handling Misspelled Input Gracefully**

## **User Story**  
As a **[new student]**, I want the chatbot to recognize common spelling mistakes in my queries,  
so that I can still receive helpful responses even if I type something wrong.

---

## **Acceptance Criteria**  
The chatbot should detect **typos or spelling mistakes** and still return helpful responses or suggestions.

### **Typo Detection & Correction**
- When a query contains misspelled words (e.g., “accomodaton”, “orientatoin”):
  - The chatbot should **detect** the typo
  - **Suggest the corrected version**, or  
  - **Proceed with answering** if confident, while still confirming interpretation

- _Example:_  
  - **User:** “Tell me about orientatoin week.”  
  - **Bot:**  
    > “Answering for: ‘Orientation Week’. Let me know if you meant something else.”

- _Example:_  
  - **User:** “How to apply for accomodaton?”  
  - **Bot:**  
    > “Did you mean: ‘accommodation’? Here’s the info for applying to campus accommodation.”

### **Unclear or Ambiguous Input**
- If no clear match is found:
  - The bot should offer **up to 3 closest suggestions**
  - Or politely ask the user to rephrase

### **Avoid Misleading Answers**
- The bot **must not fabricate** or assume with low confidence
- A fallback message should guide the user

### **Language Sensitivity**
- Typo correction should consider:
  - English
  - Mandarin Pinyin (if typed in Latin characters)

**So that** even if users make small mistakes, they won’t get stuck or confused.

---

## **Available Deliverables**
- ✅ The chatbot uses **fuzzy and embedding-based similarity** to detect spelling errors
- ✅ Misspelled queries are auto-corrected or matched with high confidence
- ✅ Users are notified of corrections and allowed to confirm or rephrase

---

# **Breakdown of Tasks**

## **1️⃣ Integrate Typo Detection Module**
**Task:** Use typo correction tools or fuzzy logic to detect and correct misspelled input.

### **Content:**
- Integrate libraries such as `SymSpell`, `TextBlob`, or `RapidFuzz`
- Compare input with known keywords and FAQ entries
- Return best matches with confidence score

**Estimate:** **2 days**

---

## **2️⃣ Implement Confidence-Based Correction**
**Task:** Determine when to auto-correct vs. ask for user confirmation.

### **Content:**
- Define confidence threshold (e.g., 85%)
- If confidence > threshold, auto-correct and proceed
- Else, return “Did you mean…” message

**Estimate:** **2 days**

---

## **3️⃣ Create User-Friendly Correction Responses**
**Task:** Format responses with correction suggestions.

### **Content:**
- Highlight corrected term in response
- Allow user to confirm or reject correction
- Keep interaction natural and friendly

**Estimate:** **1 day**

---

## **4️⃣ Build Fallback Suggestion System**
**Task:** Handle inputs that remain unrecognized.

### **Content:**
- Offer 2–3 close suggestions if confident
- Else, reply:  
  _“Sorry, I didn’t get that. Could you try rephrasing?”_

**Estimate:** **1 day**

---

## **5️⃣ Testing & Validation**
**Task:** Test chatbot responses to common misspellings and ambiguous input.

### **Content:**
- Test input like:  
  _“verifcation”, “intarnational offce”, “regstration”_
- Check corrected suggestions and fallback logic
- Confirm messages are accurate and user-friendly

**Estimate:** **1 day**

