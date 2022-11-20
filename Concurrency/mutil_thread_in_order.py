# coding: utf-8
from threading import Thread, Lock


def execute(idx, acquirable, releasable):
    for i in range(10):
        acquirable.acquire()
        print("{} -> {}".format(idx, i))
        releasable.release()


def main():
    mutex1 = Lock()
    mutex2 = Lock()
    mutex3 = Lock()

    threads = [
        Thread(target=execute, args=[params[0], params[1], params[2]])
        for params in [
                ('A', mutex1, mutex2),
                ('B', mutex2, mutex3),
                ('C', mutex3, mutex1)
            ]
    ]
    mutex2.acquire()
    mutex3.acquire()

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


if __name__ == "__main__":
    main()
