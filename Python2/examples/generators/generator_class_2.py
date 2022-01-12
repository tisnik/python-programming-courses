class infinite_generator:
    def __init__(self):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        current, self.n = self.n, self.n + 1
        return current


for i in infinite_generator():
    print(i)
    if i >= 10:
        break
