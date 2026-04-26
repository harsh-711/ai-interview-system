# AI Interview System (FastAPI)

## Overview
A backend system that simulates an interview process using REST APIs. It manages sessions, accepts answers, and dynamically moves through questions.

## Features
- Start Interview Session
- Submit Structured Answers
- Dynamic Next Question Logic
- End Interview with Summary
- Error Handling (Invalid session, duplicate answers, timeout)

## Tech Stack
- FastAPI
- Python
- Pydantic
- Uvicorn

## API Endpoints
- POST /interview/start
- POST /interview/answer
- POST /interview/next
- POST /interview/end

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reloads

## 📄 API Documentation
Swagger UI available at:
http://127.0.0.1:8001/docs