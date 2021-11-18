class generator():

    def __init__(self, max_n):
        self.max_n = max_n
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max_n:
            current, self.n = self.n, self.n+1
            return current
        raise StopIteration()


for i in generator(10000):
    print(i)
    if i >= 10:
        break
