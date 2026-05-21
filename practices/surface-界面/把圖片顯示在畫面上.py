import pygame
import time

# 初始化pygame所有模組
pygame.init()
# 創建界面，大小為480x640
main_surface = pygame.display.set_mode(size=(480, 640))
# 加載圖片
image = pygame.image.load("./resources/image/bluebird-midflap.png")
# 把圖片放在界面的某個位置
main_surface.blit(image, (240, 360))
# 更新界面
pygame.display.update()
# 保留界面5s
time.sleep(5)
# 離開
pygame.quit()
