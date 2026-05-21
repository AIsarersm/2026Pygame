import pygame
import time
# 模組初始化
pygame.init()
# 創建主視窗
main_surface = pygame.display.set_mode((600, 600))
# 創建背景色
background_color = pygame.color.Color("darkolivegreen2")
main_surface.fill(background_color)
# 加載小鳥
source_surface = pygame.image.load("./resources/image/bluebird-downflap.png")
# 設置clock對象
clock = pygame.time.Clock()
# 設置音效對象
wingAudio = './resources/sound/wing.wav'
wing_sound_obj = pygame.mixer.Sound(wingAudio)
# 設置常量
GRAVITY = 0.3
SPEED_CONST = 6.5

# 設置變量
x_cen = 300
y_cen = 300
bird_speed = 0
running = True

while running:
    clock.tick(60)  # 60 fps

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -SPEED_CONST  # 如果按space後，強制小鳥轉向某個特定速度
                wing_sound_obj.play()
    main_surface.fill(background_color)  # 填背景色
    bird_speed += GRAVITY  # 小鳥會隨時間speed愈來愈快
    rotate_image = pygame.transform.rotate(source_surface, -3 * bird_speed)  # 轉到最新的角度，-3是一個調節比例
    y_cen += bird_speed
    rotate_image_rect = rotate_image.get_rect(center=(x_cen, y_cen))  # 保持中心點不變，反推旋轉後的rect，目的是獲取旋轉後的左上角點
    main_surface.blit(rotate_image, (rotate_image_rect.x, rotate_image_rect.y))  # blit()畫的是左上角點
    pygame.display.update()

pygame.quit()
