from pathlib import Path

# 创建一个 Path 对象
path = Path('path/to/file_or_directory')

path2 = path / 'ha'
print(path2)
# 创建目录
# path.mkdir()
# # 递归创建目录（包含父目录）
# path.mkdir(parents=True)

# 删除目录
# path.rmdir()

# 递归删除目录及其内容
# import shutil
# shutil.rmtree(path)
for i in range(3):
    with open(path/f'text{i}.txt', 'w') as f:
        pass

for item in path.iterdir():
    print(item)
