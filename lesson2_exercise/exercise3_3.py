import pygame
import time

# 模塊初始化
pygame.init()
# 建立主視窗
main_surface = pygame.display.set_mode(size=(600, 400))
# 建立草地對應的矩形
tree_ground_rect = pygame.rect.Rect(0, 250, 600, 150)
# 樹立多棵樹所在surface
bg_layer_tree_group = pygame.Surface((600, 180), pygame.SRCALPHA)
for i in range(6):
    pygame.draw.rect(bg_layer_tree_group, (95, 55, 32), (60+i*100, 120, 26, 60))
    pygame.draw.polygon(bg_layer_tree_group, (116, 186, 26), [(34+i*100, 130), (112+i*100, 130), (73+i*100, 85)], 0)
    pygame.draw.polygon(bg_layer_tree_group, (52, 151, 58), [(40+i*100, 100), (106+i*100, 100), (73+i*100, 60)], 0)

# 建立tank surface
tank_surf = pygame.Surface((60, 40), pygame.SRCALPHA)
pygame.draw.rect(tank_surf, (0, 96, 0), (0, 00, 50, 40))
pygame.draw.rect(tank_surf, (0, 128, 0), (10, 10, 30, 20))
pygame.draw.rect(tank_surf, (32, 32, 96), (20, 16, 40, 8))

# 創建文字對象
sysFont_obj = pygame.font.SysFont("calibri", 26)
# 設置文字對象帶有下底線
sysFont_obj.underline = True
# 設置文字對象帶有粗體
sysFont_obj.bold = True
# 使用這字體生成文字surface
text_surface = sysFont_obj.render("Your mask is: 10", True, (0, 0, 100), (0, 100, 0))

running = True
speed = 3
y_pos = 300
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event type
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print("上鍵被按下")
        y_pos -= speed
    if keys[pygame.K_DOWN]:
        print("下鍵被按下")
        y_pos += speed

    main_surface.fill((192, 192, 255))
    pygame.draw.rect(main_surface, (64, 128, 64), tree_ground_rect)
    main_surface.blit(bg_layer_tree_group, (0, 70))
    main_surface.blit(tank_surf, (20, y_pos))
    main_surface.blit(text_surface, (430, 0))

    pygame.display.update()
    time.sleep(0.02)
pygame.quit()
