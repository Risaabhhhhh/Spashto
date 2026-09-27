from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from ..retrieval.retriever import search

router = APIRouter()

class GuideRequest(BaseModel):
    query: str
    lang: str = "en"

class GuideResponse(BaseModel):
    answer_chunks: List[str]
    sources: List[str]

@router.post("/query", response_model=GuideResponse)
def query_guide(request: GuideRequest):
    chunks, sources = search(request.query)
    return GuideResponse(answer_chunks=chunks, sources=sources)
