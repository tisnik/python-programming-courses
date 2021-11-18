def function_caller(function):

    def inner_function():
        print("Calling function...")
        function()
        print("...done")

    return inner_function


@function_caller
def hello():
    print("Hello!")


hello()
