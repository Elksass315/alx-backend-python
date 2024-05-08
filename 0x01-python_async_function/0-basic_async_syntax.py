#!/usr/bin/env python3
import asyncio
import random

"""
    Write a coroutine called wait_random that takes in an integer max_delay and returns a random delay between 0 and max_delay. Use the random module.
    """
    
async def wait_random(max_delay = 10):
    """
        async func delay for random time
        max_delay: max delay time
        return: the time delayed
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay