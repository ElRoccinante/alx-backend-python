#!/usr/bin/env python3
"""This module contains the function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for wait_random
    function with the given max_delay.

    Parameters:
    - max_delay (int): The maximum delay in seconds.

    Returns:
    - asyncio.Task: An asyncio task.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
