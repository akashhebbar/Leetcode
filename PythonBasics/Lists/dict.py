import copy

sample_dict = {"name": "Akash", "age": 20}

sample_dict_2 = copy.deepcopy(sample_dict)

sample_dict_2["name"] = "bhavya"

print("Sample_dict", sample_dict)
print("sample_dict_2", sample_dict_2)

print(sample_dict_2.get("addess", "Not avilable"))
