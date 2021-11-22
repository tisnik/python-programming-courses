def calculate(what, x, y):
    return what(x, y)


def add(x, y):
    return x + y


result = calculate(add, 10, 20)

print(result)
