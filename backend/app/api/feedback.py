from fastapi import APIRouter
from pydantic import BaseModel
from ..feedback_db import insert_feedback

router = APIRouter()

class FeedbackRequest(BaseModel):
    text: str
    simplified_text: str
    feedback_type: str # e.g. "positive", "negative"

class FeedbackResponse(BaseModel):
    status: str

@router.post("/feedback", response_model=FeedbackResponse)
def submit_feedback(request: FeedbackRequest):
    insert_feedback(request.text, request.simplified_text, request.feedback_type)
    return FeedbackResponse(status="success")
