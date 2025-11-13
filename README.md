
---

# 🧠 **Fonta AI Study Companion**

**Fonta AI Study Companion** is an **AI-powered learning assistant** designed to help **Nigerian and African students** transform their study materials into interactive quizzes, concise summaries, and guided explanations.

Developed during the **Vibe Coding Hackathon 2025**, Fonta aims to make AI-driven study tools accessible within African educational systems, providing personalized, practical learning support.

---

## 🎥 **Demonstration**

🎬 [View Demo Video](https://photos.google.com/share/AF1QipMFWU08h6s-BGZxJEDUx1M3VoZ20nLJMJV1WrYN8U8G0aaqDydpf2cKw7B3M5cL-w?pli=1&key=MmQxR2RJVXROZm1MNk1jMzh6SjRkbkFybjduckh3)

---

## ✨ **Core Features**

### 📘 1. Advanced PDF Summarizer (NEW)

* Upload PDFs up to 400 pages
* Context-preserving chunking with overlap
* Extracts verbatim definitions from source material
* Generates key bullet points (max 30)
* Creates question-style self-test prompts
* Preserves academic terminology and domain-specific language

### 🧩 2. Comprehensive Quiz Generator (NEW)

* Generates 50 high-quality questions per quiz
  * 35 multiple-choice questions (MCQs)
  * 15 short-answer questions
* Pagination: 5 questions per page (10 pages total)
* Mix of easy/medium/hard difficulty levels
* Intelligent distractors for MCQs based on common student errors
* Free users: 2 quiz attempts (upgradable to unlimited)

### 🧮 3. AI Homework Helper (NEW)

* Step-by-step solutions with detailed reasoning
* Support for Math, Science, Essay Writing, and General topics
* Includes common mistakes and tips
* Practice question recommendations
* Nigerian educational context integration

---

## 🏗️ **Project Architecture**

Fonta follows a **modular full-stack structure**:

```
project/
│
├── frontend/   → React + Vite + TypeScript + Tailwind (User Interface)
│
└── backend/    → Python FastAPI (AI Logic, Database, and API)
```

### **Frontend Responsibilities**

* User interface and experience
* File uploads, data visualization, and result rendering
* API communication with backend

### **Backend Responsibilities**

* Manages API endpoints and database logic
* Hosts in-house AI processing modules
* Connects to MongoDB for data persistence

### **AI Logic Layer (Python)**

* Google Gemini AI integration for advanced language understanding
* Context-preserving prompts for academic content
* Chunking strategy for large documents
* Verbatim definition extraction
* Intelligent quiz generation with difficulty calibration

---

## ⚙️ **Tech Stack**

| Layer           | Technology                      |
| --------------- | ------------------------------- |
| **Frontend**    | React, Vite, TypeScript         |
| **Styling**     | Tailwind CSS                    |
| **Backend**     | Python, FastAPI                 |
| **Database**    | MongoDB Atlas                   |
| **AI Engine**   | Google Gemini Pro               |
| **PDF Processing** | PyMuPDF (fitz)               |
| **File Upload** | React Dropzone, FormData        |
| **Icons**       | Lucide React                    |

---

## 🚀 **Getting Started (Local Setup)**

### 🖥️ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

> Runs locally at: [http://localhost:5173](http://localhost:5173)

---

### ⚙️ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
uvicorn app:app --reload
```

> API runs locally at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🗄️ Database & AI Setup

1. **MongoDB Setup**
   - Install [MongoDB Community Server](https://www.mongodb.com/try/download/community) or use [MongoDB Atlas](https://www.mongodb.com/atlas)
   - Create a database named **fonta_ai_db**
   - Collections will be created automatically: `users`, `summaries`, `quizzes`, `homework_requests`

2. **Google Gemini API Setup**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Gemini Pro
   - Copy the API key for configuration

3. **Environment Configuration**
   - Copy `backend/.env.example` to `backend/.env`
   - Configure the following:

   ```
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=fonta_ai_db
   GEMINI_API_KEY=your_gemini_api_key_here
   LOG_LEVEL=INFO
   ```

4. The backend will connect automatically once configured.

---

## 👥 **Team Structure & Roles**

| Team Member              | Role                                       | Responsibilities                                                                                                                                                            |
| ------------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Daud Abdulrahman** | AI Development & Backend Integration       | Designs and builds AI logic using Python; integrates model functions for summarization and quiz generation; ensures efficient communication between backend and AI modules. |
| **Raji Faruq**           | Full-Stack Developer                       | Implements and maintains frontend and backend components; manages UI and API integration; collaborates on MongoDB schema design.                                            |
| **Chinemerem Nelson**    | Full-Stack Developer                       | Focuses on backend APIs, routing, and database management; supports system optimization and testing.                                                                        |
| **Abdulhammed Toibat**   | Full-Stack Developer & Project Coordinator | Contributes to development on both frontend and backend; oversees coordination, documentation, and workflow consistency.                                                    |

---

## 🧩 **Contribution Guidelines**

Fonta is a collaborative full-stack and AI project.
Each member works within their specialization while maintaining code harmony and shared understanding.

### 🔹 For Full-Stack Developers

* Work in `/frontend` and `/backend` directories.
* Keep APIs consistent with frontend expectations.
* Use clear branch names:

  ```
  git checkout -b feature/frontend-ui
  git checkout -b feature/backend-api
  ```
* Write clear commit messages:

  ```
  feat(scope): add new component or endpoint
  fix(scope): resolve issue
  docs(scope): update documentation
  ```

### 🔹 For AI Engineer

* Develop and maintain AI scripts in `/backend/models/ai/`.
* Implement quiz generation, summarization, and contextual reasoning.
* Keep AI logic modular and reusable.
* Manage model configurations through environment variables.

### 🔹 General Collaboration Tips

* Never commit `.env` files or secrets.
* Run `npm run lint` or `pylint` before committing.
* Pull latest changes before new pushes to avoid merge conflicts.
* Document new routes or functions clearly in comments or a changelog.

---

## 🔐 **Best Practices**

* Use virtual environments (`venv`) for Python dependencies.
* Keep frontend and backend running in separate terminals.
* Validate all user inputs and file uploads.
* Maintain environment-specific configuration files.
* Use `.gitignore` to exclude node modules, virtual environments, and sensitive data.

---

## 🌍 **Target Audience**

* **Primary:** Nigerian university and polytechnic students
* **Secondary:** WAEC, JAMB, and postgraduate learners
* **Focus:** Adaptive study tools built around African exam formats

---

## 🔌 **API Endpoints**

### Summarization
- **POST /api/summarize-pdf**
  - Upload PDF file (up to 400 pages)
  - Returns: verbatim definitions, key bullets, question-style prompts
  - Response: `{ summary_id, file_name, pages, total_words, summary }`

- **GET /api/summaries/{summary_id}**
  - Retrieve a specific summary

- **GET /api/summaries?user_id={user_id}**
  - List all summaries for a user

### Quiz Generation
- **POST /api/generate-quiz**
  - Body: `{ user_id, summary_id }`
  - Generates 50 questions (35 MCQ + 15 short answer)
  - Returns: `{ quiz_id, total_questions, total_pages }`
  - Error 402: Free user attempt limit exceeded

- **GET /api/quiz/{quiz_id}?page={n}**
  - Get paginated quiz questions (5 per page)
  - Returns: `{ quiz_id, page, total_pages, questions }`

- **GET /api/quizzes?user_id={user_id}**
  - List all quizzes for a user

### Homework Help
- **POST /api/homework-helper**
  - Body: `{ user_id, question, topic?, difficulty? }`
  - Returns: `{ request_id, final_answer, step_by_step, tips }`

- **GET /api/homework/{request_id}**
  - Retrieve specific homework help

- **GET /api/homework?user_id={user_id}**
  - List homework help history

### Health & Status
- **GET /api/health**
  - Check system health (database, API, Gemini AI)

---

## 🔮 **Future Roadmap**

* [x] Implement full MongoDB integration for users and study data
* [x] Google Gemini AI integration for advanced language understanding
* [ ] Introduce speech and image input processing
* [ ] Develop a chat-style interface for real-time study assistance
* [ ] Expand subject coverage and analytics dashboard
* [ ] Add collaborative study features

---

## 📚 **Project Context**

Fonta AI Study Companion was developed during the **Vibe Coding Hackathon 2025**, under the **PLP Academy Specialization Module**.
This repository represents the **structured foundation** for scalable, collaborative development combining AI and full-stack technologies.

---

## 🧱 **Folder Structure Overview**

```
frontend/
  ├── src/
  ├── public/
  ├── package.json
  ├── vite.config.ts
  └── ...

backend/
  ├── app.py                    → Main FastAPI application
  ├── requirements.txt          → Python dependencies
  ├── .env.example              → Environment configuration template
  ├── routes/
  │   ├── summarize.py          → PDF summarization endpoints
  │   ├── quiz.py               → Quiz generation endpoints
  │   └── homework.py           → Homework helper endpoints
  ├── models/
  │   └── gemini_ai.py          → Gemini AI integration logic
  ├── utils/
  │   ├── db.py                 → MongoDB connection manager
  │   └── pdf_processor.py      → PDF extraction and chunking
  └── __init__.py

.gitignore
README.md
```

---

## 🤝 **Team Collaboration Flow Diagram**

```
+----------------+        +--------------------+        +-------------------+
|   Frontend UI  | <----> |   Backend (API)    | <----> |   AI Logic Layer   |
| (React + Vite) |        |  (FastAPI + DB)    |        |  (Python NLP)      |
+----------------+        +--------------------+        +-------------------+
       |                          |     ^
       |   Fetch & display data   |     |
       |                          |     +---> MongoDB
       v                          v
   Browser UI          Backend handles AI calls & data flow
```

**Workflow summary**

* The **Frontend team** builds the interface and communicates with backend APIs.
* The **Backend team** handles endpoints, routes, and connects with MongoDB.
* The **AI Engineer** develops Python modules that the backend invokes for processing.
* All modules interact seamlessly to deliver intelligent study assistance.

---

## 💬 **Acknowledgement**

Special thanks to **Vibe Coding**, **PLP Academy**, and our mentors for the opportunity, resources, and mentorship that made Fonta possible.

---

## ⚡ **Status**

✅ **Backend Enhanced with Gemini AI Integration**
✅ **MongoDB Atlas Integration Complete**
✅ **Advanced PDF Summarization (400 pages, context-preserving)**
✅ **50-Question Quiz Generator with Pagination**
✅ **Step-by-Step Homework Helper**
📅 **Phase:** Core AI features implemented — ready for frontend integration and testing

---

