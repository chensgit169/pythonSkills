from pathlib import Path

file_old_name = "test_ol.txt"
with open(file_old_name, "w") as f:
    f.write("Hello, world!")

# 原始文件路径
file_path = Path(file_old_name)

# 替换文件名中的某一部分
new_file_path = file_path.with_name(file_path.name.replace("old", "new"))

# 重命名文件
file_path.rename(new_file_path)
