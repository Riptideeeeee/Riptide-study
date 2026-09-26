fruits = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
prices = [5, 3, 4, 8, 12]
numbers = [0,0,0,0,0]
while True:
    print("\n===== 水果价格系统 =====")
    print("1. 显示所有水果价格")
    print("2. 查询某种水果价格")
    print("3. 买水果")
    print("4. 找出最便宜的水果")
    print("5. 查看现在账单")
    print("0. 退出")

    choice = input("请选择：")

    if choice == "0":
        print("再见！")
        break

    elif choice == "1":
        # 功能1：显示所有水果价格
        for a in range(5):
            print(f"{fruits[a]} 为 {prices[a]} 元")
        # 用 for 循环遍历，打印水果和价格
        pass  # 请填写

    elif choice == "2":
        # 功能2：查询某种水果价格
        # 输入水果名，用 for 循环查找
        for b in range (5):
            print(f"{b+1} : {fruits[b]} , ",end="")
        print()
        while True:
            question = int(input("你想知道谁的价格:"))
            if 1 <= question <= 5:
                print(f"{fruits[question-1]} : {prices[question-1]} 元")
                break
            else:
                print("输入的水果不存在!")

        pass  # 请填写

    elif choice == "3":
        # 功能3：计算总价
        # 用 while 循环让用户选择购买

        while True:
            for b in range (5):
                print(f"{b+1} : {fruits[b]} ",end=", ")
            print("0 : 退出购买")
            buyWhat = int(input("买："))
            if 1 <= buyWhat <= 5:
                print(f"买几个{fruits[buyWhat-1]}？请输入：",end="")
                num=int(input())
                #判断num是正还是负
                if num>0:
                    print(f"买了{num}个{fruits[buyWhat-1]}")
                    numbers[buyWhat-1]+=num
                elif num==0:
                    print("买0个？")
                else:
                    if numbers[buyWhat-1]>0-num:
                        print(f"减少{0-num}个{fruits[buyWhat-1]}")
                        numbers[buyWhat-1]+=num
                    else:
                        print(f"个数不足，将您的{fruits[buyWhat-1]}扣成0个")
                        numbers[buyWhat-1]=0
                num=0
            elif buyWhat == 0:
                break
            else:
                print("没有这么多水果")
        pass  # 请填写

    elif choice == "4":
        # 功能4：找出最便宜的水果
        # 用 for 循环找出最低价格
        low=0
        lowprice=100
        for i in range(5):
            if lowprice>=prices[i]:
                lowprice=prices[i]
                low=i
            else:
                lowprice=lowprice
        print(f"最低价是{fruits[low]}，最低价为{prices[low]}元")
        pass  # 请填写
    elif choice == "5":
        total=0
        for c in range (5):
            total += prices[c]*numbers[c]
            print(f"{c+1} : {fruits[c]},买了{numbers[c]}个，花了{prices[c]*numbers[c]}元")
        print(f"一共花了{total}元")
    else:
        print("输入错误，请输入0-4")