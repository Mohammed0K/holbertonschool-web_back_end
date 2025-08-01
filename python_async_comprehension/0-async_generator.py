#!/usr/bin/env python3
"""Defines an asynchronous generator that yields random floats."""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously yields 10 random floating-point numbers between 0 and 10,
    waiting 1 second between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
