#!/usr/bin/env python3
"""
Module for running multiple task_wait_random concurrently.
Returns a list of delays in ascending order.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs task_wait_random n times and returns list of delays in ascending order.
    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
