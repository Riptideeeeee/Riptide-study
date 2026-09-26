employees = {
    "001": {"name": "张三", "department": "技术部", "base_salary": 8000, "bonus": 2000},
    "002": {"name": "李四", "department": "市场部", "base_salary": 7000, "bonus": 3000},
    "003": {"name": "王五", "department": "技术部", "base_salary": 9000, "bonus": 2500},
    "004": {"name": "赵六", "department": "人事部", "base_salary": 6500, "bonus": 1500},
    "005": {"name": "小明", "department": "技术部", "base_salary": 8500, "bonus": 2200}
}


def calc_real_salary():
    """计算实发工资 = 底薪 + 奖金"""
    employee=input("查谁的工资")
    realsalary=employees[employee]["base_salary"]+employees[employee]["bonus"]
    return realsalary

def show_all_employees():
    """显示所有员工信息"""
    for employee in employees:
        print(employee,employees[employee]["name"],employees[employee]["department"],employees[employee]["bonus"],employees[employee]["base_salary"])

def search_employee():
    """查询单个员工工资"""
    search=input("希望查询谁: ")
    if search in employees:
        print(f"{search},{employees[search]}")
    else:
        print("该员工不存在")


def show_dept_average():
    """显示所有部门的平均工资"""
    salary=[0,0,0]
    num=[0,0,0]
    for man in employees:
        if employees[man]["department"] =="技术部":
            salary[0]+=employees[man]["base_salary"]
            num[0]+=1
        elif employees[man]["department"]=='人事部':
            salary[1]+=employees[man]["base_salary"]
            num[1]+=1
        else:
            salary[2]+=employees[man]["base_salary"]
            num[2]+=1
    print("技术部", salary[0] / num[0])
    print("人事部", salary[1] / num[1])
    print("市场部", salary[2] / num[2])

def find_highest_salary():
    """找出最高工资的员工"""
    pass


def add_new_employee():
    """添加新员工"""
    
    pass


def raise_employee_salary():
    """给员工涨薪"""
    pass


def show_menu():
    print("\n===== 员工工资管理系统 =====")
    print("1. 显示所有员工信息")
    print("2. 查询单个员工工资")
    print("3. 计算部门平均工资")
    print("4. 找出最高工资员工")
    print("5. 添加新员工")
    print("6. 给员工涨薪")
    print("0. 退出")


# 主程序
while True:
    show_menu()
    choice = input("请选择(0-6)：")

    if choice == "0":
        print("再见！")
        break
    elif choice == "1":
        show_all_employees()
    elif choice == "2":
        search_employee()
    elif choice == "3":
        show_dept_average()
    elif choice == "4":
        find_highest_salary()
    elif choice == "5":
        add_new_employee()
    elif choice == "6":
        raise_employee_salary()
    else:
        print("输入错误，请重新选择")