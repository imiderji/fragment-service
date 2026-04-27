from __future__ import annotations

from dishka import AsyncContainer, Provider, Scope, make_async_container, provide

from fragment_service.infrastructure.config import AppConfig, load_config


class AppProvider(Provider):
    def __init__(self, config: AppConfig) -> None:
        super().__init__(scope=Scope.APP)
        self._config = config

    @provide(scope=Scope.APP)
    def provide_config(self) -> AppConfig:
        return self._config


def create_container(config: AppConfig | None = None) -> AsyncContainer:
    resolved_config = config or load_config()
    return make_async_container(AppProvider(resolved_config))
