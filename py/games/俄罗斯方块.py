import tkinter as tk
import random

# 游戏常量
BOARD_WIDTH = 10          # 列数
BOARD_HEIGHT = 20         # 行数
BLOCK_SIZE = 30           # 每个格子的像素大小
FALL_INTERVAL = 500       # 初始下落间隔（毫秒）

# 7种标准形状，每种形状用一个二维列表表示（旋转前的形状）
SHAPES = [
    # I
    [[1, 1, 1, 1]],
    # O
    [[1, 1],
     [1, 1]],
    # T
    [[0, 1, 0],
     [1, 1, 1]],
    # S
    [[0, 1, 1],
     [1, 1, 0]],
    # Z
    [[1, 1, 0],
     [0, 1, 1]],
    # J
    [[1, 0, 0],
     [1, 1, 1]],
    # L
    [[0, 0, 1],
     [1, 1, 1]]
]

# 对应的颜色
SHAPE_COLORS = [
    'cyan',      # I
    'yellow',    # O
    'purple',    # T
    'green',     # S
    'red',       # Z
    'blue',      # J
    'orange'     # L
]


class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("俄罗斯方块")
        self.root.resizable(False, False)

        # 游戏状态
        self.board = [[None] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.game_over = False
        self.paused = False

        # 当前方块
        self.current_shape = None   # 形状矩阵
        self.current_color = None
        self.current_x = 0
        self.current_y = 0
        self.next_shape = None
        self.next_color = None

        # 计时器id（用于暂停/继续）
        self.after_id = None

        # 创建界面
        self.create_widgets()
        self.bind_keys()

        # 初始化游戏
        self.new_game()

    def create_widgets(self):
        """创建画布和显示信息的标签"""
        # 主画布，用于显示游戏板
        self.canvas = tk.Canvas(self.root, width=BOARD_WIDTH * BLOCK_SIZE,
                                height=BOARD_HEIGHT * BLOCK_SIZE,
                                bg='black')
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # 右侧信息面板
        info_frame = tk.Frame(self.root)
        info_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        # 下一个方块预览
        tk.Label(info_frame, text="下一个:", font=('Arial', 12)).pack(anchor=tk.W)
        self.preview_canvas = tk.Canvas(info_frame, width=4 * BLOCK_SIZE,
                                        height=4 * BLOCK_SIZE, bg='black')
        self.preview_canvas.pack(pady=5)

        # 分数
        tk.Label(info_frame, text="分数:", font=('Arial', 12)).pack(anchor=tk.W, pady=(15,0))
        self.score_label = tk.Label(info_frame, text="0", font=('Arial', 14, 'bold'))
        self.score_label.pack(anchor=tk.W)

        # 游戏状态提示
        self.status_label = tk.Label(info_frame, text="", font=('Arial', 12))
        self.status_label.pack(anchor=tk.W, pady=(15,0))

        # 操作说明
        help_text = """操作说明:
↑ 旋转
← → 左右移动
↓ 加速下落
空格 硬降
P 暂停
R 重新开始"""
        tk.Label(info_frame, text=help_text, font=('Arial', 10),
                 justify=tk.LEFT).pack(anchor=tk.W, pady=(20,0))

    def bind_keys(self):
        """绑定键盘事件"""
        self.root.bind('<Up>', self.rotate)
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<space>', self.hard_drop)
        self.root.bind('<p>', self.toggle_pause)
        self.root.bind('<r>', self.restart)
        # 确保焦点在root上
        self.root.focus_set()

    def new_game(self):
        """开始新游戏"""
        self.board = [[None] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.score = 0
        self.game_over = False
        self.paused = False
        self.status_label.config(text="")
        self.update_score()
        self.draw_board()
        self.spawn_new_piece()
        self.start_loop()

    def restart(self, event=None):
        """重新开始（按键R）"""
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.new_game()

    def toggle_pause(self, event=None):
        """暂停/继续"""
        if self.game_over:
            return
        self.paused = not self.paused
        if self.paused:
            self.status_label.config(text="暂停中")
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None
        else:
            self.status_label.config(text="")
            self.start_loop()

    def start_loop(self):
        """启动下落循环"""
        if not self.game_over and not self.paused:
            self.after_id = self.root.after(FALL_INTERVAL, self.step_down)

    def step_down(self):
        """每一步下落"""
        if not self.game_over and not self.paused:
            if self.move_down():
                # 如果成功下落，继续
                self.start_loop()
            else:
                # 如果无法下落，固定当前方块，检查消除，生成新方块
                self.fix_piece()
                self.clear_rows()
                self.spawn_new_piece()
                self.start_loop()

    # ---------- 方块操作 ----------

    def spawn_new_piece(self):
        """生成新的当前方块，并从下一个方块补充"""
        if self.next_shape is None:
            # 首次生成
            self.next_shape, self.next_color = self.random_piece()
        # 当前方块变为之前的下一个
        self.current_shape = [row[:] for row in self.next_shape]
        self.current_color = self.next_color
        # 生成新的下一个方块
        self.next_shape, self.next_color = self.random_piece()

        # 初始位置：居中，y=0
        self.current_x = BOARD_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0

        # 检查是否碰撞（游戏结束）
        if self.check_collision(self.current_shape, self.current_x, self.current_y):
            self.game_over = True
            self.status_label.config(text="游戏结束！")
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None
        else:
            self.draw_board()
            self.draw_preview()

    def random_piece(self):
        """随机选择一个形状和颜色"""
        idx = random.randint(0, len(SHAPES) - 1)
        shape = [row[:] for row in SHAPES[idx]]
        color = SHAPE_COLORS[idx]
        return shape, color

    def rotate(self, event=None):
        """旋转当前方块（顺时针旋转90度）"""
        if self.game_over or self.paused:
            return
        # 矩阵顺时针旋转
        rotated = list(zip(*self.current_shape[::-1]))
        # 转为列表
        rotated = [list(row) for row in rotated]
        # 检查旋转后的碰撞
        if not self.check_collision(rotated, self.current_x, self.current_y):
            self.current_shape = rotated
            self.draw_board()

    def move_left(self, event=None):
        if self.game_over or self.paused:
            return
        if not self.check_collision(self.current_shape, self.current_x - 1, self.current_y):
            self.current_x -= 1
            self.draw_board()

    def move_right(self, event=None):
        if self.game_over or self.paused:
            return
        if not self.check_collision(self.current_shape, self.current_x + 1, self.current_y):
            self.current_x += 1
            self.draw_board()

    def move_down(self, event=None):
        """下落一格，返回是否成功"""
        if self.game_over or self.paused:
            return False
        if not self.check_collision(self.current_shape, self.current_x, self.current_y + 1):
            self.current_y += 1
            self.draw_board()
            return True
        else:
            return False

    def hard_drop(self, event=None):
        """硬降：直接落到底"""
        if self.game_over or self.paused:
            return
        while not self.check_collision(self.current_shape, self.current_x, self.current_y + 1):
            self.current_y += 1
        # 固定并生成新方块
        self.fix_piece()
        self.clear_rows()
        self.spawn_new_piece()
        self.draw_board()
        # 重置定时器（让下落循环重新开始）
        if self.after_id:
            self.root.after_cancel(self.after_id)
            self.after_id = None
        self.start_loop()

    # ---------- 碰撞检测 ----------

    def check_collision(self, shape, offset_x, offset_y):
        """检测形状在给定偏移位置是否与边界或已固定方块重叠"""
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = offset_x + x
                    board_y = offset_y + y
                    # 检查边界
                    if board_x < 0 or board_x >= BOARD_WIDTH or board_y >= BOARD_HEIGHT:
                        return True
                    # 检查是否与已固定方块重叠（board_y < 0 允许上方溢出）
                    if board_y >= 0 and self.board[board_y][board_x] is not None:
                        return True
        return False

    def fix_piece(self):
        """将当前方块固定到游戏板上"""
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    board_x = self.current_x + x
                    board_y = self.current_y + y
                    if 0 <= board_y < BOARD_HEIGHT and 0 <= board_x < BOARD_WIDTH:
                        self.board[board_y][board_x] = self.current_color

    def clear_rows(self):
        """检查并清除所有满行，更新分数"""
        rows_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(self.board[y][x] is not None for x in range(BOARD_WIDTH)):
                # 移除该行
                del self.board[y]
                self.board.insert(0, [None] * BOARD_WIDTH)
                rows_cleared += 1
                # 继续检查同一行（因为上面下移了）
            else:
                y -= 1
        # 计分
        if rows_cleared > 0:
            # 简单计分：1行100，2行300，3行500，4行800
            scores = [0, 100, 300, 500, 800]
            self.score += scores[min(rows_cleared, 4)]
            self.update_score()
        self.draw_board()

    # ---------- 绘制 ----------

    def draw_board(self):
        """绘制整个游戏板及当前方块"""
        self.canvas.delete('all')
        # 绘制已固定的方块
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                color = self.board[y][x]
                if color:
                    self.draw_block(x, y, color)
        # 绘制当前方块
        if self.current_shape and not self.game_over:
            for y, row in enumerate(self.current_shape):
                for x, cell in enumerate(row):
                    if cell:
                        board_x = self.current_x + x
                        board_y = self.current_y + y
                        if 0 <= board_y < BOARD_HEIGHT:
                            self.draw_block(board_x, board_y, self.current_color)

    def draw_block(self, x, y, color):
        """在画布上绘制一个方块"""
        x1 = x * BLOCK_SIZE
        y1 = y * BLOCK_SIZE
        x2 = x1 + BLOCK_SIZE
        y2 = y1 + BLOCK_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='gray')

    def draw_preview(self):
        """绘制下一个方块的预览"""
        self.preview_canvas.delete('all')
        if self.next_shape:
            shape = self.next_shape
            color = self.next_color
            rows = len(shape)
            cols = len(shape[0])
            # 居中显示在预览画布中（4x4区域）
            offset_x = (4 - cols) // 2
            offset_y = (4 - rows) // 2
            for y, row in enumerate(shape):
                for x, cell in enumerate(row):
                    if cell:
                        x1 = (offset_x + x) * BLOCK_SIZE
                        y1 = (offset_y + y) * BLOCK_SIZE
                        x2 = x1 + BLOCK_SIZE
                        y2 = y1 + BLOCK_SIZE
                        self.preview_canvas.create_rectangle(x1, y1, x2, y2,
                                                             fill=color, outline='gray')

    def update_score(self):
        self.score_label.config(text=str(self.score))

    # ---------- 主循环 ----------

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    game = Tetris(root)
    game.run()