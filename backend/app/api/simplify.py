from fastapi import APIRouter
from pydantic import BaseModel
from ..models.simplifier import simplify_text

router = APIRouter()

class SimplifyRequest(BaseModel):
    text: str
    target_lang: str = "en"

class SimplifyResponse(BaseModel):
    simplified_text: str

@router.post("/simplify", response_model=SimplifyResponse)
def simplify(request: SimplifyRequest):
    simplified = simplify_text(request.text, request.target_lang)
    return SimplifyResponse(simplified_text=simplified)
