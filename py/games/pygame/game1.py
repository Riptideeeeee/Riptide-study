import pygame
import sys
import random

# ===== 初始化 =====
pygame.init()

# ===== 窗口 =====
WIDTH = 600
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("接住星星")

# ===== 帧率 =====
clock = pygame.time.Clock()

# ===== 玩家（用矩形代替） =====
player_x = 250
player_y = 430
player_width = 60
player_height = 30
player_speed = 6
score = 0
# ===== 星星（掉落的物体） =====
class star:
    def __init__(self,num,x,y):
        self.num = num
        self.x = x
        self.y = y
    def move(self):
        # ---- 星星下落 ----
        self.y += star_speed



        # ---- 星星掉到屏幕底部 ----
        if self.y > HEIGHT:
            # 没接到，重置
            self.x = random.randint(0, WIDTH - star_size)
            self.y = 0

    def draw(self):
        # ✅ 正确：x 和 y 分别用
        pygame.draw.circle(screen, (255, 215, 0), (self.x + star_size // 2, self.y + star_size // 2), star_size // 2)

    def text(self):
        if (player_x < self.x + star_size and
                player_x + player_width > self.x and
                player_y < self.y + star_size and
                player_y + player_height > self.y):
            # 接到了！星星重置到顶部
            self.x = random.randint(0, WIDTH - star_size)
            self.y = 0
            return 1
        else:
            return 0

star_size = 30
star_speed = 3
star_y = 0
star_x = random.randint(0, WIDTH - 30)
star0=star(0,star_x,star_y)
star_x = random.randint(0, WIDTH - 30)
star1=star(1,star_x,star_y)
star_x = random.randint(0, WIDTH - 30)
star2=star(2,star_x,star_y)
# ===== 计分 =====
score = 0
font = pygame.font.Font(None, 36)

# ===== 游戏主循环 =====
running = True
while running:
    # ---- 事件处理 ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- 玩家移动 ----
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    screen.fill((30, 30, 40))
    star0.move()
    star1.move()
    star2.move()
    star0.draw()
    star1.draw()
    star2.draw()
    # ---- 绘制 ----


    # 画玩家（蓝色方块）
    pygame.draw.rect(screen, (0, 150, 255), (player_x, player_y, player_width, player_height))
    score+=star0.text()
    score+=star1.text()
    score+=star2.text()
    # 显示分数
    score_text = font.render(f"分数: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # ---- 更新画面 ----
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()