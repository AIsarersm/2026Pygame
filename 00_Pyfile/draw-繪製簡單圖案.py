import pygame
import time

pygame.init()

main_surface = pygame.display.set_mode((480, 640))

# 1. draw rect
# pygame.draw.rect(surface, color, rect, width=0) -> Rect
init_a_rect = pygame.rect.Rect(0, 0, 50, 50)
pygame.draw.rect(main_surface, (255, 255, 255), init_a_rect, 0)
init_b_rect = pygame.rect.Rect(0, 60, 50, 50)
pygame.draw.rect(main_surface, (255, 0, 100), init_b_rect, 2)
pygame.display.update()
time.sleep(1)

# 2. draw polygon
# pygame.draw.polygon(surface, color, points, width=0) -> Rect
# width=0 means fill the polygon
# if width > 0, used for line thickness
# if width < 0, nothing will be drawn
pygame.draw.polygon(main_surface, (255, 0, 0), [(60, 30), (70, 40), (100, 20)], 0)
pygame.draw.polygon(main_surface, (255, 255, 0), [(60, 70), (70, 80), (100, 60), (80, 50)], 1)
pygame.display.update()
time.sleep(1)

# 3. draw circle
# pygame.draw.circle(surface, color, center, radius, width=0) -> Rect
pygame.draw.circle(main_surface, (0, 255, 0), (150, 30), 30)
pygame.draw.circle(main_surface, (0, 255, 0), (150, 100), 30, 1)
pygame.display.update()
time.sleep(1)

# 4. draw ellipse
# pygame.draw.ellipse(surface, color, rect, width=0) -> Rect
init_ellipse_rect = pygame.rect.Rect(200, 0, 100, 50)
pygame.draw.ellipse(main_surface, (0, 0, 255), init_ellipse_rect, 0)
init_ellipse_rect_b = pygame.rect.Rect(200, 60, 100, 50)
pygame.draw.ellipse(main_surface, (0, 0, 255), init_ellipse_rect_b, 1)
pygame.display.update()
time.sleep(1)

# 5. draw lines
# line(surface, color, start_pos, end_pos) -> Rect
pygame.draw.line(main_surface, (255, 255, 255), (300, 0), (450, 50))
pygame.display.update()
time.sleep(1)

time.sleep(5)
pygame.quit()
