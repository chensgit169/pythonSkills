from typing import Mapping


def print_values(data: Mapping[str, int]):
    for key, value in data.items():
        print(f"{key}: {value}")


my_dict = {"apple": 2, "orange": 3, "banana": 1}
print_values(my_dict)
