from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
import time

app = FastAPI(title="Interview System API")

# -----------------------------
# In-memory storage
# -----------------------------
sessions = {}
answers_store = {}

# -----------------------------
# Schemas (MATCHING TASK)
# -----------------------------
class Question(BaseModel):
    question_id: str
    question_text: str
    difficulty: str
    topic: str
    type: str = "text"


class Answer(BaseModel):
    question_id: str
    answer_text: str
    time_taken: float


class StartRequest(BaseModel):
    candidate_name: Optional[str] = None


class AnswerRequest(BaseModel):
    session_id: str
    answer: Answer


class SessionRequest(BaseModel):
    session_id: str


class Decision(BaseModel):
    next_action: str   # continue | end
    confidence_score: float
    feedback: str


# -----------------------------
# Dummy Question Bank
# -----------------------------
question_bank = [
    Question(
        question_id="q1",
        question_text="What is Python?",
        difficulty="easy",
        topic="basics"
    ),
    Question(
        question_id="q2",
        question_text="Explain OOP concepts",
        difficulty="medium",
        topic="oop"
    ),
    Question(
        question_id="q3",
        question_text="What is FastAPI?",
        difficulty="medium",
        topic="framework"
    ),
]

# -----------------------------
# 1. Start Interview
# -----------------------------
@app.post("/interview/start", status_code=201)
def start_interview(req: StartRequest):
    session_id = str(uuid.uuid4())

    sessions[session_id] = {
        "created_at": time.time(),
        "current_index": 0,
        "completed": False
    }

    answers_store[session_id] = []

    return {
        "session_id": session_id,
        "first_question": question_bank[0]
    }


# -----------------------------
# 2. Submit Answer
# -----------------------------
@app.post("/interview/answer")
def submit_answer(req: AnswerRequest):
    if req.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Invalid session_id")

    session = sessions[req.session_id]

    if session["completed"]:
        raise HTTPException(status_code=400, detail="Interview already ended")

    # Duplicate check
    for ans in answers_store[req.session_id]:
        if ans["question_id"] == req.answer.question_id:
            raise HTTPException(status_code=409, detail="Duplicate answer")

    answers_store[req.session_id].append(req.answer.dict())

    return {"message": "Answer recorded successfully"}


# -----------------------------
# 3. Get Next Question
# -----------------------------
@app.post("/interview/next")
def get_next_question(req: SessionRequest):
    if req.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Invalid session_id")

    session = sessions[req.session_id]

    # Timeout check (5 minutes)
    if time.time() - session["created_at"] > 300:
        raise HTTPException(status_code=408, detail="Session timeout")

    index = session["current_index"] + 1

    if index >= len(question_bank):
        session["completed"] = True

        return {
            "decision": {
                "next_action": "end",
                "confidence_score": 0.9,
                "feedback": "Interview completed"
            },
            "question": None
        }

    session["current_index"] = index

    return {
        "decision": {
            "next_action": "continue",
            "confidence_score": 0.8,
            "feedback": "Moving to next question"
        },
        "question": question_bank[index]
    }


# -----------------------------
# 4. End Interview
# -----------------------------
@app.post("/interview/end")
def end_interview(req: SessionRequest):
    if req.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Invalid session_id")

    sessions[req.session_id]["completed"] = True

    total_answers = len(answers_store[req.session_id])

    return {
        "message": "Interview ended successfully",
        "summary": {
            "total_questions": total_answers,
            "average_score": round(0.75, 2),
            "result": "pass" if total_answers >= 2 else "fail"
        }
    }