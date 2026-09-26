import tkinter as tk
import random
from turtledemo import clock

root = tk.Tk()
root.title("打地鼠")
root.geometry("500x500")

gap=10
length=36
button={}

for i in range(3):
    button[i]=[]
    for j in range(3):
        button[i].append(tk.Button(root,bg="skyblue", width=9, height=3))
        button[i][j].grid(row=i,column=j,ipadx=length,ipady=length,padx=gap,pady=gap)
def transform():
    ran=random.randint(0,8)
    a=int(ran/3)
    b=ran%3
    button[a][b-1].config(bg="red")
def click(event):
    event.widget.config(bg="orange")

def turn():
    transform()
    clock=root.after(1000,turn)
    clock.stop()


for i in range(3):
    for j in range(3):
        button[i][j].bind("<Button-1>",click)

root.mainloop()