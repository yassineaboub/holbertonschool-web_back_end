#!/usr/bin/env python3
"""  Measure the runtime """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return (total_time / n)
