#!/usr/bin/env python3

""" concurrent_coroutines """

import asyncio
from typing import List
import random

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delay = []
    for i in range(n):
        delay.append(await wait_random())
    return delay
