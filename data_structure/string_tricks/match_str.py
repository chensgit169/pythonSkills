import re

str_list = ['not A', 'B', 'C', 'not D', 'not E']
for _ in str_list:
    if not re.match('n', _):
        print(_)
