def dec_func(func):
    def wrapper(*args, **kwargs):
        print("start")

        # Convert args to a list to allow modification
        args = list(args)

        # Print each positional argument
        for i, arg in enumerate(args):
            print(f"arg {i}: {arg}")

        # Add an element to the list (assuming the list is the last argument)
        if len(args) > 2 and isinstance(args[2], list):
            args[2].append(30)  # Adding element 30 to the list

        # Print each keyword argument
        for key, value in kwargs.items():
            print(f"{key}: {value}")

        # Convert args back to tuple for passing to the function
        result = func(*tuple(args), **kwargs)
        print("end")
        return result

    return wrapper


@dec_func
def getName(name, age, lst):
    print("My name is Akash", name)
    print("List:", lst)


lst = [10, 20]
getName("test", 19, lst)
