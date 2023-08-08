from itertools import permutations


def permutations_demo():
    for _ in permutations('++--'):
        print(''.join(_))
