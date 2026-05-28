from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import UTC, datetime, timedelta

from fastapi import FastAPI, Request

from edf.api.schemas import (
    AnomalyResponse,
    ForecastPoint,
    ForecastResponse,
    SpikeResponse,
)
from edf.utils.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """ """
    setup_logging()
    app.state.models = {
        "forecast": "stub",
        "spike": "stub",
        "anomaly": "stub",
    }
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health() -> dict[str, str]:
    """ """
    return {"status": "ok"}


@app.get("/forecast")
def forecast(request: Request, hours: int = 24) -> ForecastResponse:
    """ """
    model = request.app.state.models["forecast"]
    start = datetime.now(UTC)
    predictions = [
        ForecastPoint(
            timestamp=start + timedelta(hours=i),
            predicted_MW=40000.0,
            lower_95=36000.0,
            upper_95=44000.0,
        )
        for i in range(hours)
    ]
    return ForecastResponse(
        model=model,
        predictions=predictions,
    )


@app.get("/spike-probability")
def spike_probability(request: Request) -> SpikeResponse:
    """ """
    return SpikeResponse(
        timestamp=datetime.now(UTC),
        probability=0.05,
        threshold_MW=48000.0,
        model=request.app.state.models["spike"],
    )


@app.get("/anomaly-score")
def anomaly_score(request: Request) -> AnomalyResponse:
    """ """
    return AnomalyResponse(
        anomaly_score=0.0,
        residual_zscore=0.0,
        is_anomaly=False,
        top_contributing_features=[],
        model=request.app.state.models["anomaly"],
    )
