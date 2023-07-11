#!/usr/bin/env python3

"""
asynchronous coroutine that takes in an integer argument
"""
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Wait for a random delay between 0 and max_delay
    Args:
        n (int)
        max_delay (int)
    Return:
        (float)
    """
    delays = []
    for x in range(n):
        delays.append(await wait_random(max_delay))
    return delays
