st="A man, a plan, a canal: Panam"

def check_painf(st):

    temp=''
    for s in st:
        if s.isalpha():
            temp+=s.lower()

    i=0
    j=len(temp)-1

    while i<j:
        if temp[i]!=temp[j]:
            return "not palindrome"

        else:
            i+=1
            j-=1

    return "palin"

ans=check_painf(st)
print(ans)


