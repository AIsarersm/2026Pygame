import pygame
import time

# 模組初始化
pygame.init()
# 建立主畫面
main_surface = pygame.display.set_mode(size=(600, 400))

# 主循環開始
running = True
while running:
    for event in pygame.event.get():
        # 收到的事件是quit，代表窗口被關
        if event.type == pygame.QUIT:
            running = False
        # 收到的事件是KEYDOWN，代表在KEYBOARD按鍵被按下
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # 判斷被按下的按鍵是否為a鍵
                print("1")
            elif event.key == pygame.K_b:  # 判斷被按下的按鍵是否為b鍵
                print("2")
            elif event.key == pygame.K_c:   # 判斷被按下的按鍵是否為c鍵
                print("3")
            else:
                print("0")   # 其余則輸出0

    time.sleep(0.05)

pygame.quit()
