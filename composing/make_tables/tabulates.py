from tabulate import tabulate

headers = ["Name", "Age", "Gender"]
data = [
    ["John", 28, "Male"],
    ["Alice", 23, "Female"],
    ["Bob", 32, "Male"]
]

table = tabulate(data, headers=headers, tablefmt="pipe")

print(table)
with open("table.md", "w") as f:
    f.write(table)

headers = ["Name", "John", "Alice", "Bob"]
data = [
    ["Age", 28, 23, 32],
    ["Gender", "Male", "Female", "Male"]
]

# 转置表格
data_transposed = list(zip(*data))

# 格式化输出
table = tabulate(data_transposed, headers=headers, tablefmt="plain")

# 交换行和列
# table = "\n".join("| {:<10} | {} |".format(col, " | ".join(str(cell) for cell in row))
#                   for col, row in zip(headers, data_transposed))

print(table)
