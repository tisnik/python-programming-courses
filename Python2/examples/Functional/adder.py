def calculate(what, x, y):
    return what(x, y)


def add(x, y):
    return x + y


def get_function(selector):
    if selector == "add":
        return add
    return None


adder = get_function("add")
result = calculate(adder, 10, 20)

print(result)
