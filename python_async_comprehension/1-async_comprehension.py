#!/usr/bin/env python3
"""Async comprehensions"""
from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing over async_generator"""
    return [i async for i in async_generator()]
