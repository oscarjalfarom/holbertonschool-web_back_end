#!/usr/bin/env python3

"""
Async comprehension
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    start = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    total_time = time.perf_counter() - start
    return total_time
