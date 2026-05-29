from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import UTC, datetime, timedelta

from fastapi import FastAPI, Request

from edf.api.schemas import (
    AnomalyRequest,
    AnomalyResponse,
    ForecastPoint,
    ForecastRequest,
    ForecastResponse,
    SpikeRequest,
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


@app.post("/forecast")
def forecast(
    request: Request, hours: int = 24, body: ForecastRequest | None = None
) -> ForecastResponse:
    """ """
    # currently a stub
    if body:
        pass

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


@app.post("/spike-probability")
def spike_probability(request: Request, body: SpikeRequest | None = None) -> SpikeResponse:
    """ """
    # currently a stub
    if body:
        pass

    return SpikeResponse(
        timestamp=datetime.now(UTC),
        probability=0.05,
        threshold_MW=48000.0,
        model=request.app.state.models["spike"],
    )


@app.post("/anomaly-score")
def anomaly_score(request: Request, body: AnomalyRequest | None = None) -> AnomalyResponse:
    """ """
    # currently a stub
    if body:
        pass

    return AnomalyResponse(
        anomaly_score=0.0,
        residual_zscore=0.0,
        is_anomaly=False,
        top_contributing_features=[],
        model=request.app.state.models["anomaly"],
    )
