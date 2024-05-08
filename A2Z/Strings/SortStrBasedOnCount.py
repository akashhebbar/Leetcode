s = "Aabb"


def return_sorted_str(s: str) -> str:
    map = {}

    for i in s:
        map[i] = map.get(i, 0) + 1
    ans = sorted(map.values(), reverse=True)
    str = ""
    for i in ans:
        for key, val in map.items():
            if val == i:
                str += key * int(val)
                map.pop(key)
                break
    return str


ans = return_sorted_str(s)
print(ans)
