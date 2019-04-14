#!/usr/bin/python3
import threading
from time import sleep
from time import perf_counter


def worker(n):
    sleep(n)


t_start = perf_counter()

for i in range(5):
    worker(i)

t_end = perf_counter()

print(t_end - t_start)
