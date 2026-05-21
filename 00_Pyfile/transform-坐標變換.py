import pygame
import time
# 模組初始化
pygame.init()
# 創建主視窗
main_surface = pygame.display.set_mode((400, 400))

# 1. 水平/垂直翻轉，flip(surface, flip_x, flip_y) -> Surface
source_surface = pygame.image.load("./resources/image/bluebird-downflap.png")
new_surface_flip_x = pygame.transform.flip(source_surface, True, False)   # 水平flip
new_surface_flip_y = pygame.transform.flip(source_surface, False, True)   # 垂直flip
main_surface.blit(source_surface, (0, 0))
main_surface.blit(new_surface_flip_x, (100, 0))
main_surface.blit(new_surface_flip_y, (200, 0))

# 2. scale surface去一個新的resolution，scale(surface, size, dest_surface=None) -> Surface
print(f"原有image surface的size是:{source_surface.get_size()}")
new_surface_size_scale = pygame.transform.scale(source_surface, (100, 78))
print(f"原有image surface的size是:{new_surface_size_scale.get_size()}")
main_surface.blit(new_surface_size_scale, (0, 100))

# 2.1 按比例縮小放大，scale_by(surface, factor, dest_surface=None) -> Surface
new_surface_size_scale_by_big = pygame.transform.scale_by(source_surface, 2)
new_surface_size_scale_by_small = pygame.transform.scale_by(source_surface, 0.5)
main_surface.blit(new_surface_size_scale_by_big, (100, 100))
main_surface.blit(new_surface_size_scale_by_small, (200, 100))

# 3. 逆/順時針旋轉，rotate(surface, angle) -> Surface
new_surface_rotate = pygame.transform.rotate(source_surface, 45)  # 此為逆時針轉45度。注意: 正數為逆時針，負數為順時針
main_surface.blit(new_surface_rotate, (0, 200))

pygame.display.update()
time.sleep(5)
pygame.quit()
