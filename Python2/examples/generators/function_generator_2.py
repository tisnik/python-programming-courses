def infinite_generator():
    n = 0
    while True:
        yield n
        n += 1


for i in infinite_generator():
    print(i)
    if i >= 10:
        break
