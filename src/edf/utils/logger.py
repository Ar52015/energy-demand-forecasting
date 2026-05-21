import json
import logging
import sys

from edf.utils.config import get_settings


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        """"""
        payload = {
            "timestamp": self.formatTime(record),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        return json.dumps(payload)


def setup_logging() -> None:
    """ """

    settings = get_settings()
    handler = logging.StreamHandler(sys.stdout)
    formatter: logging.Formatter
    if settings.log_format == "json":
        formatter = JsonFormatter()
    else:
        formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s - %(name)s : %(message)s")
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[handler])
