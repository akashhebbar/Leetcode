# def log_function_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log_function_call
# def greet(name):
#     return "hiii"
#
#
# @log_function_call
# def add(a, b):
#     return a + b
#
#
# print(greet("Alice"))
# print(add(2, 3))


def log_dec(func):
    def inner(*args, **kwrgs):
        print("function name:", func.__name__)
        func()

    return inner


@log_dec
def myname():
    print("Akash")


myname()
