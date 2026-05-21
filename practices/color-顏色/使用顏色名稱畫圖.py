import pygame
import time

# 模塊初始化
pygame.init()
# 建立主視窗
main_surface = pygame.display.set_mode(size=(600, 400))
# 主視窗填上紫色
color_background = pygame.color.Color("thistle3")
main_surface.fill(color_background)
# 建立草地對應的矩形
tree_ground_rect = pygame.rect.Rect(0, 250, 600, 150)
pygame.draw.rect(main_surface, (64, 128, 64), tree_ground_rect)
# 定義顏色:
color_chocolate4 = pygame.color.Color("chocolate4")
color_green_1 = pygame.color.Color("chartreuse3")
color_green_2 = pygame.color.Color("chartreuse4")
# 通過for畫多棵樹
for i in range(6):
    pygame.draw.rect(main_surface, color_chocolate4, (60 + i*100, 190, 26, 60))
    pygame.draw.polygon(main_surface, color_green_1, [(34 + i*100, 200), (112 + i*100, 200), (73 + i*100, 155)], 0)
    pygame.draw.polygon(main_surface, color_green_2, [(40 + i*100, 170), (106 + i*100, 170), (73 + i*100, 120)], 0)

pygame.display.update()
time.sleep(5)
pygame.quit()
