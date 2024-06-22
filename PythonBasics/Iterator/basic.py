# create basic iterator to get understanding

# create list
mylist = [10, 20, 30, 40, 5060, 60, 70, 60]

# iterator uses 2 methods iter and next method

# create iterator object

myiter = iter(mylist)


# get all elements by calling next method

def get_one_element_at_time():
    return next(myiter)


print(get_one_element_at_time())
print(get_one_element_at_time())
