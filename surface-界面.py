import pygame
import time

pygame.init()
main_surface = pygame.display.set_mode((480, 640))

# 2. 把surface obj填滿同一種顏色，fill(color, rect=None, special_flags=0) -> Rect
main_surface.fill((255, 0, 0))
pygame.display.update()
time.sleep(2)

# 3. 把一個surface對象放在另一個surface對象上
# blit(source, dest, area=None, special_flags=0) -> Rect
# source -> 目標surface對象
# dest -> 把目標放在源界面的哪里，(x,y)
source_surface = pygame.image.load("./resources/image/bluebird-downflap.png")
# source_surface = source_surface.convert_alpha()  # 一般來說若想要透明底，都需要為把image的format改為帶alpha
main_surface.blit(source_surface, (240, 320))
pygame.display.update()
time.sleep(2)

# 4. 把surface對象的格式添加alpha通道，為了顯示透明底的圖像
source_surface_2 = pygame.image.load("./resources/image/cat.jpg")
source_surface_2_covert = source_surface_2.convert_alpha()  # 添加透明通道
main_surface.blit(source_surface_2_covert, (0, 0))
pygame.display.update()
time.sleep(2)

# 5. ‌get_size()‌ 獲取surface obj的尺寸(width, height)
print(f"main surface size is: {main_surface.get_size()}")

# 6. 獲取surface obj對應的矩形區域，get_rect(**kwargs) -> Rect
print(f"對應的矩形是:{source_surface_2_covert.get_rect()}")
pygame.quit()
