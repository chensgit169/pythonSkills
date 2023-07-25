import argparse

# 创建ArgumentParser对象
parser = argparse.ArgumentParser(description='一个处理命令行选项的示例程序')

# 添加位置参数
parser.add_argument('filename', help='输入文件名')

# 添加可选参数
parser.add_argument('-o', '--output', help='输出文件名')
parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')

# 解析命令行参数
args = parser.parse_args()

# 打印解析的参数值
print('输入文件名:', args.filename)
print('输出文件名:', args.output)
print('是否显示详细信息:', args.verbose)
