# CP3407-Chatbot
# Orientation Chatbot Application

## Week 1 CP 3407 Workshop 1
## Project Overview
The **Orientation Chatbot Application** is a web-based chatbot designed to enhance the experience and engagement of new students during their orientation program. This chatbot utilizes the **ChatGPT API** to provide immediate and accurate responses to questions about orientation schedules, events, and policies. It also fosters social connections by suggesting interactive games and activities.

By leveraging data from the **Student Affairs department**, the chatbot ensures an engaging, informative, and seamless onboarding experience for students.


## Objectives
- Integrate the **ChatGPT API** to develop a **web-based chatbot** that answers orientation-related questions.
- Promote **engagement** among new students by suggesting games and interactive activities.
- Create a **scalable** and **user-friendly** platform that integrates seamlessly with the existing orientation process.

## Features


### Information Support:
- Respond to frequently asked questions about **orientation schedules**, locations, events, and other key details.
- Provide immediate clarification on **orientation-related policies** or procedures.

### Interactive Suggestions:
- Recommend **games** and activities to encourage socialization among students.
- Suggest **team-building exercises** or group discussions.

### Feedback Collection:
- Collect feedback on the chatbot’s performance to improve future iterations.
- Use feedback to refine the **orientation program**.


## Technology Stack
- **Frontend:** HTML, CSS, JavaScript (React.js)
- **Backend:** Node.js with Express
- **Chatbot Integration:** OpenAI ChatGPT API
- **Database:** MongoDB
- **Deployment:** Heroku or AWS
- **Version Control:** GitHub


## Project Management

### Team Members & Roles:

| **Member Name**  | **Role**                                             | **Responsibilities**                                               |
|------------------|------------------------------------------------------|--------------------------------------------------------------------|
| **Wang Hongbo**  | Project Lead & Developer & UI/UX Designer            | Oversee project development, manage timelines, develop chatbot logic |
| **Kuang Ziye**   | Backend Developer & Data Manager & Frontend Developer| Handle server-side coding, manage database, integrate chatbot with data |



## Week 2 CP 3407 Workshop 2

## Activity One

### Interview your target users for feedback on their requirements for your software project.

**A:**

- If we can search for more information about the school's “Orientation Week” on a website, I hope it will be simple and efficient. This means that the site is better able to provide the information that the user might need based on the keywords that the user enters. Additionally, summarize the activity content and time as much as possible.

- I hope the website can provide real-time updates so that I don't encounter any issues due to outdated information.

- I want the chatbot to allow users to have multiple rounds of communication and keep a record of those interactions. In addition, I also hope that the chatbot can answer in the language the user communicates in so that the user does not have difficulty reading the message.

---

## Activity Two

### Write the requirements document for your project and provide estimation of each user story.

# Orientation Chatbot - User Stories

## User Story 1: Flexible Event Inquiry

**As a [new student], I want to ask the chatbot various types of questions about Orientation Week,  
so that I can get accurate and relevant information quickly without needing to follow a fixed query format.**

### Acceptance Criteria:
- The chatbot should understand and respond to different types of user queries related to Orientation Week, including:
  - **General inquiries:** “Tell me about Orientation Week.” → The chatbot provides an overview.
  - **Event-based queries:** “What events are happening on Monday?” → The chatbot lists all events for that day.
  - **Location-based queries:** “Where is the welcome ceremony?” → The chatbot provides location details.
  - **Time-based queries:** “When does the networking session start?” → The chatbot provides event timing.
  - **Participation-related queries:** “Do I need to register for the campus tour?” → The chatbot clarifies registration requirements.
- The chatbot should be able to handle **fuzzy queries**, such as:
  - “What’s happening this afternoon?” → It should return only **afternoon events**.
  - “Are there any fun activities today?” → It should suggest **social events**.
- If an event does not exist or information is missing, the chatbot should provide a **friendly fallback response** instead of leaving the user without an answer.
- The chatbot should support both **free-text input** and **menu-based selection** for accessibility.

**So that I can understand the arrangements for Orientation Week in advance and make full preparations.**

### Available Deliverables:
- The chatbot supports **free-text user queries** and understands **different question types**.
- The chatbot provides a **sorted list of events** for the queried date, including:
  - **Time, name, location, description, participation details (e.g., registration required).**
- If users request additional event details, the chatbot should provide **expanded descriptions** upon request.

---

## User Story 2: Real-time Event Updates

**As a [new student], I want [the chatbot to provide real-time updates]  
so that [I can be sure I have the most current information and avoid any problems caused by outdated details].**

### Acceptance Criteria:
- The chatbot should be able to **track events that users have searched for before**.
- When an event’s **schedule changes**, the chatbot should:
  - Show the **updated event details** immediately when the user enters the chatbot.
  - Provide a **notification at the top of the conversation** when updates are available.
- Users should be able to ask:  
  - **“Are there any updates to today’s events?”** → The chatbot should return the latest changes.
- The chatbot should allow users to **opt-in or opt-out of event change notifications**.
- The chatbot should support **personalized update tracking**, meaning:
  - If a user has searched for a specific event before, and that event changes,  
    the chatbot should **proactively notify** them the next time they interact.

### Available Deliverables:
- When event details change, the chatbot automatically notifies affected users.
- If users explicitly ask about updates, the chatbot responds with **real-time event modifications**.
- The chatbot keeps track of **user search history** to provide **personalized update notifications**.

---

## User Story 3: Multi-turn Conversation & Multilingual Support

**As a [new student], I want the chatbot to [allow users to have multiple rounds of communication and keep a record of those interactions],  
so that I can continue my conversation seamlessly and not have to repeat my queries.**

### Acceptance Criteria:
- The chatbot should retain **conversation history within the current session**.
- If a user **leaves and returns to the chatbot**, it should be able to:
  - Recall the last **few interactions** and allow users to **continue where they left off**.
- Users should be able to reference previous parts of the conversation:  
  - *User:* “What about Tuesday’s events?”  
  - *Chatbot:* Should infer context from the previous query instead of requiring the user to repeat full details.
- The chatbot should automatically detect the user’s **language preference**.
- If the user **switches languages mid-conversation**, the chatbot should **adapt accordingly**.
- The chatbot should support **English, Mandarin, and other university-supported languages**.

### Available Deliverables:
- The chatbot retains **short-term conversation history** (only within the session).
- Users can **continue conversations without needing to restart queries**.
- The chatbot **automatically detects and adjusts to the user's language**.

---

