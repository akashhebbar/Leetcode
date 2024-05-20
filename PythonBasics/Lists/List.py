mylist = list()
mylist = [30, 40, 1, 30, "akash", "bhavya"]
mylist.append(20)

# ans=mylist[0:3]
# rev=mylist[0:-3]
# print('rev',rev)
# print(ans)
# print(mylist)

# str='+'.join( str(item) for  item in mylist)
# print('str',str)
print(mylist)

mylist.pop()
print(mylist)

newList = [0] * 10
print("newList", newList)

mylist.extend(newList)
mylist.insert(0, 100)
print(mylist)

sample_list = [10, 20, 10, 3, 4, 1, 40, 50, ["akash", "ram", "kumar"], {2, 4, 5, 6, 7, 8, 9}]


# sample_list.sort(key=lambda x: -x)
# print("sorted", sample_list)
# from itertools import chain
#
# test_list = list(chain.from_iterable(sample_list))
# print(test_list)

def flatten_list(input_list):
    for item in input_list:
        if isinstance(item, list):
            yield from flatten_list(item)
        elif isinstance(item, set):
            yield from item
        else:
            yield item


ans = list(flatten_list(sample_list))
print("ans", ans)
