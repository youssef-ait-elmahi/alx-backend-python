#!/usr/bin/env python3
""" Async Comprehensions """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random numbers
    using an async comprehending over async_generator.

    Returns:
        List[float]: A list of 10 random numbers.
    """
    return [i async for i in async_generator()]
