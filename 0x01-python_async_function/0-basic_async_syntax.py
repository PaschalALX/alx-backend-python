#!/usr/bin/env python3

"""
asynchronous coroutine that takes in an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay
    Args:
        max_delay (int)
    Return:
        (float)
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
