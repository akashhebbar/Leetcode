s = "paper"
t = "title"
smap = []
tmap = []
for i in s:
    smap.append(s.index(i))
for i in t:
    tmap.append(t.index(i))

if smap == tmap:
    print("true")
else:
    print("false")
