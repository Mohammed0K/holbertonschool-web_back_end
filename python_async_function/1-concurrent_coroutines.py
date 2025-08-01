#!/usr/bin/env python3
"""
Module for concurrent coroutine execution.
Runs wait_random multiple times concurrently and returns a sorted list of delays.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs wait_random n times with max_delay, returning list of all delays in ascending order.
    Args:
        n (int): Number of times to run wait_random.
        max_delay (int): Maximum delay value for wait_random.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
