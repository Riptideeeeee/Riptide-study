import tkinter as tk
try :
    with open("data.txt","r",encoding="utf-8") as f:
        read = f.read()
except FileNotFoundError:
    with open("data.txt","w",encoding="utf-8") as f:
        f.write("")
root = tk.Tk()
root.title("记账本")
size=root.maxsize()
root.geometry(f"1080x720+{int((size[0]-1080)/2)}+{int((size[1]-720)/2)}")




# 4. padx/pady：间距













root.mainloop()
