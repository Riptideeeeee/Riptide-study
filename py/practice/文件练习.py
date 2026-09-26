import os
def clear():
    """清空屏幕（Windows和Mac/Linux通用）"""
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Mac/Linux
        os.system("clear")


word=open("liuyan.txt","r+")
linenum=word.read(2)
if linenum=="":
    word.write("00\n")
    word.close()
    word=open("liuyan.txt","r")
    linenum = word.read(2)
num=0
num=int(linenum)
word.close()
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
        clear()
        liuyan=input("留言是什么:")
        f = open("liuyan.txt", "a")
        num += 1
        f.write(f"{num} : {liuyan}\n")
        f.close()

        with open ("liuyan.txt", "r") as f:
            line = f.readlines()
        if 0<=num<=9:
            line[0]=("0"+str(num)+"\n")
        elif num>=9:
            line[0]=(str(num)+"\n")
        with open ("liuyan.txt", "w") as f:
            f.writelines(line)

        pass

    elif choice == "2":
        clear()
        print(f"\n以下是留言，一共{num}条")
        with open ("liuyan.txt", "r") as f:
            read = f.readlines()
            for i in range (num):
                print(read[i+1],end="")
        # 查看所有留言
        pass

    else:
        print("输入错误")
