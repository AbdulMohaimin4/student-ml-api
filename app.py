from fastapi import FastAPI
from pydantic import BaseModel

APP_VERSION = "1.1.0"
MODEL_VERSION = "model-1"

app = FastAPI()


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": APP_VERSION,
        "model_version": MODEL_VERSION,
    }


@app.post("/predict")
async def predict(request: PredictionRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2,
    }
