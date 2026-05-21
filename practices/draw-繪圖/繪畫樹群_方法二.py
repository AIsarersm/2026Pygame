import pygame
import time

# 模塊初始化
pygame.init()
# 建立主視窗
main_surface = pygame.display.set_mode(size=(600, 400))
# 主視窗填上紫色
main_surface.fill((192, 192, 255))
# 建立草地對應的矩形
tree_ground_rect = pygame.rect.Rect(0, 250, 600, 150)
pygame.draw.rect(main_surface, (64, 128, 64), tree_ground_rect)
# 通過for畫多棵樹
for i in range(6):
    pygame.draw.rect(main_surface, (95, 55, 32), (60 + i*100, 190, 26, 60))
    pygame.draw.polygon(main_surface, (116, 186, 26), [(34 + i*100, 200), (112 + i*100, 200), (73 + i*100, 155)], 0)
    pygame.draw.polygon(main_surface, (52, 151, 58), [(40 + i*100, 170), (106 + i*100, 170), (73 + i*100, 120)], 0)

pygame.display.update()
time.sleep(5)
pygame.quit()
