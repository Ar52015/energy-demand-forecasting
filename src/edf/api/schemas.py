from datetime import datetime

from pydantic import BaseModel


class ForecastPoint(BaseModel):
    timestamp: datetime
    predicted_MW: float
    lower_95: float
    upper_95: float


class ForecastRequest(BaseModel):
    as_of: datetime | None = None


class ForecastResponse(BaseModel):
    model: str
    prediction: list[ForecastPoint]


class SpikeRequest(BaseModel):
    as_of: datetime | None = None


class SpikeResponse(BaseModel):
    timestamp: datetime
    probability: float
    threshold_MW: float
    model: str


class AnomalyRequest(BaseModel):
    timestamp: datetime | None = None
    observed_MW: float | None = None


class AnomalyResponse(BaseModel):
    anamoly_score: float
    residual_zscore: float
    is_anomaly: bool
    top_contributing_features: list[tuple[str, float]]
    model: str
