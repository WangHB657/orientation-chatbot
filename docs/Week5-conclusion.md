# Week 5 prac

## Activity One and Activity Two

I found that in the current code and classes, not every part strictly follows the **Single Responsibility Principle (SRP)**.  

In the **"Chatbot System"** class, three tasks are handled simultaneously:  

- `fetch_faq_data()`
- `call_openai_api()`
- Processing user input and responses  

![Week5 1](../image/Week5%201.png)

In the **"Knowledgebase"** class, two functionalities are combined:  

- Time queries  
- Retrieving event information  

![Week5 2](../image/Week5%202.png)

Some parts of the code also do not follow the **DRY (Don't Repeat Yourself)** principle.  
For example, there are multiple occurrences of HTML information parsing functionalities in my code, such as in `fetch_multiple_websites()`.  
We should consolidate these functionalities into a single method and call it wherever needed.  

---

## Activity 3: Current Limitations & Ongoing Optimizations  

### Our project has currently implemented the following features:

#### 1. Developed a user-friendly **UI frontend** for seamless interaction between users and the chatbot.  
#### 2. Built a fully functional **backend** to support chatbot operations.  
#### 3. Enabled the chatbot to recognize user queries effectively.  
#### 4. Implemented a **two-step response mechanism**:
- The chatbot checks the FAQ data to find relevant answers.  
- If no matching answer is found, it connects to ChatGPT to fetch information from the website, but only for questions related to orientation from the specified site.  

![Week5 3](../image/Week5%203.png)

### Our project currently faces the following challenges:

#### **1. Limited FAQ Detection**  
- The system can only answer questions that exactly match those recorded in the FAQ.  
- If users phrase questions differently, the system fails to recognize them and redirects to ChatGPT.  
- **Optimization in progress**: Implementing **keyword matching and fuzzy matching**.  

#### **2. Long Response Time**  
- Fetching answers, especially from the website, takes a long time.  
- **Optimization in progress**: Implementing **caching** to reduce the number of website fetch requests.  

#### **3. No Chat History Retention**  
- The chatbot does not remember past interactions.  
- It lacks contextual understanding between user queries.  

#### **4. Simple UI Design**  
- The current interface is minimal and could be improved for a better user experience.  
