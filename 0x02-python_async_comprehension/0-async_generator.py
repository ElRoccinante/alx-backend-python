#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields
    random numbers between 0 and 10.
    Each yield is delayed by 1 second
    using asyncio.sleep.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
