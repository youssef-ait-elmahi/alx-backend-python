#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that waits for n random delays
    and returns them in ascending order.

    Args:
        n (int): The number of random delays.
        max_delay (int): The maximum delay value.

    Returns:
        List[float]: A list of delay values in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for future in asyncio.as_completed(tasks):
        delay = await future
        delays.append(delay)
    return delays
