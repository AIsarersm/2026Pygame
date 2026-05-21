import pygame
import time

# 模塊初始化
pygame.init()
# 建立主畫面
main_surface = pygame.display.set_mode(size=(600,400))
# 創建文字對象
sysFont_obj = pygame.font.SysFont("calibri", 26)
# 設置文字對象帶有下底線
sysFont_obj.underline = True
# 設置文字對象帶有粗體
sysFont_obj.bold = True
# 使用這字體生成文字surface
text_surface = sysFont_obj.render("Your mask is: 10", True, (0, 0, 100), (0, 100, 0))
# 在main surface上blit出這一surface
main_surface.blit(text_surface, (430, 0))

pygame.display.update()
time.sleep(5)

pygame.quit()
