#!/usr/bin/env python3
""" using the random modul Write an asynchronous coroutine  """
import asyncio
from random import uniform
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
