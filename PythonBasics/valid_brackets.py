s = "([])"


def check_valid_brackets(st: str) -> bool:
    maping = {
        ")": "(", "}": "{", "]": "["
    }
    stack = []
    for char in st:
        if char in ["[", "{", "("]:
            stack.append(char)
        elif len(stack) != 0 and stack.pop() != maping.get(char):
            return False

    if len(stack) == 0:
        return True


ans = check_valid_brackets(s)
print(ans)
