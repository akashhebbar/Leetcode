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

sample_list = [10, 20, 10, 3, 4, 1, 40, 50]
sample_list.sort(key=lambda x: -x)
print("sorted", sample_list)
