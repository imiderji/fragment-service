from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from os import getenv


def _read_bool(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True, slots=True)
class AppConfig:
    service_name: str
    environment: str
    debug: bool
    log_level: str

    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            service_name=getenv("FRAGMENT_SERVICE_NAME", "fragment-service"),
            environment=getenv("FRAGMENT_SERVICE_ENV", "local"),
            debug=_read_bool(getenv("FRAGMENT_SERVICE_DEBUG")),
            log_level=getenv("FRAGMENT_SERVICE_LOG_LEVEL", "INFO"),
        )


@lru_cache(maxsize=1)
def load_config() -> AppConfig:
    return AppConfig.from_env()
