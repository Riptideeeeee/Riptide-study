import pygame
import sys
import random
from pygame.sprite import Sprite

# ===== 初始化 =====
pygame.init()

# ===== 常量 =====
WIDTH = 600
HEIGHT = 700
FPS = 60

# ===== 颜色 =====
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)

# ===== 窗口 =====
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("太空射击")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)


# ===== 玩家 =====
class Player(Sprite):
    def __init__(self):
        # TODO: 创建飞船（三角形或图片）
        super().__init__()
        pass

    def update(self):
        # TODO: 键盘控制 + 边界限制
        pass

    def shoot(self):
        # TODO: 创建子弹并加入组
        pass


# ===== 子弹 =====
class Bullet(Sprite):
    def __init__(self, x, y):
        # TODO: 创建子弹，从飞船位置发射
        pass

    def update(self):
        # TODO: 向上飞行，超出屏幕消失
        pass


# ===== 敌人 =====
class Enemy(Sprite):
    def __init__(self):
        # TODO: 从顶部随机位置生成
        pass

    def update(self):
        # TODO: 下落，到底部消失
        pass


# ===== 游戏管理 =====
class Game:
    def __init__(self):
        # TODO: 初始化精灵组、分数、生命值
        pass

    def spawn_enemy(self):
        # TODO: 生成敌人（限制数量 5-8 个）
        pass

    def check_collisions(self):
        # TODO: 子弹vs敌人 → 加分
        # TODO: 玩家vs敌人 → 扣命
        pass

    def reset(self):
        # TODO: 重置游戏
        pass

    def draw_ui(self):
        # TODO: 显示分数和生命值
        pass

    def draw_gameover(self):
        # TODO: 显示游戏结束画面
        pass

    def run(self):
        running = True
        while running:
            # ---- 事件 ----
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # TODO: 发射子弹
                        pass
                    if event.key == pygame.K_r:
                        # TODO: 重新开始
                        pass

            # ---- 更新 ----
            if self.game_state == "playing":
                # TODO: 更新所有精灵
                # TODO: 生成敌人
                # TODO: 碰撞检测
                pass

            # ---- 绘制 ----
            screen.fill(BLACK)
            # TODO: 绘制所有精灵
            # TODO: 绘制UI
            # TODO: 游戏结束画面

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()