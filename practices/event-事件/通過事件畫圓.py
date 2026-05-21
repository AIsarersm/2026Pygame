import pygame
import time
# 導入random模組
import random

# 模組初始化
pygame.init()
# 創建主視窗
main_surface = pygame.display.set_mode(size=(600, 400))
# 主循環開始
running = True
while running:
    for event in pygame.event.get():
        # 收到的事件是quit，代表窗口被關
        if event.type == pygame.QUIT:
            running = False
        # 收到的事件是MOUSEBUTTONDOWN，代表鼠標某個鍵被按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # 獲取按下點的鼠標坐標
            r = random.randint(0, 255)  # 通過random中的函數產生0-255間的整數
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            pygame.draw.circle(main_surface, (r, g, b), mouse_pos, 20, 0)  # 繪畫circle
            pygame.display.update()

    time.sleep(0.05)  # 暫時通過time sleep控制FPS，这里fps=20

pygame.quit()
