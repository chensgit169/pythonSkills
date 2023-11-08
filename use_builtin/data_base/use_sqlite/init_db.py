import sqlite3

# 连接到 SQLite 数据库（如果不存在，则会创建一个新的数据库文件）
conn = sqlite3.connect("tasks.db")

# 创建一个游标对象，用于执行 SQL 查询
cursor = conn.cursor()

# 创建一个名为 "tasks" 的表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        task_name TEXT,
        status TEXT,
        priority INTEGER,
        finish_time TIMESTAMP
    )
''')

# 提交更改并关闭连接
conn.commit()
conn.close()
