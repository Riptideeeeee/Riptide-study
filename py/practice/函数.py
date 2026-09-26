# 全局变量（可以在任何地方访问）
name = "全局的小明"

def test():
    # 局部变量（只能在函数内部访问）
    age = 18
    print(f"函数内部：{name}")  # 可以访问全局变量
    print(f"函数内部：{age}")   # 可以访问局部变量

test()
print(name)  # 可以访问（全局）
# print(age)  # 报错！局部变量不能在函数外访问