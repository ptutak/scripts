#!/usr/bin/python3
import asyncio
from time import sleep
from time import perf_counter


async def worker(n):
    await asyncio.sleep(n)


async def main():
    for i in range(5):
        await worker(i)


loop = asyncio.get_event_loop()
t_start = perf_counter()
loop.run_until_complete(main())
t_end = perf_counter()

print(t_end - t_start)
