#!/usr/bin/env python3

"""
asynchronous coroutine that takes in an integer argument
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for a random delay between 0 and max_delay
    Args:
        n (int)
        max_delay (int)
    Return:
        (float)
    """
    values = await asyncio.gather(*[task_wait_random(max_delay)
                                    for _ in range(n)])
    return sorted(values)
