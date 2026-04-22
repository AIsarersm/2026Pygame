import pygame

# pygame object for color representations
# 1. 使用RGB/RGBA去創建color object
color_red = pygame.color.Color(255, 0, 0)  # 創建red顏色
color_green = pygame.color.Color(0, 255, 0)
color_blue = pygame.color.Color(0, 0, 255)
color_red_a = pygame.color.Color(255, 0, 0, 100)

# 2. 使用預設定的顏色名稱初始化
# https://www.pygame.org/docs/ref/color_list.html
color_gray = pygame.color.Color("gray")

# 3. color對象使用print可以獲取其RGB[A]值
# 这是因為在內部實現了__repr__/__str__方法，因此直接print其object時會輸出RGBA值
print(f"gray顏色的RGB是{color_gray}")

# 4. 可以直接獲取和修改其r, g, b, a, cmy, hsva, hsla等property, (read and write)
red_channel_of_color_red = color_red.r
green_channel_of_color_red = color_red.g
blue_channel_of_color_red = color_red.b
alpha_channel_of_color_red = color_red.a
print(f"red_channel_of_color_red: {red_channel_of_color_red}")
print(f"green_channel_of_color_red: {green_channel_of_color_red}")
print(f"blue_channel_of_color_red: {blue_channel_of_color_red}")
print(f"alpha_channel_of_color_red: {alpha_channel_of_color_red}")

print(color_red)
