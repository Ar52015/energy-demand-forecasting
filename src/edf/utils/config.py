from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ """

    model_config = SettingsConfigDict(env_prefix="EDF_")

    data_root: Path = Path("data")
    model_root: Path = Path("models")
    feature_pipeline_path: Path = Path("models/feature_pipeline_path")
    served_models: dict[str, Path] = {
        "forecaster": Path("models/forecaster.joblib"),
        "spike": Path("models/spike.joblib"),
        "anamoly": Path("models/anamoly.joblib"),
    }
    as_of_default: Literal["latest_in_store"] = "latest_in_store"


@lru_cache
def get_settings() -> Settings:
    return Settings()
