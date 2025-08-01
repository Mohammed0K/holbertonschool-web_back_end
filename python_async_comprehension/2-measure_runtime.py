#!/usr/bin/env python3
"""Measures the runtime of running async_comprehension in parallel."""

import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension concurrently four times using asyncio.gather,
    and returns the total elapsed time.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
