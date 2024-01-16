#!/usr/bin/env Python3
"""First Async and Await corroutine"""


from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """First concurrent module"""
    i = uniform(0, max_delay)
    await sleep(i)

    return i
