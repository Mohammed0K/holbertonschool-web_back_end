#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """yield a random number from 0 to 10, 10 times with 1 sec delay"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
