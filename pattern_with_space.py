# #    *
# #   ***
# # *******
#
row = 5
for i in range(row):
    for j in range(row - i -1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    for l in range(row - i - 1):
        print(" ", end="")
    print(" ")
# row = 4  # Adjust row as needed
# for i in range(row):
#     for j in range(row - i - 1):
#         print(" ", end="")
#     for k in range(2 * i + 1):
#         print("*", end="")
#     for l in range(row - i - 1):
#         print(" ", end="")
#     print("")
