#!/usr/bin/env python3
"""Measures the total runtime for executing async_comprehension four times in parallel."""

import asyncio
import time
from async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather.
    Returns the total runtime.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
