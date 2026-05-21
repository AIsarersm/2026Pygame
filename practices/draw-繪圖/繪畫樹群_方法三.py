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
# 通過surface+for 畫多棵樹
bg_layer_tree_group = pygame.Surface((600, 180), pygame.SRCALPHA)
for i in range(6):
    pygame.draw.rect(bg_layer_tree_group, (95, 55, 32), (60+i*100, 120, 26, 60))
    pygame.draw.polygon(bg_layer_tree_group, (116, 186, 26), [(34+i*100, 130), (112+i*100, 130), (73+i*100, 85)], 0)
    pygame.draw.polygon(bg_layer_tree_group, (52, 151, 58), [(40+i*100, 100), (106+i*100, 100), (73+i*100, 60)], 0)

main_surface.blit(bg_layer_tree_group, (0, 70))
pygame.display.update()
time.sleep(5)
pygame.quit()
