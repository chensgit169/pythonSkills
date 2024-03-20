import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# 插入一些示例任务数据
cursor.execute("INSERT INTO tasks (task_name, status, priority, finish_time) VALUES (?, ?, ?, ?)",
               ("完成项目报告", "未完成", 2, "2023-08-31 15:00:00"))
cursor.execute("INSERT INTO tasks (task_name, status, priority, finish_time) VALUES (?, ?, ?, ?)",
               ("准备会议材料", "已完成", 1, "2023-09-05 10:30:00"))
cursor.execute("INSERT INTO tasks (task_name, status, priority, finish_time) VALUES (?, ?, ?, ?)",
               ("清理办公室", "未完成", 3, "2023-09-10 14:45:00"))

conn.commit()
conn.close()

print("任务数据已成功存储到数据库中。")
