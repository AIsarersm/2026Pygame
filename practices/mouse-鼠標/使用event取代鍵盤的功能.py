import pygame
import time

# 模組初始化
pygame.init()
# 創建主視窗
main_surface = pygame.display.set_mode(size=(600, 400))

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event type
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # 按下瞬間觸發的事件
            mouse_pos = event.pos  # 按下時的鼠標座標
            if event.button == 1:   # 按下時的鼠標按鍵是哪個，通過event.button來獲取
                print(f"在{mouse_pos}處按下了左鍵")
            elif event.button == 2:
                print(f"在{mouse_pos}處按下了中鍵")
            elif event.button == 3:
                print(f"在{mouse_pos}處按下了右鍵")
        if event.type == pygame.MOUSEBUTTONUP:    # 松開瞬間觸發的事件
            mouse_pos = event.pos  # 松開時的鼠標座標
            if event.button == 1:
                print(f"在{mouse_pos}處松開了左鍵")
            elif event.button == 2:
                print(f"在{mouse_pos}處松開了中鍵")
            elif event.button == 3:
                print(f"在{mouse_pos}處松開了右鍵")
        if event.type == pygame.MOUSEMOTION:    # 移動觸發的事件
            mouse_pos = event.pos  # 移動時的鼠標座標
            buttons = event.buttons  # 移動時鼠標按鍵狀態
            left_button_pressed = buttons[0]
            mid_button_pressed = buttons[1]
            right_button_pressed = buttons[2]
            if left_button_pressed:
                print(f"左鍵按實的情況下移動到{mouse_pos}")
            if mid_button_pressed:
                print(f"中鍵按實的情況下移動到{mouse_pos}")
            if right_button_pressed:
                print(f"右鍵按實的情況下移動到{mouse_pos}")

    time.sleep(0.05)

pygame.quit()
