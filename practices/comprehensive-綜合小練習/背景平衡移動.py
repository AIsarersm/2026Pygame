import pygame
# 模塊初始化
pygame.init()

# 常量，一般用用大寫表示
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
TREE_GROUP_WIDTH = 600
TREE_GROUP_HEIGHT = 100
MOVING_SPEED = 3
FPS = 30

# 變量
# 樹群的初始化x坐標
bg_layer_tree_blit_pos = 0  # 樹群的x方向坐標

# 時鐘對象
clock = pygame.time.Clock()

# 設置主視窗
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# 加載樹圖像
tree1_image = pygame.image.load("./resources/image/tree_resize.png")
# 把六個樹組合為一個surface
bg_layer_tree_group = pygame.Surface((TREE_GROUP_WIDTH, TREE_GROUP_HEIGHT), pygame.SRCALPHA)
for i in range(6):
    bg_layer_tree_group.blit(tree1_image, (i * 100, 15))

# 主循環
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 計算新的樹群位置x
    bg_layer_tree_blit_pos -= MOVING_SPEED
    if bg_layer_tree_blit_pos <= -bg_layer_tree_group.get_width():
        bg_layer_tree_blit_pos = 0

    # 背景填色
    window.fill((192, 192, 255))
    # 畫地面
    pygame.draw.rect(window, (64, 128, 64), (0, 250, 600, 150))
    # 畫樹群1
    window.blit(bg_layer_tree_group, (bg_layer_tree_blit_pos, 150))
    # 畫樹群2
    window.blit(bg_layer_tree_group, (bg_layer_tree_blit_pos + bg_layer_tree_group.get_width(), 150))
    # 只需要兩個樹群就可以連接上整個畫面，不然要繼續blit()

    # 更新
    pygame.display.update()

pygame.quit()
