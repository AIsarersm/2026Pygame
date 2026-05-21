import pygame
import time

# 模塊初始化
pygame.init()
# 創建主視窗
gameDisplay = pygame.display.set_mode((600, 600))
# 初始化主視窗背景
gameDisplay.fill((0, 0, 255))
# 變量定義
running = True
clicked = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠標按下時觸發
            clicked = True
            lastx, lasty = event.pos  # 記錄按下時的坐標
        if event.type == pygame.MOUSEBUTTONUP:  # 鼠標松開時觸發
            clicked = False
        if event.type == pygame.MOUSEMOTION:  # 鼠標移動時觸發
            x, y = event.pos   # 記錄移動時的坐標
        if event.type == pygame.QUIT:
            running = False

    if clicked:
        pygame.draw.circle(gameDisplay, (255, 0, 0), (lastx, lasty), 5)
        pygame.draw.line(gameDisplay, (255, 0, 0), (lastx, lasty), (x, y), 10)
        pygame.draw.circle(gameDisplay, (255, 0, 0), (x, y), 5)
        lastx, lasty = x, y

    pygame.display.update()
    time.sleep(0.02)

pygame.quit()
