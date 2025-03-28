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

- **Frontend:** Python Streamlit (for chatbot UI)
- **Backend:** FastAPI (Python REST API)
- **Chatbot Integration:** OpenAI GPT API (via openai-python SDK)
- **Data Source:** Static JSON file (`faq.json`) for FAQ matching
- **Testing:** pytest, requests-mock, Selenium
- **Deployment:** Localhost (for development), can be deployed to Render / Railway / AWS
- **Version Control:** Git & GitHub


## Project Management

### Team Members & Roles:

| **Member Name**  | **Role**                                             | **Responsibilities**                                               |
|------------------|------------------------------------------------------|--------------------------------------------------------------------|
| **Wang Hongbo**  | Project Lead & Developer & UI/UX Designer            | Oversee project development, manage timelines, develop chatbot logic |
| **Kuang Ziye**   | Backend Developer & Data Manager & Frontend Developer| Handle server-side coding, manage database, integrate chatbot with data |

