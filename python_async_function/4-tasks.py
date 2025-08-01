#!/usr/bin/env python3
"""
Module for running multiple task_wait_random concurrently.
Returns a list of delays in ascending order by completion time.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with max_delay.
    Returns: List of delays in ascending order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
