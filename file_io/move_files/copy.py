import shutil


def copy_directory(source, destination):
    # 复制源目录到目标目录
    shutil.copytree(source, destination)


# 指定源目录和目标目录的路径
source_directory = 'D:\\'
destination_directory = 'C:\\Download\\ChinesePainting'

# 调用函数复制目录
copy_directory(source_directory, destination_directory)
