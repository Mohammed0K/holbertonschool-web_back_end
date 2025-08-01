#!/usr/bin/env python3
"""Collects a list of random numbers using async comprehensions."""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers asynchronously from async_generator
    and returns them in a list.
    """
    return [value async for value in async_generator()]
