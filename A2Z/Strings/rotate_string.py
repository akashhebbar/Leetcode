s = "abcde"
goal = "cdeab"


def check_rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    combine = s + s
    if goal in combine:
        return True
    return False


ans = check_rotate_string(s, goal)
print("ans:", ans)
