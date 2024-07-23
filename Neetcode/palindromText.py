s = "Was it a car or a at I saw?"


def check_palindrome(text: str) -> bool:
    result = [i.lower() for i in text if i.isalpha()]
    temp_str = ''.join(result)
    i = 0
    j = len(temp_str) - 1
    while i < j:
        if temp_str[i] != temp_str[j]:
            return False
        i += 1
        j -= 1
    return True


res = check_palindrome(s)
print(res)
