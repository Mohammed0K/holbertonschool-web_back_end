#!/usr/bin/env python3
"""Coroutine async_comprehension using async comprehension."""

from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Collect and return 10 random numbers asynchronously."""
    return [num async for num in async_generator()]
