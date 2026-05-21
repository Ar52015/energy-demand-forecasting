from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from edf.utils.logger import setup_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    setup_logging()
    app.state.models = {
        "forecast": "stub",
        "spike": "stub",
        "anamoly": "stub",
    }
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
