#!/usr/bin/env python3
"""async"""
from typing import List
wait = __import__("0-basic_async_syntax").wait_random


async def wait_n(a: int, max_delay: int) -> List[float]:
    """an async"""
    delays = []
    for _ in range(a):
        delays.append(await wait(max_delay))
    return sorted(delays)
