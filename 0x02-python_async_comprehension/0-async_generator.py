#!/usr/bin/env python3
""" Async Generator """
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine called async_generator that takes no arguments
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
