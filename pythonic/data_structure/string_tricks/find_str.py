from pprint import pprint
import itertools


expression = '(not A and B and C and not D and not E) or (A and not B and not C and not D and not E) or (not A and D and E)'
# for A, B, C, D, E in itertools.product([False, True], repeat=5):
#     print(eval(expression))

print(expression.replace('or', 'ha!'))

minterms = expression.split(' or ')
minterms = [_[1:-1].split(' and ') for _ in minterms]
pprint(minterms)


value_dict = {'A': True, 'B': False}
not_dict = {'not ' + _: not value_dict[_] for _ in value_dict}
value_dict = {**value_dict, **not_dict}
pprint(value_dict)

print()
