import pygame
# 模塊初始化
pygame.init()

# 常量，一般用用大寫表示
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
TREE_GROUP_WIDTH = 600
TREE_GROUP_HEIGHT = 100
MOVING_SPEED = 3
FPS = 60

# 變量
# 設置主視窗
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 加載樹圖像
tree1_image = pygame.image.load("./resources/image/tree_resize.png")
# 把六個樹組合為一個surface
bg_layer_tree_group = pygame.Surface((TREE_GROUP_WIDTH, TREE_GROUP_HEIGHT), pygame.SRCALPHA)
for i in range(6):
    bg_layer_tree_group.blit(tree1_image, (i * 100, 15))
# 樹群的初始化x坐標
bg_layer_tree_blit_pos = 0  # 樹群的x方向坐標

# 創建坦克surface對象
tank_surf = pygame.Surface((60, 40), pygame.SRCALPHA)
pygame.draw.rect(tank_surf, (0, 96, 0), (0, 00, 50, 40))
pygame.draw.rect(tank_surf, (0, 128, 0), (10, 10, 30, 20))
pygame.draw.rect(tank_surf, (32, 32, 96), (20, 16, 40, 8))
tank_rect = tank_surf.get_rect(midleft=(20, 330))  # 指定坦克的左中點位置

# 創建子彈surface對象
bullet_surf = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(bullet_surf, (64, 64, 62), (5, 5), 5)

# 時鐘對象
clock = pygame.time.Clock()

# 控制子彈參數的變量
bullet_list = []  # 存放子彈的列表
max_bullets = 100  # 控制最多在畫面中顯示的子彈數
next_bullet_time = 0  # 記錄發射時間的變量
BULLET_DELTA_TIME = 150  # 控制相鄰子彈間發射的最小時間間隔
#  遊戲常量
X_SPEED = 5

# 主循環
running = True
while running:
    clock.tick(FPS)
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
        if bullet_list[i][0] > window.get_width():  # 超過畫面
            del bullet_list[i:]  # 因為list是按時間順序insert，所以將出界及其以後的全部del
            break

    # 計算新的樹群位置x
    bg_layer_tree_blit_pos -= MOVING_SPEED
    if bg_layer_tree_blit_pos <= -bg_layer_tree_group.get_width():
        bg_layer_tree_blit_pos = 0
    # 背景填色
    window.fill((192, 192, 255))
    # 畫地面
    pygame.draw.rect(window, (64, 128, 64), (0, 250, 600, 150))

    # 畫樹群1
    window.blit(bg_layer_tree_group, (bg_layer_tree_blit_pos + bg_layer_tree_group.get_width(), 150))
    # 畫樹群2
    window.blit(bg_layer_tree_group, (bg_layer_tree_blit_pos, 150))
    window.blit(tank_surf, (tank_rect.x, tank_rect.y))
    for bullet_pos in bullet_list:  # 直接遍歷
        window.blit(bullet_surf, (bullet_pos[0], bullet_pos[1]))  # -5是向上對準槍口
    # 更新
    pygame.display.update()

pygame.quit()
