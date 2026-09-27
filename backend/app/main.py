from fastapi import FastAPI
from contextlib import asynccontextmanager
from .api import simplify, guide, feedback
from .models.simplifier import load_model
from .models.embedder import load_embedder
from .feedback_db import init_db

from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB and optionally pre-load models
    init_db()
    load_model()
    load_embedder()
    yield

app = FastAPI(title="Spashto API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(simplify.router, tags=["Simplify"])
app.include_router(guide.router, prefix="/guide", tags=["Guide"])
app.include_router(feedback.router, tags=["Feedback"])

@app.get("/")
def read_root():
    return {"status": "ok"}
