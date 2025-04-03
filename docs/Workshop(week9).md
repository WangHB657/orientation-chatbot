# JCU Orientation Chatbot - System Testing Policy and Plan

---

## 📌 System Testing Policy

### Goal
The goal of system testing is to verify that the **JCU Orientation Chatbot** behaves correctly, reliably, and meets customer needs (students, staff) in a real-world environment.

System testing is about **real-world behavior**, not just passing unit tests.

---

### Scope
- Streamlit-based Frontend
- FastAPI-based Backend
- FAQ Database Interaction
- User Query Handling
- Typo Detection and Suggestions
- Error Handling
- Chat History and Caching

---

### Objectives
- Validate the system as a whole (end-to-end).
- Find issues missed during unit testing.
- Ensure the chatbot handles typical and edge-case scenarios.
- Ensure chatbot strictly follows behavior defined in the system prompt.

---

### Policy Rules
1. System Testing must be completed before every major release.
2. Testing will be performed in an environment close to production.
3. Developers cannot system-test their own code.
4. Testing focuses on **the full system**, not just components.
5. Use realistic user queries for all test cases.
6. Document all results and prioritize bug fixing with stakeholders.

---

### Responsibilities
- Developers: Conduct unit testing and fix bugs.
- Testers (or non-developers): Conduct system testing.
- Project team: Track, prioritize, and resolve bugs.

---

## 📌 System Testing Plan

### Objective
- Confirm chatbot's ability to answer JCU SG related queries.
- Validate typo handling, FAQ fallback, unrelated question handling.
- Verify caching, multi-session, and API error handling work correctly.

---

### Test Approach
- **Black-box testing** simulating end-users.
- **Scenario-based testing** using realistic student queries.
- **Iteration-based testing** performed after each development iteration.

---

### Features to be Tested
- Chat creation and management
- User input and chatbot responses
- Typo detection
- FAQ fallback
- Cache mechanism
- API error handling
- History tracking

---

### Test Cases

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC01 | Ask about JCU SG orientation | Bot provides correct orientation information |
| TC02 | User input with typo: "orrientation" | Bot asks: "Did you mean orientation?" and then responds |
| TC03 | Ask about unrelated topic (e.g., NUS courses) | Bot replies: "I can only answer questions related to JCU SG." |
| TC04 | Ask for missing information | Bot says: "Sorry, I couldn't find precise information. Please check the official website." |
| TC05 | Ask the same question twice | Bot uses cached answer |
| TC06 | API connection fails | Bot returns: "Request failed, please try again later." |

---

### Test Schedule

| Activity | Responsible | Time |
| -------- | ----------- | ---- |
| Unit Testing | Developers | During Iteration |
| System Testing | Testers | End of Iteration |
| Bug Fixing | Developers | Next Iteration |

---

### Test Environment
- Localhost deployment (Streamlit frontend + FastAPI backend)
- Realistic FAQ dataset
- Simulated or real user queries

---

### Acceptance Criteria
- All test cases pass.
- No critical or high-severity bugs.
- Chatbot fully complies with system behavior definition.
- Response time < 2 seconds under normal load.

---

### Bug Handling
- All bugs will be recorded in the bug tracker.
- Critical bugs will be fixed before the next iteration.
- Minor bugs will be discussed and prioritized.

---

> Note: Developers should NOT system-test their own code.
> Testers should adopt a user perspective.

