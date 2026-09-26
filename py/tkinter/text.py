import tkinter as tk
root = tk.Tk()
root.geometry("400x400")

# 第一列只有一个短文字，会非常窄
label1 = tk.Label(root, text="短")
label1.grid(row=0, column=0)

# 第二列文字很长，这一列会变得很宽
label2 = tk.Label(root, text="超级无敌长的文字")
label2.grid(row=0, column=1)

label3 = tk.Label(root, text="超级无敌长的文字")
label3.grid(row=1, column=0)

# 第二列文字很长，这一列会变得很宽
label4 = tk.Label(root, text="短")
label4.grid(row=1, column=1)

root.mainloop()