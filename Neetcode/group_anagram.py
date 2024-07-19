strs = ["act", "pots", "tops", "cat", "stop", "hat"]


# def group_anagrams(strs) -> list:
#     output = []
#
#     for i in range(len(strs)):
#         temp_list = []
#         for j in range(i + 1, len(strs)):
#             if sorted(strs[i]) == sorted(strs[j]) and strs[j] != "visited":
#                 temp_list.append(strs[j])
#                 strs[j] = "visited"
#         if strs[i] != "visited":
#             temp_list.append(strs[i])
#             output.append(temp_list)
#
#     return output
#
#
# result = group_anagrams(strs)
# print(result)

def group_anagrams_dict(strs):
    anagrams_dict = {}
    for str in strs:
        key = ''.join(sorted(str))
        print(key)
        print(type(key))
        if key in anagrams_dict:
            anagrams_dict[key].append(str)
        else:
            anagrams_dict[key] = [str]

    return list(anagrams_dict.values())


result = group_anagrams_dict(strs)

print(result)
