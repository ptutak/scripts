#!/usr/bin/python3
import threading
from time import sleep
from time import perf_counter


def worker(n):
    sleep(n)


threads = []

t_start = perf_counter()

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

t_end = perf_counter()

print(t_end - t_start)
