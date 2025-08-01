#!/usr/bin/env python3
"""Module for async_comprehension coroutine to collect random numbers asynchronously."""

from typing import List
import random
from typing import List


async def async_generator():
    """Yield 10 random numbers between 0 and 10 asynchronously."""
    for _ in range(10):
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator,
    and returns them as a list.
    """
    return [i async for i in async_generator()]
