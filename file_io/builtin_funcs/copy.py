import os
import shutil


def copy_directory(source, destination):
    # copy the directory from source to destination
    shutil.copytree(source, destination)


def demo():
    # 指定源目录和目标目录的路径
    source_directory = os.getcwd()
    destination_directory = os.path.join(os.getcwd(), 'backup')

    # 调用函数复制目录
    copy_directory(source_directory, destination_directory)


if __name__ == '__main__':
    demo()