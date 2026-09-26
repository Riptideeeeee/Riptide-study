import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.geometry("300x150")

def get_name():
    name = simpledialog.askstring("输入姓名", "请输入你的名字：")
    if name:
        label.config(text=f"你好，{name}！")

label = tk.Label(root, text="", font=("微软雅黑", 16))
label.pack(pady=20)

tk.Button(root, text="输入名字", command=get_name).pack()

root.mainloop()