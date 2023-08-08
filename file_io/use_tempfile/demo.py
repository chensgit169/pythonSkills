import tempfile

# 创建一个临时文件
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Hello, this is a temporary file.")
    print("Temporary file:", temp_file.name)

# # 创建一个临时目录
# with tempfile.TemporaryDirectory() as temp_dir:
#     print("Temporary directory:", temp_dir)
#     temp_file_path = temp_dir + "/temp_file.txt"
#     with open(temp_file_path, "w") as temp_file:
#         temp_file.write("Hello, this is a temporary file in a temporary directory.")

with open(temp_file.name, 'r') as f:
    print(f.read())
