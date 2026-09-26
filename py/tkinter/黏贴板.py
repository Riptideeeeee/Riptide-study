from tkinter import *

root = Tk()
root.geometry("400x300")

frame = Frame(root, bg="lightgray", width=380, height=280)
frame.pack(padx=10, pady=10)

# side="left" 时 anchor 控制垂直方向
Label(frame, text="left + n", bg="red").pack(side="left", anchor="n")
Label(frame, text="left + center", bg="green").pack(side="left", anchor="center")
Label(frame, text="left + s", bg="blue").pack(side="left", anchor="s")
Label(frame, text="left + s", bg="blue").pack(side="right", anchor="n")

root.mainloop()