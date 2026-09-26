import os

# ===== 全局数据 =====
data = {}


# ===== 文件操作 =====
def read_student():
    """从文件读取数据，存入全局字典 data"""
    global data
    data = {}

    try:
        with open("students.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        # 文件不存在，创建初始数据
        lines = ["001,张三,85,92,78\n", "002,李四,90,88,85\n", "003,王五,76,95,82\n"]
        with open("students.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)

    # 解析数据
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split(",")
            eid = parts[0]  # 保持字符串格式
            data[eid] = [parts[1], parts[2], parts[3], parts[4]]


def save_data():
    """保存数据到文件"""
    with open("students.txt", "w", encoding="utf-8") as f:
        for eid, info in data.items():
            line = f"{eid},{info[0]},{info[1]},{info[2]},{info[3]}\n"
            f.write(line)


def check_empty():
    """检查数据是否为空"""
    if not data:
        lines = ["001,张三,85,92,78\n", "002,李四,90,88,85\n", "003,王五,76,95,82\n"]
        with open("students.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
        read_student()
        print("数据库为空，已自动填入初始数据")


# ===== 核心功能 =====
def calc_total(eid):
    """计算总分"""
    try:
        return int(data[eid][1]) + int(data[eid][2]) + int(data[eid][3])
    except (ValueError, KeyError):
        return 0


def calc_avg(eid):
    """计算平均分"""
    return calc_total(eid) / 3


def student_exist(eid):
    """检查学生是否存在"""
    return eid in data


def clear_screen():
    """清屏"""
    os.system("cls" if os.name == "nt" else "clear")


# ===== 显示功能 =====
def show_student(eid):
    """显示单个学生"""
    info = data[eid]
    print(f"\n学号：{eid}")
    print(f"姓名：{info[0]}")
    print(f"语文：{info[1]}")
    print(f"数学：{info[2]}")
    print(f"英语：{info[3]}")
    print(f"总分：{calc_total(eid)}")
    print(f"平均分：{calc_avg(eid):.1f}")


def show_all():
    """显示所有学生"""
    check_empty()
    print("\n学号    姓名    语文    数学    英语    总分")
    print("-" * 45)
    for eid, info in data.items():
        total = calc_total(eid)
        print(f"{eid}    {info[0]}     {info[1]}      {info[2]}      {info[3]}     {total}")


def show_all_students():
    """显示所有学生（简版）"""
    check_empty()
    for eid, info in data.items():
        print(f"{eid} : {info[0]}")


def show_stats():
    """统计信息"""
    check_empty()
    if not data:
        print("暂无学生数据")
        return

    total_score = 0
    for eid in data:
        total_score += calc_total(eid)

    count = len(data)
    print(f"\n班级总分：{total_score}")
    print(f"班级平均分：{total_score / count:.1f}")


# ===== 修改功能 =====
def add_student():
    """添加学生"""
    eid = input("请输入学号（如001）：")

    if eid in data:
        print("该学号已存在！")
        return

    name = input("请输入姓名：")
    chinese = input("请输入语文成绩：")
    math = input("请输入数学成绩：")
    english = input("请输入英语成绩：")

    data[eid] = [name, chinese, math, english]
    print(f"已添加学生：{name}")


def delete_student(eid):
    """删除学生"""
    name = data[eid][0]
    confirm = input(f"确认删除 {name}？(y/n)：")
    if confirm.lower() == "y":
        del data[eid]
        print("删除成功！")
    else:
        print("取消删除")


def modify_score(eid):
    """修改成绩"""
    info = data[eid]
    print(f"\n当前成绩：{info[0]} 语文{info[1]} 数学{info[2]} 英语{info[3]}")

    chinese = input("请输入新语文成绩（直接回车保留）：")
    math = input("请输入新数学成绩（直接回车保留）：")
    english = input("请输入新英语成绩（直接回车保留）：")

    if chinese:
        info[1] = chinese
    if math:
        info[2] = math
    if english:
        info[3] = english

    print("修改成功！")


# ===== 主程序 =====
def main():
    read_student()

    while True:
        clear_screen()
        print("\n===== 学生成绩管理系统 =====")
        print("1. 显示所有学生成绩")
        print("2. 查询某个学生成绩")
        print("3. 添加新学生")
        print("4. 删除学生")
        print("5. 统计信息")
        print("6. 修改成绩")
        print("0. 退出")

        choice = input("请选择：")

        if choice == "0":
            save_data()
            print("再见！")
            break

        elif choice == "1":
            show_all()
            input("\n按回车键继续...")

        elif choice == "2":
            show_all_students()
            eid = input("请输入学号：")
            if student_exist(eid):
                show_student(eid)
            else:
                print("该学生不存在！")
            input("\n按回车键继续...")

        elif choice == "3":
            add_student()
            save_data()
            input("\n按回车键继续...")

        elif choice == "4":
            show_all_students()
            eid = input("请输入要删除的学号：")
            if student_exist(eid):
                delete_student(eid)
                save_data()
            else:
                print("该学生不存在！")
            input("\n按回车键继续...")

        elif choice == "5":
            show_stats()
            input("\n按回车键继续...")

        elif choice == "6":
            show_all_students()
            eid = input("请输入要修改的学号：")
            if student_exist(eid):
                modify_score(eid)
                save_data()
            else:
                print("该学生不存在！")
            input("\n按回车键继续...")

        else:
            print("输入错误，请重新选择！")
            input("\n按回车键继续...")


if __name__ == "__main__":
    main()