#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n
    times with the specified max_delay.

    Parameters:
    - n (int): Number of times to spawn wait_random.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - List[float]: List of delays in ascending order.
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
