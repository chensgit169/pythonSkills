

class MyList:
    def __init__(self, a_list: list):
        self.a_list = a_list

    def __getitem__(self, item):
        return self.a_list[item]


my_list = MyList([1, 2, 3])
print(my_list[0])
