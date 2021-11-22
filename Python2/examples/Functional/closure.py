def increment_by(n):

    def add(x):
        return x + n

    return add


i1 = increment_by(2)
print(i1(1))
print(i1(10))

i2 = increment_by(100)
print(i2(1))
print(i2(10))
