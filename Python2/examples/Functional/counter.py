def counter():
    cnt = 0

    def impl():
        nonlocal cnt
        cnt += 1
        return cnt

    return impl


c1 = counter()
c2 = counter()

print(c1())
print(c1())
print(c1())

print(c2())

print(c1())
print(c1())
print(c1())

print(c2())

