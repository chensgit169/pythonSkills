import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute('SELECT * FROM tasks')

# # 指定要检索的 task_name
# target_task_name = "没有完成项目报告"
#
# # 执行 SQL 查询以检索特定 task_name 的任务数据
# cursor.execute("SELECT * FROM tasks WHERE task_name=?", (target_task_name,))

# 获取匹配的任务数据
matching_tasks = cursor.fetchall()

# 打印匹配的任务数据
if matching_tasks:
    for task in matching_tasks:
        task_id, task_name, status, priority, finish_time = task
        print(f"Task ID: {task_id}")
        print(f"Task Name: {task_name}")
        print(f"Status: {status}")
        print(f"Priority: {priority}")
        print(f"Finish Time: {finish_time}")
        print("------------------------")
else:
    print(f"No tasks found")

# 关闭连接
conn.close()
