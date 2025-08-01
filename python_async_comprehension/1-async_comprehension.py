#!/usr/bin/env python3
"""Module for async_comprehension coroutine to collect random numbers asynchronously."""

import importlib
from typing import List

# Import the module with a numeric filename
async_generator_module = importlib.import_module('0-async_generator')
async_generator = async_generator_module.async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator,
    and returns them as a list.
    """
    return [i async for i in async_generator()]