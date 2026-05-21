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
# 畫樹1
pygame.draw.rect(main_surface, (95, 55, 32), (60, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(34, 200), (112, 200), (73, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(40, 170), (106, 170), (73, 120)], 0)
# 畫樹2
pygame.draw.rect(main_surface, (95, 55, 32), (160, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(134, 200), (212, 200), (173, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(140, 170), (206, 170), (173, 120)], 0)
# 畫樹3
pygame.draw.rect(main_surface, (95, 55, 32), (260, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(234, 200), (312, 200), (273, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(240, 170), (306, 170), (273, 120)], 0)
# 畫樹4
pygame.draw.rect(main_surface, (95, 55, 32), (360, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(334, 200), (412, 200), (373, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(340, 170), (406, 170), (373, 120)], 0)
# 畫樹5
pygame.draw.rect(main_surface, (95, 55, 32), (460, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(434, 200), (512, 200), (473, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(440, 170), (506, 170), (473, 120)], 0)
# 畫樹6
pygame.draw.rect(main_surface, (95, 55, 32), (560, 190, 26, 60))
pygame.draw.polygon(main_surface, (116, 186, 26), [(534, 200), (612, 200), (573, 155)], 0)
pygame.draw.polygon(main_surface, (52, 151, 58), [(540, 170), (606, 170), (573, 120)], 0)

pygame.display.update()
time.sleep(5)
pygame.quit()
