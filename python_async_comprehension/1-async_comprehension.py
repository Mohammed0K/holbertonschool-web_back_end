#!/usr/bin/env python3
"""Coroutine async_comprehension using async comprehension."""

from typing import List
from importlib import import_module

async_generator = import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers asynchronously."""
    return [number async for number in async_generator()]
