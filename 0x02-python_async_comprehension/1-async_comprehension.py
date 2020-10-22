#!/usr/bin/env python3
""" Async Comprehensions """
from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine collect 10 random numbers using an async
    comprehensing, return the 10 random numbers.
    """
    res = [i async for i in async_generator()]
    return res
