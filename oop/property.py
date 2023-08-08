


class Tensor:
    def __init__(self, a: int):
        self.a = a

    def set_a(self, a):
        self.a = a

    @property
    def square(self):
        print('ha!')
        return self.a ** 2


if __name__ == '__main__':
    tensor = Tensor(2)
    print(tensor.square)
    print(tensor.square)
    tensor.set_a(3)
    print(tensor.square)