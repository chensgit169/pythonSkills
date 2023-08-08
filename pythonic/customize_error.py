# customize_error.py

# 按类继承的方式自定义异常
class CustomValueError(ValueError):
    def __init__(self, message, invalid_value):
        # 保证异常链的连接以便追踪和调试
        super().__init__(message)

        # 存储错误信息
        self.invalid_value = invalid_value


# 函数调用
def sqrt(num):
    if num < 0:
        raise CustomValueError("Invalid input: The number must be non-negative.", num)
    return num ** 0.5


# 异常捕获
try:
    result = sqrt(-4)
except CustomValueError as e:  # except后最好specify异常类型
    print("Error:", e)
    print("Invalid value:", e.invalid_value)
