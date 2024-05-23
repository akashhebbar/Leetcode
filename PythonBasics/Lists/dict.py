# import copy
#
# sample_dict = {"name": "Akash", "age": 20}
#
# sample_dict_2 = copy.deepcopy(sample_dict)
#
# sample_dict_2["name"] = "bhavya"
#
# print("Sample_dict", sample_dict)
# print("sample_dict_2", sample_dict_2)
#
# print(sample_dict_2.get("addess", "Not avilable"))
#
# ans = dict(sorted(sample_dict.items(), reverse=True))
#
# print(ans)
#
# dict1 = {"name": "akash"}
# dict2 = {"age": 20}
#
# res = {**dict1, **dict2}
# print(res)
#
test_dict = {'Gfg': {'a': [1, 3], 'b': [3, 6], 'c': [6, 7, 8]},
             'Best': {'a': [7, 9], 'b': [5, 3, 2], 'd': [0, 1, 0]}}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Swapping Hierarchy in Nested Dictionaries
# Using loop + items()
res = dict()
# for key, val in test_dict.items():
#     for key_in, val_in in val.items():
#         if key_in not in res:
#             temp = dict()
#         else:
#             temp = res[key_in]
#         temp[key] = val_in
#         res[key_in] = temp


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dt = {}
for k, v in zip(keys, values):
    dt[k] = v

print(dt)

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


def getkey(sampleDict, target):
    for key, values in sampleDict.items():
        if key == target:
            print(values)
        elif isinstance(values, dict):
            getkey(values, target)


getkey(sampleDict, 'history')
