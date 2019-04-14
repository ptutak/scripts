#!/usr/bin/python3
import asyncio
from time import sleep
from time import perf_counter


async def worker(n):
    await asyncio.sleep(n)


loop = asyncio.get_event_loop()
t_start = perf_counter()
loop.run_until_complete(asyncio.gather(*[worker(i) for i in range(5)]))
t_end = perf_counter()
loop.close()

print(t_end - t_start)
