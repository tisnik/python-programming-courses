def counter(start=0, step=1):
    cnt = start

    def impl():
        nonlocal cnt
        cnt += step
        return cnt

    return impl


c1 = counter(10, 1)
c2 = counter(0, 2)
c3 = counter(100, -10)

for i in range(10):
    print("c1", c1())

print()

for i in range(10):
    print("c2", c2())

print()

for i in range(10):
    print("c3", c3())
