from pydantic import BaseModel


class PredictionRequest(BaseModel):
    features: dict[str, int | float | str]


class PredictionResponse(BaseModel):
    prediction: int | str
    model_name: str
    model_alias: str
