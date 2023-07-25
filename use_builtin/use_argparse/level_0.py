import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='一个接受两个整数作为参数的示例程序')

# 添加位置参数
parser.add_argument('num1', type=int, help='第一个整数')
parser.add_argument('num2', type=int, help='第二个整数')

# 解析命令行参数
args = parser.parse_args()

# 打印解析的参数值
print('第一个整数:', args.num1)
print('第二个整数:', args.num2)
