#!/usr/bin/env python3
"""Module for asynchronous generator.
Yields 10 random floats between 0 and 10, waiting 1s each time.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously yields 10 random floats between 0 and 10, waiting 1s each time."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
