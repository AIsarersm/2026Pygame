import pygame
import time

pygame.init()
main_surface = pygame.display.set_mode(size=(640,480))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event type
            running = False

    # 1. 獲取鼠標的實時按下狀態
    # get_pressed(num_buttons=3) -> (button1, button2, button3) # 常見鼠標
    # get_pressed(num_buttons=5) -> (button1, button2, button3, button4, button5)
    # 以三鍵鼠標為例，get_pressed(3)返回一個(左键状态, 中键状态, 右键状态)的元組
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        print("左键按下")
    if buttons[1]:
        print("中键按下")
    if buttons[2]:
        print("右键按下")

    # 2. 獲取鼠標在display畫面中的坐標(x,y)，pygame.mouse.get_pos()
    pos = pygame.mouse.get_pos()
    print(f"鼠標位置：{pos}")

    time.sleep(0.05)

# 注意:
# 事件驅動‌：對於單次點擊檢測（非持續按下），建議通過 MOUSEBUTTONDOWN 事件實現
