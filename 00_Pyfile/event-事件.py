import pygame
import time

# pygame.event 模塊主要用於獲取遊戲中的事件
# 需要在display模組初始化後使用
pygame.init()
main_surface = pygame.display.set_mode(size=(600, 400))
# pygame.key.set_repeat(100,100)
# 常用函數:
# 1. 獲取此時在event queue的所有事件。event.get()
# pygame.event.get(eventtype=None, pump=True, exclude=None) -> Eventlist
# 一般用法是在遊戲主循環中調用，然後獲取該幀內所有event. 然後篩選出想要的event type做對應操作，例如:
running = True
while running:
    for event in pygame.event.get():
        # 返回的event是一個pygame.Event對象，Event對象會包括一個"type"用以分析不同的event種類
        # 和對應attributes的一個dict，用以獲取數據
        if event.type == pygame.QUIT:  # event type
            # do something A
            print("遊戲離開了")
            running = False
        if event.type == pygame.KEYDOWN: # keyboard 按下事件
            if event.key == pygame.K_r:  # event attributes，这里判斷是不是r鍵
                # do something B
                print("R鍵被按下了")
            elif event.key == pygame.K_SPACE:
                print("space鍵被按下了")
            else:
                print("其他鍵被按下了")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == 1:
                print(f"在{mouse_pos}處按下了左鍵")
            elif event.button == 2:
                print(f"在{mouse_pos}處按下了中鍵")
            elif event.button == 3:
                print(f"在{mouse_pos}處按下了右鍵")

    time.sleep(0.05)

pygame.quit()

# 注意:
# get()如果不加參數將默認獲取所有在queue中的event，獲取後queue將清空
# 程序中必須要處理事件，否則系統會被locked. 原話「Not handling events may cause your system to decide your program has locked up」
# 因此不管你用不用到事件，你都是定期清理一下event queue的event.
# 實際是event的queue填滿了，並不會自己釋放


# # 除了使用系統自帶的event外，用戶還可以自定義event
# # 2. 自定義event。通過pygame.event.post()和pygame.event.custom_type()聯合組成
# # 2.1 先定義自定義event ID
# self_defined_event_id_a = pygame.event.custom_type() # 會生成一個在USEREVENT ~ NUMEVENTS - 1的event id
# # 2.2 然後生成event對陡，使用post發布
# self_event = pygame.event.Event(self_defined_event_id_a, {"my_key": "123", "my_id": 213})
# pygame.event.post(self_event)
# # post後，用戶就可以在event.get()中獲取到，通過用event.type == self_defined_event_id_a用以判斷
