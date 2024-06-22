# Create a simple decorator function
# except function as input
def decorator_function(func):
    # create wrapper arround it
    def warapper(*args, **kwargs):
        print("My Details ***********************")
        print("Function Details", func.__name__)
        items = list(args)
        items[0] = "Akash Hebbar"

        func(*items, **kwargs)
        print("End ****************************")
        return func

    return warapper


@decorator_function
def get_my_details(name, age, sex):
    print("My name is : ", name)
    print("My age is :", age)
    print("My sex is :", sex)


get_my_details("Akash", 20, "Male")
