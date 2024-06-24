from typing import List


class BinarySearch:
    def __init__(self, items: List[int]):
        self.items = sorted(items)  # Ensure the list is sorted

    def binary_search(self, key: int) -> int:
        low = 0
        high = len(self.items) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.items[mid] == key:
                return mid  # Return the index of the found item
            elif self.items[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1  # Return -1 if the item is not found


obj = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9])

ans = obj.binary_search(2)
print("Result-:", ans)
