# Create a decorator factory function to accept additional arguments
def decorator_function(count):
    # Define the actual decorator function
    def actual_decorator(func):
        # Create the wrapper around the function
        def wrapper(*args, **kwargs):
            print("My Details ***********************")
            print("Function Details:", func.__name__)
            retry = 1
            # Custom logic using the count
            try:
                if len(args) > 0 and count <= 10:
                    raise Exception("Custom Exception")

                result = func(*args, **kwargs)
                print("End ****************************")
                return result
            except Exception as e:
                print("Exception occurred:", e)
                if retry < 2:
                    # Retry logic if count is less than 2
                    print("Retrying...", retry)
                    result = func(*args, **kwargs)
                    retry += 1
                    return result
                print("Exception Count:", count)

        return wrapper

    return actual_decorator


@decorator_function(count=10)
def get_my_details(name, age, sex):
    print("My name is:", name)
    print("My age is:", age)
    print("My sex is:", sex)


# Call the decorated function
get_my_details("Akash", 20, "Male")
