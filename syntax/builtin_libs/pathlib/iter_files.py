from pathlib import Path

folder_path = Path("your_folder_path_here")  # 替换为你想要遍历的文件夹路径

# 遍历文件夹，排除子文件夹，只获取文件
for file_path in folder_path.iterdir():
    if file_path.is_file():  # 判断是否为文件
        print(file_path.name)  # 处理文件，如读取内容
