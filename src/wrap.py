from typing import Callable

def duo_wrapper(func: Callable):
    def inner_func():
        print("Antes my_func")
        func()
        print("Depois my_func")

    return inner_func

def wrapper(func: Callable):
    def inner_func():
        print("Antes my_func")
        func()
        print("Depois my_func")

    return inner_func

@wrapper
@duo_wrapper
def my_func():
    print("my_func")

my_func()