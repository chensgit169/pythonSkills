from typing import Optional


def find_element(arr: Optional[list], target: int) -> Optional[int]:
    if arr is None:
        return None
    for index, value in enumerate(arr):
        if value == target:
            return index
    return None


my_list = [1, 2, 3, 4, 5]
result = find_element(my_list, 3)
print(result)  # 输出: 2

result = find_element(None, 3)
print(result)  # 输出: None
