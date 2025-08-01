#!/usr/bin/env python3
"""Module to measure runtime for running async_comprehension in parallel."""
import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Measures total runtime for running 4 async_comprehension coroutines in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
