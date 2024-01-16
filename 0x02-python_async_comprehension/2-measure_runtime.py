#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous coroutine that measures the total runtime
    of executing async_comprehension four times in parallel.

    Returns:
        float: Total runtime.
    """
    start_time = time.time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
