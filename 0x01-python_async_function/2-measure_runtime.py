#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as arguments
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): The number of random delays.
        max_delay (int): The maximum delay value.

    Returns:
        float: The average time of execution.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
