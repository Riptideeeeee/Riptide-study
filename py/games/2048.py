import random
import os
import sys

# 尝试导入 curses 库（Windows 可能需要额外安装）
try:
    import curses

    CURSES_AVAILABLE = True
except ImportError:
    CURSES_AVAILABLE = False
    print("提示：为获得更好的游戏体验，请在Windows上运行: pip install windows-curses")


class Game2048:
    def __init__(self):
        """初始化游戏"""
        self.size = 4  # 棋盘大小 4x4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.best_score = self.load_best_score()
        self.add_new_tile()
        self.add_new_tile()

    def load_best_score(self):
        """加载最高分记录"""
        try:
            with open("2048_best_score.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_best_score(self):
        """保存最高分记录"""
        if self.score > self.best_score:
            self.best_score = self.score
            try:
                with open("2048_best_score.txt", "w") as f:
                    f.write(str(self.best_score))
            except:
                pass

    def add_new_tile(self):
        """在随机空白位置添加一个新数字（2或4）"""
        empty_cells = [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            # 90%概率生成2，10%概率生成4
            self.board[i][j] = 2 if random.random() < 0.9 else 4

    def compress(self, row):
        """将一行中的非零数字向左移动"""
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        """合并相邻的相同数字"""
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                self.score += row[i]
                row[i + 1] = 0
        return row

    def move_left(self):
        """向左移动"""
        changed = False
        for i in range(self.size):
            original_row = self.board[i][:]
            new_row = self.compress(self.board[i])
            new_row = self.merge(new_row)
            new_row = self.compress(new_row)
            self.board[i] = new_row
            if original_row != self.board[i]:
                changed = True
        return changed

    def move_right(self):
        """向右移动"""
        changed = False
        for i in range(self.size):
            original_row = self.board[i][:]
            # 反转行，处理后再次反转
            reversed_row = self.board[i][::-1]
            new_row = self.compress(reversed_row)
            new_row = self.merge(new_row)
            new_row = self.compress(new_row)
            self.board[i] = new_row[::-1]
            if original_row != self.board[i]:
                changed = True
        return changed

    def move_up(self):
        """向上移动"""
        changed = False
        for j in range(self.size):
            # 获取列
            column = [self.board[i][j] for i in range(self.size)]
            original_column = column[:]
            new_column = self.compress(column)
            new_column = self.merge(new_column)
            new_column = self.compress(new_column)
            # 放回原处
            for i in range(self.size):
                self.board[i][j] = new_column[i]
            if original_column != new_column:
                changed = True
        return changed

    def move_down(self):
        """向下移动"""
        changed = False
        for j in range(self.size):
            # 获取列并反转
            column = [self.board[i][j] for i in range(self.size)]
            original_column = column[:]
            reversed_column = column[::-1]
            new_column = self.compress(reversed_column)
            new_column = self.merge(new_column)
            new_column = self.compress(new_column)
            new_column = new_column[::-1]
            # 放回原处
            for i in range(self.size):
                self.board[i][j] = new_column[i]
            if original_column != new_column:
                changed = True
        return changed

    def is_game_over(self):
        """检查游戏是否结束"""
        # 检查是否有空格
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return False

        # 检查是否有相邻的相同数字
        for i in range(self.size):
            for j in range(self.size - 1):
                if self.board[i][j] == self.board[i][j + 1]:
                    return False

        for i in range(self.size - 1):
            for j in range(self.size):
                if self.board[i][j] == self.board[i + 1][j]:
                    return False

        return True

    def has_won(self):
        """检查是否达到2048"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 2048:
                    return True
        return False

    def print_board_console(self):
        """在控制台打印游戏界面"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("                    2048 游戏")
        print("=" * 50)
        print(f"得分: {self.score}  |  最高分: {self.best_score}")
        print("-" * 50)

        for i in range(self.size):
            print("|", end=" ")
            for j in range(self.size):
                if self.board[i][j] == 0:
                    print("    ".center(6), end=" | ")
                else:
                    # 不同数字用不同颜色（仅支持部分终端）
                    num = self.board[i][j]
                    color_code = ""
                    reset_code = ""
                    if sys.platform != "win32":  # 非Windows系统支持颜色
                        if num < 16:
                            color_code = "\033[94m"  # 蓝色
                        elif num < 64:
                            color_code = "\033[92m"  # 绿色
                        elif num < 256:
                            color_code = "\033[93m"  # 黄色
                        elif num < 1024:
                            color_code = "\033[91m"  # 红色
                        else:
                            color_code = "\033[95m"  # 紫色
                        reset_code = "\033[0m"
                    print(f"{color_code}{str(num).center(4)}{reset_code}", end=" | ")
            print()
            print("-" * 50)

        print("\n操作说明：")
        print("  W/A/S/D 或 上/下/左/右 键移动")
        print("  R 键重新开始")
        print("  Q 键退出游戏")
        print("=" * 50)


def play_console():
    """控制台版本（使用键盘输入）"""
    game = Game2048()

    # 根据不同系统使用不同的输入方式
    if os.name == 'nt':  # Windows
        import msvcrt

        game.print_board_console()

        while True:
            if game.is_game_over():
                game.print_board_console()
                print("\n💀 游戏结束！💀")
                game.save_best_score()
                break

            if game.has_won():
                game.print_board_console()
                print("\n🎉 恭喜！你达到了2048！🎉")
                print("继续游戏可以获得更高分数...")

            key = msvcrt.getch().decode('utf-8').lower()

            if key == 'q':
                print("\n感谢游玩！")
                game.save_best_score()
                break
            elif key == 'r':
                game = Game2048()
                game.print_board_console()
                continue

            moved = False
            if key in ['w', 'w'] or key == '\x48':  # 上
                moved = game.move_up()
            elif key in ['s', 's'] or key == '\x50':  # 下
                moved = game.move_down()
            elif key in ['a', 'a'] or key == '\x4b':  # 左
                moved = game.move_left()
            elif key in ['d', 'd'] or key == '\x4d':  # 右
                moved = game.move_right()

            if moved:
                game.add_new_tile()
                game.print_board_console()
                game.save_best_score()

    else:  # Linux/Mac
        import termios
        import tty

        def get_key():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                key = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return key

        game.print_board_console()

        while True:
            if game.is_game_over():
                game.print_board_console()
                print("\n💀 游戏结束！💀")
                game.save_best_score()
                break

            if game.has_won():
                game.print_board_console()
                print("\n🎉 恭喜！你达到了2048！🎉")
                print("继续游戏可以获得更高分数...")

            key = get_key().lower()

            if key == 'q':
                print("\n感谢游玩！")
                game.save_best_score()
                break
            elif key == 'r':
                game = Game2048()
                game.print_board_console()
                continue

            moved = False
            if key in ['w', '\x1b[A']:  # 上
                moved = game.move_up()
            elif key in ['s', '\x1b[B']:  # 下
                moved = game.move_down()
            elif key in ['a', '\x1b[D']:  # 左
                moved = game.move_left()
            elif key in ['d', '\x1b[C']:  # 右
                moved = game.move_right()

            if moved:
                game.add_new_tile()
                game.print_board_console()
                game.save_best_score()


class Game2048GUI:
    """图形界面版本（使用 tkinter）"""

    def __init__(self):
        try:
            import tkinter as tk
            from tkinter import messagebox
            self.tk = tk
            self.messagebox = messagebox
        except ImportError:
            print("无法导入 tkinter，请使用控制台版本")
            return

        self.game = Game2048()
        self.root = self.tk.Tk()
        self.root.title("2048")
        self.root.resizable(False, False)

        # 颜色方案
        self.colors = {
            0: "#CDC1B4",
            2: "#EEE4DA",
            4: "#EDE0C8",
            8: "#F2B179",
            16: "#F59563",
            32: "#F67C5F",
            64: "#F65E3B",
            128: "#EDCF72",
            256: "#EDCC61",
            512: "#EDC850",
            1024: "#EDC53F",
            2048: "#EDC22E",
        }

        self.setup_ui()
        self.update_display()
        self.root.mainloop()

    def setup_ui(self):
        """设置界面"""
        # 分数显示区域
        info_frame = self.tk.Frame(self.root)
        info_frame.pack(pady=10)

        self.score_label = self.tk.Label(info_frame, text=f"Score: {self.game.score}",
                                         font=("Arial", 16, "bold"))
        self.score_label.pack(side=self.tk.LEFT, padx=20)

        self.best_label = self.tk.Label(info_frame, text=f"Best: {self.game.best_score}",
                                        font=("Arial", 16, "bold"))
        self.best_label.pack(side=self.tk.LEFT, padx=20)

        # 游戏棋盘
        self.board_frame = self.tk.Frame(self.root)
        self.board_frame.pack(pady=10)

        self.cells = []
        for i in range(4):
            row = []
            for j in range(4):
                cell = self.tk.Label(self.board_frame, text="", width=6, height=3,
                                     font=("Arial", 20, "bold"), relief="ridge")
                cell.grid(row=i, column=j, padx=5, pady=5)
                row.append(cell)
            self.cells.append(row)

        # 控制按钮
        button_frame = self.tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.tk.Button(button_frame, text="新游戏", command=self.new_game,
                       font=("Arial", 12), width=10).pack(side=self.tk.LEFT, padx=10)
        self.tk.Button(button_frame, text="退出", command=self.root.quit,
                       font=("Arial", 12), width=10).pack(side=self.tk.LEFT, padx=10)

        # 绑定键盘事件
        self.root.bind("<Up>", lambda e: self.move("up"))
        self.root.bind("<Down>", lambda e: self.move("down"))
        self.root.bind("<Left>", lambda e: self.move("left"))
        self.root.bind("<Right>", lambda e: self.move("right"))
        self.root.bind("<w>", lambda e: self.move("up"))
        self.root.bind("<s>", lambda e: self.move("down"))
        self.root.bind("<a>", lambda e: self.move("left"))
        self.root.bind("<d>", lambda e: self.move("right"))

    def update_display(self):
        """更新显示"""
        self.score_label.config(text=f"Score: {self.game.score}")
        self.best_label.config(text=f"Best: {self.game.best_score}")

        for i in range(4):
            for j in range(4):
                value = self.game.board[i][j]
                color = self.colors.get(value, "#EDC22E")
                self.cells[i][j].config(
                    text=str(value) if value != 0 else "",
                    bg=color,
                    fg="#776E65" if value <= 4 else "#F9F6F2"
                )

    def move(self, direction):
        """处理移动"""
        moved = False
        if direction == "up":
            moved = self.game.move_up()
        elif direction == "down":
            moved = self.game.move_down()
        elif direction == "left":
            moved = self.game.move_left()
        elif direction == "right":
            moved = self.game.move_right()

        if moved:
            self.game.add_new_tile()
            self.update_display()
            self.game.save_best_score()

            if self.game.has_won():
                if self.messagebox.askyesno("胜利！", "恭喜达到2048！是否继续游戏？"):
                    pass
                else:
                    self.root.quit()
            elif self.game.is_game_over():
                if self.messagebox.askyesno("游戏结束", f"最终得分: {self.game.score}\n是否重新开始？"):
                    self.new_game()
                else:
                    self.root.quit()

    def new_game(self):
        """重新开始游戏"""
        self.game = Game2048()
        self.update_display()


def main():
    """主函数：选择游戏模式"""
    print("=" * 50)
    print("           2048 游戏")
    print("=" * 50)
    print("\n请选择游戏模式：")
    print("  1. 图形界面模式（推荐）")
    print("  2. 控制台模式")
    print("  3. 退出")

    while True:
        choice = input("\n请输入选择 (1-3): ").strip()
        if choice == "1":
            try:
                Game2048GUI()
                break
            except:
                print("图形界面启动失败，尝试使用控制台模式...")
                play_console()
                break
        elif choice == "2":
            play_console()
            break
        elif choice == "3":
            print("感谢游玩！")
            break
        else:
            print("无效选择，请输入 1, 2 或 3")


if __name__ == "__main__":
    main()