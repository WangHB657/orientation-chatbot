# CP3407-Chatbot
# Orientation Chatbot Application

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



# Week 2
# CP 3407 Workshop 2

## Activity One

### Interview your target users for feedback on their requirements for your software project.

**A:**

- If we can search for more information about the school's “Orientation Week” on a website, I hope it will be simple and efficient. This means that the site is better able to provide the information that the user might need based on the keywords that the user enters. Additionally, summarize the activity content and time as much as possible.

- I hope the website can provide real-time updates so that I don't encounter any issues due to outdated information.

- I want the chatbot to allow users to have multiple rounds of communication and keep a record of those interactions. In addition, I also hope that the chatbot can answer in the language the user communicates in so that the user does not have difficulty reading the message.

---

## Activity Two

### Write the requirements document for your project and provide estimation of each user story.

#### User Story 1:

**As a [new student], I want to be able to quickly find detailed information about Orientation Week through the university website's chatbot, specifically:**

- When I interact with the chatbot, I can input or select a date, for example, `September 2nd, 2024`.
- The chatbot should, based on the date I input, return a list of all Orientation Week activities for that day, arranged in chronological order.
- For each activity, the chatbot should clearly display the following information:
  - **Activity Time:** For example, `9:00 AM - 10:00 AM`
  - **Activity Name:** For example, `Welcome Ceremony`
  - **Activity Location:** For example, `Gymnasium`
  - **Brief Activity Description:** For example, `Chancellor's address, introduction to the faculties`
  - **Participation Details:** For example, `No registration required`

**So that I can understand the arrangements for Orientation Week in advance and make full preparations.**

**Available deliverables:**

- The chatbot supports users entering or selecting a query date, such as `Orientation Week Monday's events.`
- The chatbot returns all events for that date, sorted by time, and includes a brief description (e.g., whether registration is required, whether personal identification is needed, etc.).

#### User Story 2:

**As a [new student], I want [the chatbot to provide real-time updates] so that [I can be sure I have the most current information and avoid any problems caused by outdated details].**

- To be more specific, the website could learn about the events I'm interested in based on my search history.
- When the schedules of these events change, the website should be able to promptly send me notifications.

**Available deliverables:**

- When there are changes to the event schedule, the chatbot will display the updated information as soon as the user enters the chatbot.
- When users ask questions like `Are there any updates to today's events?` or similar, the chatbot should respond correctly.
- The chatbot should be able to provide personalized update notifications based on the user's query history. *(For example, when an event the user has searched for changes, the chatbot will display the change information at the top of the conversation as soon as the user interacts with it.)*

#### User Story 3:

**As a [new student], I want the chatbot to [allow users to have multiple rounds of communication and keep a record of those interactions].**

- In addition, I also hope that the chatbot can **answer in the language the user communicates** in so that the user does not have difficulty reading the message.

**Available deliverables:**

- The chatbot remembers previous questions or commands in the current session. If the user returns to the chatbot later, the chatbot can review and continue the previous conversation.
- The conversation history can be temporarily stored *(only within the current session).*
- The chatbot can automatically detect the language used by the user, and if the user switches languages during the conversation, the chatbot should be able to adapt automatically.