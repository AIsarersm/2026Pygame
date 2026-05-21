import pygame
import time

pygame.init()
main_surface = pygame.display.set_mode(size=(600, 400))

# 3. 當我們的一直按下某個鍵，默認情況下，系統只會觸發一次事件。
# 如果想系統一直觸發「按下」这個事件，則需要使用到set_repeat()
# 當set_repeat()不給參數時，代表是disable这功能，即只觸發一次事件
# 而當設置成set_repeat(delay, interval)，代表在delay多少秒發首次觸發第一次事件，之後每隔interval觸發一次
# pygame.key.set_repeat(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # event type
            running = False
        if event.type == pygame.KEYDOWN: # keyboard 按下事件
            if event.key == pygame.K_COMMA:  # event attributes，这里判斷是不是r鍵
                print(",鍵被按下了")

    # 1. 返回包含所有鍵盘狀態的bool列表
    keys = pygame.key.get_pressed()  # key是一個列表，使用key[xx]來獲取該key是否按下
    if keys[pygame.K_LEFT]:
        print("左鍵被按下")
    # 例如有
    # 方向鍵
    # pygame.K_RIGHT ->右鍵
    # pygame.K_UP -> 上鍵
    # pygame.K_DOWN -> 下鍵
    # 字母键
    # pygame.K_a -> A 键
    # pygame.K_b -> B 键
    # ...... 其他字母類似，如 K_c 到 K_z
    # 數字鍵:
    # pygame.K_0 -> 数字 0
    # pygame.K_1 -> 数字 1
    # 其他數字鍵如K_2 到 K_9
    # 功能键:
    # pygame.K_SPACE → 空格键
    # pygame.K_ESCAPE → ESC 键
    # pygame.K_RETURN → 回车键
    # pygame.K_BACKSPACE → 退格键
    # 修飾鍵:
    # pygame.K_LSHIFT → 左侧 Shift 键
    # pygame.K_RCTRL → 右侧 Control 键
    # pygame.K_CAPSLOCK → 大写锁定键
    # ......

    # 2. 獲取特殊修飾鍵:
    mods = pygame.key.get_mods()
    # get_mods() 返回的修饰键以‌位掩碼组合‌形式表示，可檢測以下按键的激活狀態
    # KMOD_SHIFT → 任意 Shift 键（左/右）
    # KMOD_CTRL → 任意 Control 键（左/右）
    # KMOD_ALT → 任意 Alt 键（左/右）
    # KMOD_CAPS → Caps Lock 键（大写锁定）
    # KMOD_MODE → AltGr 键（部分键盘布局支持）
    # KMOD_NUM → Num Lock 键（数字键盘锁定）
    # KMOD_META → Windows 键 或 Command 键（Mac）
    # 2.1 使用方法是需要通過按位與(&)判斷是否激活
    if_shift_pressed = mods & pygame.KMOD_SHIFT
    if if_shift_pressed:
        print(f"if_shift_pressed: {if_shift_pressed}")

    time.sleep(0.05)

# 4. 獲取pygame 標識符（如 K_SPACE）轉換為可讀名稱（如 "Space"）
key_name = pygame.key.name(pygame.K_SPACE)
print(f"K_SPACE對應的名稱是:{key_name}")

# 5. 將名稱轉換為pygame的標識符
key_id = pygame.key.key_code("space")
print(f"在pygame中，space對應的標識符值是:{key_id}")
print(f"兩者是否相等: {key_id == pygame.K_SPACE}")

pygame.quit()
