def parameter_modifier(func):
    def wrapper(name, *args, **kwargs):
        modified_name = 'Alice'  # 修改参数为 'Alice'
        return func(modified_name, *args, **kwargs)

    return wrapper


@parameter_modifier
def greet(name, other):
    print(f"Hello, {name}!")
    print(other)


greet('Bob', 'John')
# 输出: Hello, Alice!
