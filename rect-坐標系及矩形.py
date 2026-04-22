import pygame

# 坐標系:
    # 坐標系原點在左上角(0,0)
    # x軸水平向右，逐漸增加
    # y軸垂直向下，逐漸增加


# 矩形 (pygame.Rect)
    # pygame object for storing rectangular coordinates
    # 遊戲中矩形元素都是要以矩形描过，包括該矩陣左上角點坐標(x,y)，及其寬度(width)和高度(height). [x,y,w,h]
    # 初始化方法 Rect(left, top, width, height), Rect((left, top), (width, height))
test_rect = pygame.Rect(100, 500, 50, 60)
# test_rect = pygame.Rect((100, 500), (50, 60))


# 基本屬性:
print(f"矩形的坐標原點是{test_rect.x},{test_rect.y}")  # 坐標可以是負值
print(f"矩形的坐標原點是{test_rect.left},{test_rect.top}")
print(f"矩形的寬度是{test_rect.width}, 矩形的高度{test_rect.height}")  # width也可以用w, height也可以用h
print(f"矩形的中心是{test_rect.center}, 其中心的x坐標是{test_rect.centerx}, 其y坐標是{test_rect.centery}")
print(f"矩形的左上是{test_rect.topleft}, 左下是{test_rect.bottomleft}, 右上是{test_rect.topright}, 右下是{test_rect.bottomright}")
print(f"矩形的左中是{test_rect.midleft}, 下中是{test_rect.midbottom}, 右中是{test_rect.midright}, 上中是{test_rect.midtop}")
print(f"矩形的size是{test_rect.size}")  # 注意size是獲取矩形的寬度和高度，用元組方式表示
print("*****************************************************************")


# 以上的property除了可以read外，還可以write，即可以被賦上新值，
# Example1: 修改矩形的寬度
print(f"修改前的矩形的寬高是{test_rect.w},{test_rect.h}")
test_rect.width = 60
print(f"修改後的矩形的寬高是{test_rect.w},{test_rect.h}")
print("*****************************************************************")
# 重點!: 修改size, width, height時 - 「changes the dimensions of the rectangle」


# Example2: 修改中心點
print(f"修改前的矩形的中心是{test_rect.center}")
print(f"修改前的矩形的坐標原點是{test_rect.x},{test_rect.y}")
test_rect.center = (140, 540)
print(f"修改後的矩形的坐標原點是{test_rect.x},{test_rect.y}")
print(f"修改後的矩形的中心是{test_rect.center}")
print("*****************************************************************")
# 重點!: 修改其余property時，「move the rectangle without resizing it.」

# For more refs.
# https://www.pygame.org/docs/ref/rect.html
