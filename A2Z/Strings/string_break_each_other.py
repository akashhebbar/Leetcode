s1 = "abc"
s2 = "xya"
#sort both strings

st1 = sorted(s1)
st2 = sorted(s2)

counts1 = 0
counts2 = 0

for i in range(len(st1)):
    if st1[i] >= st2[i]:
        counts1 += 1

for i in range(len(st2)):
    if st2[i] >= st1[i]:
        counts2 += 1

if counts1 == len(st1) or counts2 == len(st2):
    print("true")
else:
    print("false")
