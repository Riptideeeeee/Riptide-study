import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x150")

def show():
    messagebox.showinfo("提示", "操作成功！")
    messagebox.showwarning("警告", "库存不足！")
    messagebox.showerror("错误", "文件不存在！")
    result = messagebox.askyesno("确认", "确定要删除吗？")
    if result:
        print("用户点了「是」")
    else:
        print("用户点了「否」")
    
tk.Button(root, text="点击", command=show).pack()

root.mainloop()