import pygame

# 模組初始化
pygame.init()
# 創建主視窗
screen = pygame.display.set_mode((400, 400))
# 創建時鐘對象
clock = pygame.time.Clock()
# 創建兩個block，一個是player，一個是障礙物
player_size = (20, 20)  # player rect的寬和高
player_pos = (0, 0)  # player rect的初始位置
player = pygame.Rect((player_pos[0], player_pos[1], player_size[0], player_size[1]))
block = pygame.Rect(150, 330, 20, 20)
# 地面Y坐標
ground_y = 350
# player的x,y速度
x_speed = 0
y_speed = 0


def collide_check(player, block, speed_x, speed_y):
    if player.colliderect(block):
        if speed_y > 0:  # 發生碰撞時仍有speed_y，代表正在站上block上
            player.bottom = block.top

    # x方向判斷
    player.x += speed_x
    if player.colliderect(block):
        if speed_x > 0:
            player.right = block.left
        if speed_x < 0:
            player.left = block.right


# 主循環
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                if player.bottom == ground_y or player.bottom == block.top:  # 貼在地面時才可以觸發跳起
                    y_speed = -5  # 跳起就是把速度進行突變

    keys = pygame.key.get_pressed()
    move_left = keys[pygame.K_LEFT]  # 判斷左邊是否按下，返回True/False
    move_right = keys[pygame.K_RIGHT]  # 判斷右邊是否按下，返回True/False
    x_speed = (move_right - move_left) * 2.5  # 簡單的方向控制方法
    y_speed += 0.2
    player.y += y_speed
    collide_check(player, block, x_speed, y_speed)

    # 使player保持在地面以上
    if player.bottom >= ground_y:
        player.bottom = ground_y
        y_speed = 0

    # 畫背景
    screen.fill((255, 255, 255))
    # 畫地面
    pygame.draw.rect(screen, "gray", (0, ground_y, 400, 400 - ground_y))
    # 畫player
    pygame.draw.rect(screen, (255, 0, 0), player)
    # 畫block
    pygame.draw.rect(screen, (0, 0, 0), block)
    pygame.display.update()

pygame.quit()
