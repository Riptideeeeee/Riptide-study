import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x150")

def delete():
    result = messagebox.askyesno("确认删除", "确定要删除这条记录吗？")
    if result:
        label.config(text="已删除！", fg="red")
    else:
        label.config(text="取消删除", fg="blue")

label = tk.Label(root, text="等待操作", font=("微软雅黑", 16))
label.pack(pady=20)

tk.Button(root, text="删除", command=delete).pack()

root.mainloop()