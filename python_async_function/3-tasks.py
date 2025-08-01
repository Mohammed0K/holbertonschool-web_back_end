#!/usr/bin/env python3
"""
Module for creating asyncio tasks from wait_random.
"""
import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for wait_random with max_delay.
    Args:
        max_delay (int): Maximum delay for wait_random.
    Returns:
        asyncio.Task: The scheduled task.
    """
    return asyncio.create_task(wait_random(max_delay))
