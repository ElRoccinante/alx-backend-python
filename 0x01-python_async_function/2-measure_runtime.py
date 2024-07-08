#!/usr/bin/env python3
"""This module contains the function"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for
    wait_n(n, max_delay)

    Parameters:
    - n (int): Number of times to spawn wait_random in wait_n.
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - float: return total_time / n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
