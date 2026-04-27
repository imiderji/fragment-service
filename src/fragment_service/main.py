from __future__ import annotations

import asyncio

from fragment_service.infrastructure.config import AppConfig
from fragment_service.infrastructure.di import create_container


async def run() -> None:
    container = create_container()
    try:
        config = await container.get(AppConfig)
        print(
            f"{config.service_name} started "
            f"(env={config.environment}, debug={config.debug})"
        )
    finally:
        await container.close()


def main() -> None:
    asyncio.run(run())
