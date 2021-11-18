def generator(max_n):
    n = 0
    while n < max_n:
        yield n
        n += 1


for i in generator(10000):
    print(i)
    if i >= 10:
        break
