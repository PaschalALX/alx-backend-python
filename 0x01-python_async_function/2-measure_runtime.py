#!/usr/bin/env python3

"""
measure_time
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure time
    Args:
        n (int)
        max_delay (int)
    Return:
        (float)
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start
    return end / n
