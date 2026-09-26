while True:
    print("\n===== 留言板 =====")
    print("1. 写留言")
    print("2. 查看所有留言")
    print("0. 退出")

    choice = input("请选择：")

    if choice == "0":
        print("再见！")
        break

    elif choice == "1":
        msg = input("请输入你的留言：")
        with open("messages.txt", "a", encoding="utf-8") as f:
            f.write(msg + "\n")
        print("留言已保存！")

    elif choice == "2":
        try:
            with open("messages.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()

            if len(lines) == 0:
                print("暂无留言")
            else:
                print("\n===== 所有留言 =====")
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
        except FileNotFoundError:
            print("暂无留言（文件不存在）")

    else:
        print("输入错误")