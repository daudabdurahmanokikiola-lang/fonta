
---

# 🧠 **Fonta AI Study Companion**

**Fonta AI Study Companion** is an **AI-powered learning assistant** designed to help **Nigerian and African students** transform their study materials into interactive quizzes, concise summaries, and guided explanations.

Developed during the **Vibe Coding Hackathon 2025**, Fonta aims to make AI-driven study tools accessible within African educational systems, providing personalized, practical learning support.

---

## 🎥 **Demonstration**

🎬 [View Demo Video](https://photos.google.com/share/AF1QipMFWU08h6s-BGZxJEDUx1M3VoZ20nLJMJV1WrYN8U8G0aaqDydpf2cKw7B3M5cL-w?pli=1&key=MmQxR2RJVXROZm1MNk1jMzh6SjRkbkFybjduckh3)

---

## ✨ **Core Features (Planned & Existing)**

### 🧩 1. AI Note-to-Quiz Generator

* Upload PDFs or paste text notes
* Automatically generate **multiple-choice** and **short-answer** questions
* Include intelligent explanations for each question

### 📘 2. AI Digital Library Summarizer

* Convert long notes into concise summaries
* Save and retrieve study summaries for revision

### 🧮 3. AI Homework Helper

* Step-by-step reasoning for Math, Science, and Essay topics
* Encourages understanding rather than rote memorization

### 🧠 4. Next-Phase Improvements (Planned)

* **Custom MongoDB Database** for user data and summaries
* **In-house AI logic** (no third-party APIs) for question generation and summarization
* **Enhanced backend architecture** with modular AI integration

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

* Built internally for summarization and quiz generation
* Uses NLP techniques and model fine-tuning (no external APIs)
* Integrated through FastAPI endpoints

---

## ⚙️ **Tech Stack**

| Layer           | Technology                 |
| --------------- | -------------------------- |
| **Frontend**    | React, Vite, TypeScript    |
| **Styling**     | Tailwind CSS               |
| **Backend**     | Python, FastAPI            |
| **Database**    | MongoDB                    |
| **AI Logic**    | Custom NLP Models (Python) |
| **File Upload** | React Dropzone             |
| **Icons**       | Lucide React               |

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

### 🗄️ Database Setup (MongoDB)

1. Install [MongoDB Community Server](https://www.mongodb.com/try/download/community) or use [MongoDB Atlas](https://www.mongodb.com/atlas).

2. Create a database named **fonta_ai_db**.

3. Add your connection string to an `.env` file in the backend directory:

   ```
   MONGO_URI=mongodb://localhost:27017/fonta_ai_db
   ```

4. The backend will connect automatically once configured.

---

## 👥 **Team Structure & Roles**

| Team Member              | Role                                       | Responsibilities                                                                                                                                                            |
| ------------------------ | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AI Software Engineer** | AI Development & Backend Integration       | Designs and builds AI logic using Python; integrates model functions for summarization and quiz generation; ensures efficient communication between backend and AI modules. |
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

## 🔮 **Future Roadmap**

* [ ] Implement full MongoDB integration for users and study data
* [ ] Replace all third-party AI services with local AI modules
* [ ] Introduce speech and image input processing
* [ ] Develop a chat-style interface for real-time study assistance
* [ ] Expand subject coverage and analytics dashboard

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
  ├── app.py
  ├── requirements.txt
  ├── routes/
  ├── models/
  │   └── ai/      → AI logic scripts go here
  ├── utils/
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

✅ *Repository structured and collaboration-ready*
📅 *Phase:* System organization complete — implementation phase begins next

---

