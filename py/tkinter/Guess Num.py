import tkinter as tk
import random
from tkinter import simpledialog
root = tk.Tk()
root.geometry("500x500")
root.title("猜数字")

answer=random.randint(1,100)
now_min=1
now_max=100
rangenow=f"目前范围：{now_min} - {now_max}"
a=0
b="大"
result="点击开始猜数"
print(answer)
times=0

text=tk.Label(root,text="💣猜数字",font=("微软雅黑",40),fg="black",bg="lightblue")
text_now_range=tk.Label(root,text=rangenow,font=("微软雅黑",30),fg="black")
text_result=tk.Label(root,text=result,font=("微软雅黑",30),fg="black")
text_times=tk.Label(root,text=f"一共猜了{times}次",font=("微软雅黑",30),fg="black")

text.pack()
text_now_range.pack()
text_result.pack()

def guess():
    global a,b,result,now_min,now_max,text_now_range,text_result,times
    guess_num=simpledialog.askinteger("猜数","输入你猜的数: ")
    a=guess_num
    times=times+1
    if guess_num==answer:
        text_result.config(text="🎉 恭喜猜中！")
        text_now_range.config(text=f"答案是{answer}")
        text_now_range.pack()
        text_result.pack(pady=20)
        text_times.config(text=f"一共猜了{times}次")
        text_times.pack(side="bottom")
    else:
        if guess_num>answer:
            b = "大"
            if guess_num>now_max:
                pass
            else:
                now_max = guess_num

        elif guess_num < answer:
            b = "小"
            if guess_num<now_min:
                pass
            else:
                now_min = guess_num
        rangenow = f"目前范围：{now_min} - {now_max}"
        result = f"你猜的是{a}，猜{b}了"
        text_now_range.config(text=rangenow)
        text_result.config(text=result)
        text_now_range.pack()
        text_result.pack(pady=(10, 5))
        text_times.config(text=f"一共猜了{times}次")
        text_times.pack(side="bottom")



guess_button=tk.Button(root,text="点我猜数字",font=("微软雅黑",50),command=guess,bg="lightblue",fg="black")
guess_button.pack(side="bottom")
text_times.pack(side="bottom")
root.mainloop()