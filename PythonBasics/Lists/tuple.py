# nested tuple
state_tuple = (("Goa", "Orange"), "Kerala", ("Delhi", "DL"), "Karnataka", ("Gujarat", "GJ", 129), "Tamilnadu")
test = ("ate",)
# accessing nested tuple
print(state_tuple[0][0])
print(state_tuple[2][1])
print(state_tuple[2])
print(state_tuple[3])
print(state_tuple[4][2])

print(type(test))

my_list = [10, 20, 30, 40, 50, 60]

print(my_list.count("10"))
