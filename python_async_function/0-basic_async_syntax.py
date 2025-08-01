#!/usr/bin/env python3
"""
Module for basic asynchronous syntax.
Defines a coroutine that waits for a random delay and returns it.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay (included).
    Args:
        max_delay (int): Maximum number of seconds to wait.
    Returns:
        float: The actual random delay waited.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
