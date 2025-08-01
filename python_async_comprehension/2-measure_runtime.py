#!/usr/bin/env python3
"""Coroutine measure_runtime to measure runtime of async comprehensions."""

import asyncio
import time
from importlib import import_module

async_comprehension = import_module("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of running 4 async_comprehensions in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
