# User Story 1: Flexible Event Inquiry

## User Story
**As a [new student]**, I want to ask the chatbot various types of questions about Orientation Week,  
so that I can get accurate and relevant information quickly without needing to follow a fixed query format.

## Acceptance Criteria

The chatbot should understand and respond to different types of user queries related to Orientation Week, including:

- **General inquiries**:  
  **“Tell me about Orientation Week.”** → The chatbot provides an overview.

- **Event-based queries**:  
  **“What events are happening on Monday?”** → The chatbot lists all events for that day.

- **Location-based queries**:  
  **“Where is the welcome ceremony?”** → The chatbot provides location details.

- **Time-based queries**:  
  **“When does the networking session start?”** → The chatbot provides event timing.

- **Participation-related queries**:  
  **“Do I need to register for the campus tour?”** → The chatbot clarifies registration requirements.

The chatbot should be able to handle **fuzzy queries**, such as:

- **“What’s happening this afternoon?”** → It should return only *afternoon events*.
- **“Are there any fun activities today?”** → It should suggest *social events*.

If an event does not exist or information is missing, the chatbot should provide a **friendly fallback response** instead of leaving the user without an answer.

The chatbot should support both **free-text input** and **menu-based selection** for accessibility.

**So that I can understand the arrangements for Orientation Week in advance and make full preparations.**

---

## Available Deliverables

The chatbot supports **free-text user queries** and understands **different question types**.

The chatbot provides a **sorted list of events** for the queried date, including:

- Time
- Name
- Location
- Description
- Participation details (e.g., registration required)

If users request additional event details, the chatbot should provide **expanded descriptions** upon request.

---

## Tasks & Estimates

### Design the Chatbot Framework
- **Task**: Complete the basic functionalities of the chatbot (e.g., conversation handling, information recognition, etc.)
- **Estimate**: *3 days*

### Build a Database to Handle Multiple Types of Query Responses
- **Task**: Ensure the database contains sufficient responses to handle the various user queries. Try to ensure that the responses are relevant and match the user’s questions.
- **Estimate**: *1 week*

### User Input Parsing
- **Task**: Design a feature to parse user queries.
- **Estimate**: *3 days*

### Keyword Search
- **Task**: Perform a search in the database based on the keywords provided by the user (e.g., time, location, event, etc.) to retrieve relevant responses.
- **Estimate**: *2 days*

### Testing & Validation
- **Task**: Test various different questions to ensure the chatbot can provide appropriate responses.
- **Estimate**: *1 day*


## Class Diagram
![User Story 1 Class Diagram](../image/userstory1class3.drawio.png)


## Sequence Diagram
![User Story 1 Sequence Diagram](../image/userstorysequence1.drawio.png)