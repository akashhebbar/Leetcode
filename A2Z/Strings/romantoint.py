dt={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s = "MCMXCIV"
ans=0
for i in range(1,len(s)):

    if dt[s[i-1]] < dt[s[i]]:
        ans+=dt[s[i-1]+s[i]]
    else:
        ans+=dt[s[i]]

print(ans)




