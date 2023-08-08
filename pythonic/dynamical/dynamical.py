# codes = "print('hi!')"
# eval(codes)
# assign_values_command = "a=1"
# exec(assign_values_command)
# print(f'a={a}')


def func_1():
    print(1)


def func_2():
    print(2)


command_dict = {'func1': func_1, 'func2': func_2}
key = 'func1'
func = command_dict[key]
func()
