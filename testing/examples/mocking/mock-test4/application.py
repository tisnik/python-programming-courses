"""Implementace logiky aplikace, kterou budeme testovat."""


def function1():
    """První funkce, která volá funkci druhou."""
    print("function1 called")
    return function2()


def function2():
    """Druhá funkce, kterou v testech nahradíme mockem."""
    print("*" * 60)
    print("function2 called")
    print("*" * 60)
    return "function 2"
