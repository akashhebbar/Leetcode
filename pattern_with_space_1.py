# #   *****
#      ***
#       *
#
row = 9
for i in range(row):
    for j in range(i):
        print(" ", end="")
    for k in range(2*row-2*i-1):
        print("*", end="")
    for l in range(i):
        print(" ", end="")
    print(" ")
   # for k in range(2*row-(2*i-1)):