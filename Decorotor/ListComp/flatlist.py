# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# ans = [item for single_list in nested_list for item in single_list]
#
# print(ans)


# items = [10, 2, 3, 4, 5, 44, 53, 5, 62, 334]
#
# ans = [i for i in items if i % 2 == 0 and i > 50]
#
# print(ans)


items = [10, 2, 3, 4, 5, 44, 53, 5, 62, 334]

ans = [i if i % 2 == 0 else -1 for i in items]

print(ans)
