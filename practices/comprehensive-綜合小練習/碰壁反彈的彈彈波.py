import pygame
# 模組初始化
pygame.init()
# 設置主視窗
main_window = pygame.display.set_mode((600, 400))
# 設置時鐘對象
clock = pygame.time.Clock()
# 設置遊戲參數
running = True  # 視窗是否關閉的變量
start = False  # 遊戲是否開始的變量

# 設置球的參數
circle_radius = 10  # 球的半徑
circle_pos_x = 200  # 用此變量代表球的x坐標，初始化為200
circle_pos_y = 200  # 用此變量代表球的y坐標，初始化為200
speed_x = 3  # 球的x方向速度
speed_y = 3  # 球的y方向速度

# 設置矩形的範圍
bounds = pygame.Rect(50, 50, 500, 300)

# 主循環開始
while running:
    clock.tick(120)  # 120fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 當檢測到按下space時，start變為True，遊戲開始
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True

    if start:  # 只有按下了space時，if才為True，才會觸發遊戲動畫
        circle_pos_y += speed_y  # y方向每秒更新位置
        circle_pos_x += speed_x  # x方向每秒更新位置

        if circle_pos_x - circle_radius < bounds.left or circle_pos_x + circle_radius > bounds.right:
            speed_x *= -1
        if circle_pos_y - circle_radius < bounds.top or circle_pos_y + circle_radius > bounds.bottom:
            speed_y *= -1

        # speed_y += 0.1  # 加上重力

    # 更新畫面
    main_window.fill((0, 0, 0))
    pygame.draw.rect(main_window, (255, 0, 0), bounds, 1)
    pygame.draw.circle(main_window, (44, 176, 55), (circle_pos_x, circle_pos_y), circle_radius)
    pygame.display.update()
