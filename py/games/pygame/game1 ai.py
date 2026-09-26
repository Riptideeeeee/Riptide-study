# ===== 游戏状态 =====
# 1. 游戏中：正常运行
# 2. 游戏结束：显示 "游戏结束！按 R 重新开始"
# 3. 暂停（选做）：按 P 暂停/继续
import pygame
import sys
import random
from pygame.sprite import Sprite

from 卖水果 import apple, grape
from 卖水果2 import fruits

# ===== 初始化 =====
pygame.init()

# ===== 常量 =====
WIDTH = 600
HEIGHT = 700
FPS = 60

# ===== 颜色 =====
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# ===== 窗口 =====
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("接水果游戏")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)


# ===== 玩家（篮子）=====
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - 40
        self.rect.y = HEIGHT - 80
        self.speed = 8

    def update(self):
        # TODO: 键盘控制左右移动
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT] and self.rect.x < WIDTH -80 :
            self.rect.x += self.speed
        pass


# ===== 掉落物基类 =====
class FallingObject(Sprite):
    def __init__(self, color, size, speed, points):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - size)
        self.rect.y = random.randint(-100, -size)
        self.speed = speed
        self.points = points

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.reset()

    def reset(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -self.rect.height)


# ===== 水果类（继承掉落物）=====
class Fruit(FallingObject):
    def __init__(self, color, size, speed, points):
        super().__init__(color, size, speed, points)


# ===== 炸弹类（继承掉落物）=====
class Bomb(FallingObject):
    def __init__(self,color, size, speed, points):
        # TODO: 黑色炸弹，大小30，速度3，分数0
        super().__init__(color, size, speed, points)
        self.color = BLACK
        self.size = 30
        self.speed = 3
        self.points = 0
        pass


# ===== 游戏管理类 =====
class Game:
    def __init__(self):
        self.score = 0
        self.running = True
        self.game_over = False

        # 创建精灵组
        self.all_sprites = pygame.sprite.Group()
        self.fruits = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()

        # 创建玩家
        self.player = Player()
        self.all_sprites.add(self.player)

        # 创建初始掉落物（3个水果 + 1个炸弹）
        # TODO: 创建水果和炸弹并添加到组
        apple = Fruit(RED, 30, 3, 10)
        grape = Fruit(PURPLE, 30, 3, 10)
        orange = Fruit(ORANGE, 30, 3, 10)
        self.fruits.add(apple, grape, orange)
        self.all_sprites.add(self.fruits)
    def spawn_fruit(self):
        rand=random.randint(1,4)
        if rand == 1:
            apple.update()
        elif rand == 2:
            grape.update()
        elif rand == 3:
            orange.update()
        else:
            pass
        """随机生成一个水果"""
        # TODO: 随机选择水果类型（绿/橙/紫），创建并加入组
        pass

    def spawn_bomb(self):
        """生成一个炸弹"""
        pass

    def check_collisions(self):
        """检测碰撞"""
        # TODO: 检测玩家和水果碰撞 → 加分，水果重置
        # TODO: 检测玩家和炸弹碰撞 → 游戏结束
        pass

    def reset(self):
        """重新开始游戏"""
        self.score = 0
        self.game_over = False
        # TODO: 重置所有物体
        pass

    def draw_ui(self):
        """绘制分数和提示"""
        pass

    def run(self):
        """游戏主循环"""
        while self.running:
            # ---- 事件处理 ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r and self.game_over:
                        self.reset()

            # ---- 更新 ----
            if not self.game_over:
                self.all_sprites.update()
                self.check_collisions()

            # ---- 绘制 ----
            screen.fill(WHITE)
            self.all_sprites.draw(screen)
            self.draw_ui()

            # ---- 更新画面 ----
            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()


# ===== 启动游戏 =====
if __name__ == "__main__":
    game = Game()
    game.run()