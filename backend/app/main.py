from fastapi import FastAPI
from contextlib import asynccontextmanager
from .api import simplify, guide, feedback
from .models.simplifier import load_model
from .models.embedder import load_embedder
from .feedback_db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB and optionally pre-load models
    init_db()
    load_model()
    load_embedder()
    yield

app = FastAPI(title="Spashto API", lifespan=lifespan)

app.include_router(simplify.router, tags=["Simplify"])
app.include_router(guide.router, prefix="/guide", tags=["Guide"])
app.include_router(feedback.router, tags=["Feedback"])

@app.get("/")
def read_root():
    return {"status": "ok"}
