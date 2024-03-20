import tempfile


def write_temp_file(data):
    # 创建一个临时文件，模式为文本写入模式 ('w')，自动删除 (delete=True)
    with tempfile.NamedTemporaryFile(mode='w', delete=True) as temp_file:
        # 写入数据到临时文件
        temp_file.write(data)
        temp_file.flush()  # 刷新缓冲，确保数据被写入文件

        # 获取临时文件的路径，并返回
        return temp_file.name


# 测试示例
data_to_write = "Hello, this is a temporary file content!"
temp_file_path = write_temp_file(data_to_write)
print(f"Temporary file path: {temp_file_path}")  # ...\AppData\Local\Temp\tmpzcbpjt1c
