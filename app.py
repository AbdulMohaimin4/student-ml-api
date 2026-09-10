from fastapi import FastAPI
from pydantic import BaseModel

APP_VERSION = "1.0.0"

app = FastAPI()


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": APP_VERSION,
    }


@app.post("/predict")
async def predict(request: PredictionRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2,
    }
