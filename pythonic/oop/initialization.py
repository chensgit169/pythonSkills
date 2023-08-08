

class Z2Tensor:
    def __init__(self, t_type: str):
        from numpy import ndarray
        self.type = t_type


class Z2Ising(Z2Tensor):
    def __init__(self, t_type: str, other: int):
        self.other = other
        self.type = 'not ndarray'
        Z2Tensor.__init__(self, t_type)


if __name__ == '__main__':
    ising = Z2Ising('ndarray', 1)
    print(ising.type)
    print(ising.other)
