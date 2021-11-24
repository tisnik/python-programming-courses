from multiprocessing import Process


def worker(name):
    print("hello", name)


p = Process(target=worker, args=("foo",))
p.start()
p.join()
