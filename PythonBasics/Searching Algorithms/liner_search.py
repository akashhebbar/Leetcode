# code for simple liner search algorithm
class LinerSearch:
    def __init__(self, items):
        self.items = items

    def liner_search(self, key) -> bool:
        if len(self.items) == 0:
            return False
        for i in self.items:
            if i == key:
                # found
                return True

        # not found
        return False


obj = LinerSearch([10, 20, 4, 0, 11, 33, 5, 13, -3, -10, 39, 459])
result = obj.liner_search(500)

print("Search :", result)
