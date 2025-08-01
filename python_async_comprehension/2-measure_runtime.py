#!/usr/bin/env python3
"""Coroutine measure_runtime to measure execution time of parallel tasks."""

import asyncio
import time
from typing import float
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measure and return runtime of running 4 async_comprehensions in parallel."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
