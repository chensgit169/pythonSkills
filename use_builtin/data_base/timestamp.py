from datetime import datetime

# 将当前时间格式化为 ISO 8601 时间戳格式
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("当前时间（ISO 8601 格式）：", current_time)

# 解析 ISO 8601 时间戳为 datetime 对象
timestamp_str = "2023-08-31 15:00:00"
timestamp_datetime = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
print("解析后的时间（datetime 对象）：", timestamp_datetime)
