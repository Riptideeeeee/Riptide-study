import tkinter as tk
import random

names = ["张三", "李四", "王五", "赵六", "小明", "小红", "小刚", "小美", "刘洋", "陈静"]
remaining = names.copy()
current_name = ""
count = 0
is_running = False
timer_id = None

root = tk.Tk()
root.title("🎯 随机点名器")
root.geometry("400x350")

# ===== 显示名字 =====
name_label = tk.Label(
    root,
    text="点击「开始点名」",
    font=("微软雅黑", 40, "bold"),
    fg="gray"
)
name_label.pack(pady=40)

count_label = tk.Label(
    root,
    text="已点：0 人",
    font=("微软雅黑", 14),
    fg="gray"
)
count_label.pack(pady=10)


def pick_random():
    """随机选一个名字并更新显示，返回是否还有剩余"""
    global current_name

    if not remaining:
        name_label.config(text="🎉 全部点完！", fg="green")
        return False

    current_name = random.choice(remaining)
    name_label.config(text=current_name, fg="blue")
    return True


def roll():
    """滚动更新（每次定时器触发时调用）"""
    global timer_id

    # 如果已停止，不再继续
    if not is_running:
        return

    # 如果已点完，停止
    if not remaining:
        name_label.config(text="🎉 全部点完！", fg="green")
        return

    # 随机选一个名字显示
    pick_random()

    # 继续安排下一次更新
    timer_id = root.after(80, roll)


def start():
    """开始点名"""
    global is_running, timer_id

    if is_running:
        return

    if not remaining:
        name_label.config(text="🎉 全部点完！", fg="green")
        return

    is_running = True
    roll()  # 启动滚动循环


def stop():
    """停止点名，记录结果"""
    global count, is_running, timer_id, current_name

    if not is_running:
        return

    # 1. 取消定时器
    if timer_id:
        root.after_cancel(timer_id)
        timer_id = None

    is_running = False

    # 2. 记录当前名字
    if current_name and current_name in remaining:
        remaining.remove(current_name)
        count += 1
        count_label.config(text=f"已点：{count} 人")
        name_label.config(fg="green")

        if not remaining:
            name_label.config(text="🎉 全部点完！", fg="green")


# ===== 按钮 =====
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

btn_start = tk.Button(
    btn_frame,
    text="开始点名",
    font=("微软雅黑", 14),
    bg="#4CAF50",
    fg="white",
    width=10,
    command=start
)
btn_start.pack(side="left", padx=20)

btn_stop = tk.Button(
    btn_frame,
    text="停止",
    font=("微软雅黑", 14),
    bg="#FF5722",
    fg="white",
    width=10,
    command=stop
)
btn_stop.pack(side="left", padx=20)

root.mainloop()