#!/usr/bin/env Python3
"""First Async and Await corroutine"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """A cycle with an async function"""
    delay = []
    for i in range(n):
        delay.append(await wait_random(max_delay))
    return sorted(delay)
