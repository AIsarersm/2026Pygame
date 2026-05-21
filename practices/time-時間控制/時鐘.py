import pygame
# 模組初始化
pygame.init()
# 初始化視窗
screen = pygame.display.set_mode((300, 100))
# 創建font對象
timer_font = pygame.font.SysFont("Calibri", 38)
# 獲取遊戲開始瞬間的時間ms
start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time_ms = pygame.time.get_ticks() - start_time
    # time_ms是獲取到的遊戲時長(ms)，轉為時、分、秒
    # 1. 先轉為秒
    time_s = time_ms // 1000  # 取整
    # 2. 計算秒
    new_s = time_s % 60
    new_m = time_s // 60
    # 3. 計算分
    new_m = new_m % 60
    new_h = new_m // 60
    # 4. 計算時
    new_h = new_h % 24

    timer_surf = timer_font.render(f'{new_h:02d}:{new_m:02d}:{new_s:02d}', True, (255, 255, 255))

    screen.fill(0)
    screen.blit(timer_surf, (80, 20))
    pygame.display.update()

pygame.quit()
