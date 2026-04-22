import pygame
import time

# pygame.display
# pygame module to control the display window and screen
# 用於創建和管理界面
# 常用function: get_init(), set_mode(), set_icon(), set_caption(), get_window_size(), update()
pygame.init()  # 執行pygame.init()時會自動執行display模塊的init(), 即pygame.display.init()

# 1. 設置遊戲主窗口，並指定其大小pixel.
# set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
# size為界面尺寸
# flags 是一系列額外的options，例如pygame.FULLSCREEN(全屏)
main_surface = pygame.display.set_mode(size=(480, 640))#, flags=pygame.NOFRAME)
print("*****************************************************************")
# 2. 設置主窗口遊戲標題:
pygame.display.set_caption("Game tester")
# 3. 獲取主窗口大小:
print(f"main surface size is: {pygame.display.get_window_size()}")
time.sleep(5)

#  最後記得要釋放資源
pygame.quit()
#  其余功能請看ref:
#  https://www.pygame.org/docs/ref/display.html
