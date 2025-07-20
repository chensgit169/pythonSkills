import os

# 设置要操作的文件夹路径
folder_path = r"C:\Users\weich\Downloads"

# 要替换的字段
old_text = " (Z-Library)"
new_text = ""

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf") and old_text in filename:
        new_filename = filename.replace(old_text, new_text)
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # 重命名文件
        os.rename(old_file_path, new_file_path)
        print(f"已重命名: {filename} -> {new_filename}")
