import os


def print_directory_contents(path):
    # 遍历目录下的所有文件和文件夹
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            # 如果是文件夹，则递归调用函数打印其内容
            print_directory_contents(child_path)
        else:
            # 如果是文件，则打印文件名
            print(child_path)


# 指定要查看的目录路径
directory_path = 'D:\\'

# 调用函数查看目录下的所有文件夹和文件
print_directory_contents(directory_path)
