#!/usr/bin/python3
import multiprocessing
from multiprocessing.managers import BaseManager, BaseProxy
from time import sleep
from time import perf_counter


class GeneratorProxy(BaseProxy):
    _exposed_ = ['__next__']

    def __iter__(self):
        return self

    def __next__(self):
        return self._callmethod('__next__')


class MyManager(BaseManager):
    pass


def my_gen(n):
    for i in range(n):
        yield i


MyManager.register('MyGen', my_gen, proxytype=GeneratorProxy)


class MyClass:
    def worker(self, n, gen):
        for _ in range(1000):
            try:
                x = next(gen)
            except StopIteration:
                break
        print('Process number: {}, value: {}'.format(n, x))



if __name__ == '__main__':
    manager = MyManager()
    manager.start()

    my_gen_exm = manager.MyGen(1000000)

    lock = multiprocessing.Lock()
    processes = []
    manager = multiprocessing.Manager()
    t_start = perf_counter()
    instance = MyClass()

    for i in range(100):
        p = multiprocessing.Process(target=instance.worker, args=(i, my_gen_exm))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    t_end = perf_counter()
    manager.shutdown()
    print(t_end - t_start)
