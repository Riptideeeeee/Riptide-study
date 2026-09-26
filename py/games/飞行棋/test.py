import pygame
import sys
import math

# 初始化
pygame.init()
WIN_SIZE = 800
MARGIN = 50
screen = pygame.display.set_mode((WIN_SIZE, WIN_SIZE), pygame.RESIZABLE)
pygame.display.set_caption("飞行棋棋盘 - 坐标预览")
clock = pygame.time.Clock()

# 颜色定义
COLORS = {
    'path': (180, 180, 180),
    'runway': [(255, 50, 50), (255, 255, 50), (50, 255, 50), (50, 150, 255)],
    'start': [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)],
    'park': [(200, 50, 50), (200, 200, 50), (50, 200, 50), (50, 100, 200)]
}

# 计算基本尺寸
effective = WIN_SIZE - 2 * MARGIN
step = effective / 12  # 13个点有12个间隔

# 四个角坐标（左上、右上、右下、左下）
corners = [
    (MARGIN, MARGIN),
    (WIN_SIZE - MARGIN, MARGIN),
    (WIN_SIZE - MARGIN, WIN_SIZE - MARGIN),
    (MARGIN, WIN_SIZE - MARGIN)
]
center = (WIN_SIZE / 2, WIN_SIZE / 2)

# ---- 1. 生成外围路径点（52个点，顺时针，角点重复） ----
path_points = []
for i in range(4):
    start = corners[i]
    end = corners[(i + 1) % 4]
    for j in range(13):
        t = j / 12.0
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        path_points.append((x, y))

# ---- 2. 生成跑道点（每个角向中心延伸5个点，包含起点） ----
runway_points = []
for idx, corner in enumerate(corners):
    # 方向向量：从角指向中心
    dx = center[0] - corner[0]
    dy = center[1] - corner[1]
    # 只走一半距离，避免跑道交叉
    for j in range(5):
        t = j / 4.0
        x = corner[0] + dx * t * 0.5
        y = corner[1] + dy * t * 0.5
        runway_points.append((x, y, idx))  # idx表示玩家颜色

# ---- 3. 起飞处：四个角点 ----
start_points = corners  # 列表

# ---- 4. 停机处：每个角内部4个点 ----
park_points = []
offset = 20
for idx, corner in enumerate(corners):
    # 向内部偏移（朝向中心）
    dx = center[0] - corner[0]
    dy = center[1] - corner[1]
    # 归一化
    length = math.hypot(dx, dy)
    if length != 0:
        dx /= length
        dy /= length
    # 四个偏移方向：沿法向和切向组合（形成2x2网格）
    # 法向（朝向中心）和切向（顺时针垂直）
    nx, ny = dx, dy
    tx, ty = -dy, dx  # 顺时针旋转90度
    # 四个点：中心偏移 ±offset*nx ±offset*tx
    for sx in (-1, 1):
        for sy in (-1, 1):
            px = corner[0] + nx * offset * 0.6 + tx * offset * 0.4 * sx
            py = corner[1] + ny * offset * 0.6 + ty * offset * 0.4 * sy
            park_points.append((px, py, idx))

# ---------- 主循环 ----------
running = True
while running:
    # 获取当前窗口尺寸（支持缩放）
    win_w, win_h = screen.get_size()
    # 清屏
    screen.fill((30, 30, 30))

    # 计算缩放比例（以原始尺寸为基准）
    scale_x = win_w / WIN_SIZE
    scale_y = win_h / WIN_SIZE

    def scale_point(x, y):
        return (int(x * scale_x), int(y * scale_y))

    # 绘制外围路径（灰色）
    for x, y in path_points:
        sx, sy = scale_point(x, y)
        pygame.draw.circle(screen, COLORS['path'], (sx, sy), 6)

    # 绘制跑道（彩色）
    for x, y, idx in runway_points:
        sx, sy = scale_point(x, y)
        pygame.draw.circle(screen, COLORS['runway'][idx], (sx, sy), 8)

    # 绘制起飞处（大圆带边框）
    for idx, (x, y) in enumerate(start_points):
        sx, sy = scale_point(x, y)
        pygame.draw.circle(screen, COLORS['start'][idx], (sx, sy), 12)
        pygame.draw.circle(screen, (255, 255, 255), (sx, sy), 12, 2)  # 白边

    # 绘制停机处（小圆）
    for x, y, idx in park_points:
        sx, sy = scale_point(x, y)
        pygame.draw.circle(screen, COLORS['park'][idx], (sx, sy), 5)

    # 绘制中心区域提示
    font = pygame.font.Font(None, 30)
    text = font.render("飞行棋棋盘预览", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.VIDEORESIZE:
            # 窗口大小改变时自动适应
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

pygame.quit()