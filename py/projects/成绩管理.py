students = {
    "张三": {"语文": 85, "数学": 92, "英语": 78},
    "李四": {"语文": 90, "数学": 88, "英语": 85},
    "王五": {"语文": 76, "数学": 95, "英语": 82},
    "赵六": {"语文": 88, "数学": 79, "英语": 91},
    "小明": {"语文": 95, "数学": 98, "英语": 94}
}
while True:

    choise=input("""===== 学生成绩管理系统 =====
1. 显示所有学生成绩
2. 查询某个学生的成绩
3. 计算总分和平均分
4. 找出单科最高分
5. 找出总分第一名
6. 添加新学生
0. 退出
请选择：
""")
    if choise=="1":
        for stu , score in students.items():
            print(stu,end=' ')
            for sco in score:
                print(sco,",",score[sco],end=' , ')
            print()

    elif choise=="2":
        #2.查询某个学生的成绩
        ask=input("希望查询谁的成绩:")
        if ask in students:
            print(ask)
            for sco in students[ask]:
                print(sco,",",students[ask][sco],end=' ,')
            print()
        else:
            print("学生不存在！")

    elif choise=="3":
        #3.计算总分和平均分
        chinese=0
        for i in students:
            chinese += students[i]['语文']
        math = 0
        for i in students:
            math += students[i]['数学']
        english = 0
        for i in students:
            english += students[i]['英语']
        print ("语文：",chinese,"数学",math,"英语",english)
        print(f"语文平均分: {chinese/len(students)} 数学平均分: {math/len(students)} 英语平均分:{english/len(students)}")
        allsco=chinese+math+english
        print(f"总分：{allsco} 总分平均分：{allsco/len(students)}")

    elif choise=="4":
        #4. 找出单科最高分
        high= {'语文':0,'数学':0,'英语':0}
        student={'语文':' ','数学':' ','英语':' '}
        for sub in {'语文','数学','英语'}:
            for stu in students:
                if high[sub]<=students[stu][sub]:
                    high[sub]=students[stu][sub]
                    student[sub]=stu
        print(f"语文最高分是{student['语文']} : {high['语文']}分\n数学最高分是{student['数学']} : {high['数学']}分\n英语最高分是{student['英语']} : {high['英语']}分")

    elif choise=="5":
        allhigh=0
        highstu=str()
        for stu in students:
            stuall=0
            for sco in students[stu]:
                stuall+=students[stu][sco]
            if stuall>allhigh:
                allhigh=stuall
                highstu=stu
        print(f"总分第一是{highstu}, 分数为{allhigh}")

    elif choise=="6":
        name=input("添加学生名字为:")
        newstudent={"语文": 0, "数学": 0, "英语": 0}
        students[name] = newstudent
        students[name]['语文'] = int(input("学生语文成绩为: "))
        students[name]['数学'] = int(input("学生数学成绩为: "))
        students[name]['英语'] = int(input("学生英语成绩为: "))
        print(f"学生{name}已录入")

    elif choise=="0":
        print("感谢使用！")
        break
    else:
        print("输入的数字不正确")