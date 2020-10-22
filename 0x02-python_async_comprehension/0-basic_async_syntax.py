#!/usr/bin/env python3
""" basics of async """
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """ wait for a random delay between
        0 and max_delay and returns it.
    """
    n = random.uniform(0, max_delay)
    await asyncio.sleep(n)
    return n
