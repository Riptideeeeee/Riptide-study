import pandas as pd

# 1. 定义一个字典
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# 2. 用 pd.DataFrame() 把它变成表格
df = pd.DataFrame(data)

# 3. 打印这个表格看看
print(df)