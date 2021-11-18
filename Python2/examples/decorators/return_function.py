def function_caller(function):

    def inner_function():
        print("Calling function...")
        function()
        print("...done")

    return inner_function


def hello():
    print("Hello!")


f = function_caller(hello)
f()
