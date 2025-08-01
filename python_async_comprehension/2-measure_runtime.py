#!/usr/bin/env python3
"""Module for measuring runtime of running async_comprehension four times in parallel."""

import asyncio
import importlib
import time
from typing import Callable

# Import the module with a numeric filename
async_comprehension_module = importlib.import_module('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension

async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension four times in parallel.
    Returns the elapsed time in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start