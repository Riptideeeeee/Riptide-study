# 你的原版
# apple=0, banana=0, orange=0, grape=0

# 改进版
counts = [0, 0, 0, 0]  # 苹果,香蕉,橙子,葡萄
names = ["苹果", "香蕉", "橙子", "葡萄"]
prices = [5, 3, 4, 8]

while True:
    print("\n" + "=" * 30)
    for i in range(4):
        print(f"{i + 1}. {names[i]} - {prices[i]}元 现有:{counts[i]}个")
    print("0. 结束")

    choice = int(input("请选择："))

    if choice == 0:
        break

    if 1 <= choice <= 4:
        idx = choice - 1
        num = int(input(f"买几个{names[idx]}？"))
        if num > 0:
            counts[idx] += num
            print(f"买了{num}个{names[idx]}")
    else:
        print("输入错误")

# 计算总价
total = 0
for i in range(4):
    total += prices[i] * counts[i]
print(f"\n总价：{total}元")