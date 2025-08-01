#!/usr/bin/env python3
"""
Module for running multiple task_wait_random concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Returns a list of all delays (float values) in ascending order of completion.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
