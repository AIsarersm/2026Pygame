import pygame

pygame.init()
# 1. pygame.time.get_ticks() - 獲取從init()後的遊戲運行時長，單位為ms
print(f"遊戲init後的運行時長{pygame.time.get_ticks()}ms")

# 2. pygame.time.delay(ms) - 遊戲休眠多少ms，delay()比wait()更準確
pygame.time.delay(1000)
print(f"遊戲init後的運行時長{pygame.time.get_ticks()}ms")

# 3. pygame.time.wait(ms) - 遊戲休眠多少ms，wait()比delay()準確差
pygame.time.wait(1000)
print(f"遊戲init後的運行時長{pygame.time.get_ticks()}ms")

# 4. pygame.time.Clock
# 主要用於控制遊戲的FPS
# Clock對像中有一個tick(fps)函數，在每一次更新時需要使用tick(fps)去控制FPS
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)  # 指的是遊戲以60FPS進行，系統會自動控制時間，使得遊戲1s只會執行60次
    # do something
    # clock對像中有一個函數可以知道現在的fps, clock.get_fps()
    print(clock.get_fps())

pygame.quit()
