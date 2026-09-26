import os
import sys

def load_data():
    """从文件读取数据，返回字典"""
    try:
        with open("students.txt","r",encoding="utf-8") as f:
            students = f.readlines()
    except FileNotFoundError:
        students = ["001,张三,85,92,78\n","002,李四,90,88,85\n","003,王五,76,95,82\n"]
        with open("students.txt","w",encoding="utf-8") as f:
            f.writelines(students)
    with open("students.txt","r+",encoding="utf-8") as f:
        a=f.readline(2)
        if a=="":
            students = ["001,张三,85,92,78\n", "002,李四,90,88,85\n", "003,王五,76,95,82\n"]
            f.writelines(students)
    # 如果文件存在，读取
    # 如果文件不存在，创建并写入初始数据
    return students
load_data()
data={}
def read_student():
    """读取文件变成字典"""
    with open("students.txt", "r",encoding="utf-8") as f:
        read = f.readlines()
    #read = ["001,张三,85,92,78\n", "002,李四,90,88,85\n", "003,王五,76,95,82\n"]
    #student="001,张三,85,92,78"
    #part=["001","zs","85","92","78]
    for student in read:
        student = student.strip("\n")
        part = student.split(",")
        data[int(part[0])] = [part[1],part[2],part[3],part[4]]
    pass
read_student()
def save_data():
    """保存数据到文件"""
    with open("students.txt","w",encoding="utf-8") as f:
        f.write("")
    for i in data:
        if 0<=i<=9:
            with open("students.txt","a+",encoding="utf-8") as f:
                f.write("00"+str(i)+","+data[i][0]+","+data[i][1]+","+data[i][2]+","+data[i][3]+"\n")
        elif 10<=i<=100:
            with open("students.txt", "a+", encoding="utf-8") as f:
                f.write("0" + str(i) + "," + data[i][0] + "," + data[i][1] + "," + data[i][2] + "," + data[i][3] + "\n")
    pass
def empty_data():
    with open("students.txt","r+",encoding="utf-8") as f:
        a=f.readline(2)
        if a=="":
            students = ["001,张三,85,92,78\n", "002,李四,90,88,85\n", "003,王五,76,95,82\n"]
            f.writelines(students)
            print("数据库内没有学生了，已自动填入数据")
            save_data()
            pass
        else:
            pass
def student_exist(num):
    if num in data:
        return True
    else:
        print("该学生不存在！")
        return False
def clear_screen():
    """清空屏幕（Windows和Mac/Linux通用）"""
    if os.name == "nt":  # Windows
        os.system("cls")
    else:                # Mac/Linux
        os.system("clear")
def calc_total(num):
    """计算总分"""
    try:
        return int(data[num][1])+int(data[num][2])+int(data[num][3])
    except ValueError:
        print("存在学生成绩不是数字，请先修改再使用其他功能")
        python = sys.executable  # 获取当前 Python 解释器路径
        os.execl(python, python, *sys.argv)  # 用同样的参数重新执行
def calc_avg(num):
    """计算平均分"""
    return calc_total(num) / 3
def show_student(num):
    """显示单个学生信息"""
    empty_data()
    print("学号  名字")
    print(f"{num}    {data[num][0]}\n\n"
          f"语文 ：{data[num][1]}\n"
          f"数学 ：{data[num][2]}\n"
          f"英语 ：{data[num][3]}\n")
    print(f"总分 ：{calc_total(num)}\n"
          f"平均分 : {calc_avg(num)}\n")
    pass
def show_all():
    """显示所有学生"""
    empty_data()
    print("学号  名字  语文  数学  英语")
    for i in data:
        print(f"{i}  : {data[i][0]}   {data[i][1]}   {data[i][2]}   {data[i][3]}")
    pass
def add_student():
    """添加学生"""
    f=int(input("学生学号："))
    a=input("学生名字：")
    b=input("学生语文成绩：")
    c=input("学生数学成绩：")
    d=input("学生英语成绩：")
    data[f]=[a,b,c,d]
    pass
def delete_student(delete):
    """删除学生"""
    que=input("确认删除？1.确认   2.取消")
    if que=="1":
        del data[delete]
        print("删除成功！")
        for i in data:
            print(f"{i}: {data[i][0]}")
        pass
    elif que=="2":
        print("取消删除")
        pass
    else:
        print("选错了")
        pass
def show_stats():
    """统计信息"""
    total=0
    avg=0
    empty_data()
    for i in data:
        avg+=calc_avg(i)
        total+=calc_total(i)
    print(f"班级总分是：{total}\n班级平均分是：{avg/len(data)}")
def modify_score(num):
    """修改成绩"""
    empty_data()
    a=input("语文成绩是：")
    b=input("数学成绩是：")
    c=input("英语成绩是：")
    data[num]=[data[num][0],a,b,c]
    pass
def show_all_students():
    empty_data()
    for i in data:
        print(f"{i} : {data[i][0]}")
    pass

# ===== 主程序 =====
def main():
    while True:

        print("\n===== 学生成绩管理系统 =====")
        print("1. 显示所有学生成绩")
        print("2. 查询某个学生成绩")
        print("3. 添加新学生")
        print("4. 删除学生")
        print("5. 统计信息")
        print("6. 修改成绩")
        print("0. 退出")

        choice = input("请选择：")
        clear_screen()
        if choice == "0":
            save_data()
            print("再见！")
            break
        elif choice == "1":
            show_all()
        elif choice == "2":
            show_all_students()
            i=int(input("希望查询谁的成绩："))
            if student_exist(i):
                show_student(i)
            else:
                continue
        elif choice == "3":
            add_student()
            save_data()
        elif choice == "4":
            for i in data:
                print(f"编号{i} : {data[i][0]}")
            delete = int(input("希望删除谁"))
            if student_exist(delete):
                delete_student(delete)
                save_data()
            else:
                continue
        elif choice == "5":
            show_stats()
        elif choice == "6":
            show_all_students()
            i =int( input("希望修改谁的成绩："))
            if student_exist(i):
                modify_score(i)
                save_data()
            else:
                continue

        else:
            print("输入错误，请重新选择！")


if __name__ == "__main__":
    main()