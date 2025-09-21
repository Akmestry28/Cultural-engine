from fastapi import FastAPI
from pydantic import BaseModel
from models.cultural_classifier import OptimizedCulturalEngine

app = FastAPI(title="Free Cultural Intelligence Engine")
engine = OptimizedCulturalEngine()

class QueryRequest(BaseModel):
    text: str
    user_id: str = "anonymous"
    region: str = "Unknown"

@app.post("/analyze")
def analyze(request: QueryRequest):
    result = engine.analyze_cultural_context(request.text, {"user_id": request.user_id, "region": request.region})
    return result
