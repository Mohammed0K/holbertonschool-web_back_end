#!/usr/bin/env python3
"""
Module to measure runtime for executing wait_n.
"""
import time
import asyncio
from typing import Callable

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures average execution time for running wait_n(n, max_delay).
    Args:
        n (int): Number of tasks.
        max_delay (int): Maximum delay for wait_random.
    Returns:
        float: Average time per task.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
