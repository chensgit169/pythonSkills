# 从 Python 3.8 开始，typing_extensions 的一些功能被合并到了标准库的 typing 模块中

from typing import Annotated, Literal, Final, Protocol, runtime_checkable

# 使用 Annotated 增加类型注释的附加信息
Name = Annotated[str, 'Person name']


def greet(name: Name) -> str:
    return f"Hello, {name}!"


# 使用 Literal 限制变量的字面值
Gender = Literal['Male', 'Female']


def get_gender(gender: Gender) -> str:
    return gender


# 使用 Final 标记类成员为最终的
class MyClass:
    def __init__(self):
        self.value: Final[int] = 42


# 使用 Protocol 定义协议
@runtime_checkable
class MyProtocol(Protocol):
    def do_something(self) -> None:
        ...


# 使用 runtime_checkable 运行时类型检查
@runtime_checkable
class MyRuntimeCheckableProtocol(Protocol):
    def do_something(self) -> None:
        ...
