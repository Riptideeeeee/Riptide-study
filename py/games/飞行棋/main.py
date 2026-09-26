import pygame
import sys
import random
from pygame.sprite import Sprite
import ctypes

gamesize=900
pygame.init()
chessboard = pygame.display.set_mode((gamesize, gamesize))
pygame.display.set_caption("飞行棋")
clock = pygame.time.Clock()
background=pygame.image.load("chessboard.png")
background=pygame.transform.scale(background, (gamesize, gamesize))
ctypes.windll.imm32.ImmDisableIME(0)
def dice():
    return random.randint(1,6)
class Plane(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)  # 透明背景
        pygame.draw.circle(self.image, (255, 0, 0), (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_s]:
            self.rect.y += 10
        if keys[pygame.K_w]:
            self.rect.y -= 10
class PlayerPlane(Plane):
    def __init__(self):
        super().__init__()
        self.rect.x = 100
        self.rect.y = 100
    def update(self):
        super().update()
class EnemyPlane(Plane):
    def __init__(self):
        pass
    def move(self):
        pass
def main():
    playerplane=PlayerPlane()
    all_planes=pygame.sprite.Group()
    all_planes.add(playerplane)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 获取点击位置（元组 (x, y)）
                mouse_x, mouse_y = event.pos
                print(f"鼠标点击位置: ({mouse_x}, {mouse_y})")
        chessboard.blit(background, (0,0))
        # all_planes.update()
        # all_planes.draw(chessboard)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()