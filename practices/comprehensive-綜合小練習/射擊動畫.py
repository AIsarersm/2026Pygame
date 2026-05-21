import pygame
# 模塊初始化
pygame.init()

# 創建主視窗
main_window = pygame.display.set_mode((500, 200))
# 創建坦克surface對象
tank_surf = pygame.Surface((60, 40), pygame.SRCALPHA)
pygame.draw.rect(tank_surf, (0, 96, 0), (0, 00, 50, 40))
pygame.draw.rect(tank_surf, (0, 128, 0), (10, 10, 30, 20))
pygame.draw.rect(tank_surf, (32, 32, 96), (20, 16, 40, 8))
# tank_rect = tank_surf.get_rect(midleft=(20, 100 - 40//2))  # 直接計算位置
tank_rect = tank_surf.get_rect(midleft=(20, main_window.get_height() // 2))  # 指定坦克的左中點位置

# 創建子彈surface對象
bullet_surf = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(bullet_surf, (64, 64, 62), (5, 5), 5)

# 控制子彈參數的變量
bullet_list = []  # 存放子彈的列表
max_bullets = 10  # 控制最多在畫面中顯示的子彈數
next_bullet_time = 0  # 記錄發射時間的變量
BULLET_DELTA_TIME = 100  # 控制相鄰子彈間發射的最小時間間隔

#  遊戲常量
X_SPEED = 5

# 時鐘clock對象，主要用於fps管理
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # 希望按實space鍵也一直發子彈，因此用函數方法，而不是用event
    if keys[pygame.K_SPACE]:
        if len(bullet_list) < max_bullets and current_time >= next_bullet_time:
            next_bullet_time = current_time + BULLET_DELTA_TIME  # 控制子彈發射間隔
            bullet_list.insert(0, [tank_rect.midright[0], tank_rect.midright[1] - bullet_surf.get_height() // 2])  # 保存tank的右中心點作為子彈的左中心點 [(x1,y1),(x2,y2)......]

    for i in range(len(bullet_list)):  # 索引遍歷
        bullet_list[i][0] += X_SPEED # 每個幀向右移5pix
        if bullet_list[i][0] > main_window.get_width():  # 超過畫面
            del bullet_list[i:]  # 因為list是按時間順序insert，所以將出界及其以後的全部del
            break

    main_window.fill((224, 192, 160))
    main_window.blit(tank_surf, (tank_rect.x, tank_rect.y))
    for bullet_pos in bullet_list:  # 直接遍歷
        main_window.blit(bullet_surf, (bullet_pos[0], bullet_pos[1]))  # -5是向上對準槍口

    pygame.display.update()

pygame.quit()
