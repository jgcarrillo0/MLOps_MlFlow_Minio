import pandas as pd
from fastapi import FastAPI, HTTPException

import mlflow
from api.config import settings
from api.schemas import PredictionRequest, PredictionResponse

app = FastAPI(
    title="Covertype ML API",
    version="0.1.0",
)

mlflow.set_tracking_uri(settings.mlflow_tracking_uri)

model = None


def load_model():
    model_uri = (
        f"models:/{settings.mlflow_model_name}@{settings.mlflow_model_alias}"
    )
    return mlflow.pyfunc.load_model(model_uri)


@app.on_event("startup")
def startup_event() -> None:
    global model

    try:
        model = load_model()
    except Exception:
        model = None


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "Covertype ML API",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str | bool]:
    return {
        "status": "ok",
        "model_loaded": model is not None,
    }


@app.get("/model")
def model_info() -> dict[str, str]:
    return {
        "model_name": settings.mlflow_model_name,
        "model_alias": settings.mlflow_model_alias,
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest) -> PredictionResponse:
    if model is None:
        raise HTTPException(
            status_code=503,
            detail="No model is currently available in MLflow.",
        )

    input_data = pd.DataFrame([request.features])
    prediction = model.predict(input_data)[0]

    if hasattr(prediction, "item"):
        prediction = prediction.item()

    return PredictionResponse(
        prediction=prediction,
        model_name=settings.mlflow_model_name,
        model_alias=settings.mlflow_model_alias,
    )
