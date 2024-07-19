s = "rat"
t = "car"

scount = {}

for i in s:
    scount[i] = scount.get(i, 0) + 1

for t in t:
    if t not in scount or scount[t] == 0:
        print(False)

print(True)

