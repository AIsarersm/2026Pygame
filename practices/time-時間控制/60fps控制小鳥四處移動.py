import pygame
import time

# 模組初始化
pygame.init()
# 創建主視窗
main_window = pygame.display.set_mode((320, 320))
# 加載小鳥圖像，並生成image_obj這個surface對象
image_obj = pygame.image.load("./resources/image/bluebird-downflap.png")
# 設置clock對象
clock = pygame.time.Clock()
# 小鳥坐標變量
x_pos = 0
y_pos = 0
speed = 1
# 主循環開始
running = True
while running:
    for event in pygame.event.get():
        # 收到的事件是quit，代表窗口被關
        if event.type == pygame.QUIT:
            running = False
    # 把背景填為黑色
    main_window.fill((0, 0, 0))
    # 通過函數主動去獲取keyboard的按下狀況
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("左鍵被按下")
        x_pos -= speed  # 位置控制
    if keys[pygame.K_RIGHT]:
        print("右鍵被按下")
        x_pos += speed  # 位置控制
    if keys[pygame.K_UP]:
        print("上鍵被按下")
        y_pos -= speed  # 位置控制
    if keys[pygame.K_DOWN]:
        print("下鍵被按下")
        y_pos += speed  # 位置控制
    main_window.blit(image_obj, (x_pos, y_pos))  # 把小鳥surface畫在對應的位置上
    pygame.display.update()

    clock.tick(60)  # 60fps
pygame.quit()
