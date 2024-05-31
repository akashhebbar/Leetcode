# dec to memorize function

# dec function
def memorize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


@memorize
def getAge(age):
    if age < 18:
        return "Under 18 years"
    else:
        return "18+ years"


ans = getAge(18)
print(ans)
ans1 = getAge(18)
print(ans1)
