# 🚀 AI Interview System (FastAPI)

## 📌 Overview
The AI Interview System is a backend application built using FastAPI that simulates a real interview process. It manages interview sessions, accepts structured answers, and dynamically controls the flow of questions using RESTful APIs.

This project demonstrates strong backend fundamentals including API contract design, schema validation, and session-based workflow management.

## 🎯 Features
- Session-based interview system
- RESTful API architecture
- Structured request/response schemas using Pydantic
- Dynamic question flow control
- Handles edge cases like invalid session IDs, duplicate answers, and interview completion
- Swagger (OpenAPI) API documentation

## 🛠️ Tech Stack
- FastAPI
- Python
- Uvicorn
- Pydantic

## 🔗 API Endpoints
- POST /interview/start → Start interview session
- POST /interview/answer → Submit answer
- POST /interview/next → Get next question
- POST /interview/end → End interview session

## 📌 Example API Usage

Start Interview:
{
  "candidate_name": "Harsh"
}

Submit Answer:
{
  "session_id": "abc123",
  "answer": {
    "question_id": "q1",
    "answer_text": "Python is a programming language",
    "time_taken": 20
  }
}

Get Next Question:
{
  "session_id": "abc123"
}

End Interview:
{
  "session_id": "abc123"
}

## 🔄 Flow
Start Interview → Submit Answer → Get Next Question → Repeat → End Interview

## ▶️ How to Run
pip install -r requirements.txt
uvicorn main:app --reload --port 8001

## 📄 API Docs
Swagger UI:
http://127.0.0.1:8001/docs

## ⚠️ Edge Cases Handled
- Invalid session ID
- Duplicate answers
- Interview completion handling

## 📊 Highlights
- 4 REST APIs designed and implemented
- Session-based architecture
- Schema validation using Pydantic
- Fully testable using Swagger

## 🔮 Future Improvements
- Database integration (MongoDB / PostgreSQL)
- AI-based answer evaluation
- User authentication system
- Frontend UI (React)
- Cloud deployment (Render / AWS)

