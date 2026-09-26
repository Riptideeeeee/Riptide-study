import tkinter as tk

root = tk.Tk()

# 没有 pady
tk.Label(root, text="没有间距", bg="lightblue").pack()

# 有 pady
tk.Label(root, text="有 pady=20", bg="lightgreen").pack(pady=200)

# 对比用的标签
tk.Label(root, text="我在下面", bg="lightcoral").pack()

root.mainloop()