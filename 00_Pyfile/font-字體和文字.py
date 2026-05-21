import pygame
import time

pygame.init()
main_surface = pygame.display.set_mode(size=(400,400))

# font為字體管理模塊，同時亦可以進行文本輸出
# 1. 獲取所有可用的字體，pygame.font.get_fonts() -> list of strings
all_usable_font = pygame.font.get_fonts()
print(f"系統中擁有如下字體:{all_usable_font}")

# 2. 使用系統的字體來創建pygame的Font 對象
# pygame.font.SysFont(name, size, bold=False, italic=False) -> Font
sysFont_obj = pygame.font.SysFont("arial", 30)

# 3.pygame中Font對象有以下使用方式
# 3.1 生成一個文字的surface對象
# render(text, antialias, color, background=None) -> Surface
# The antialias argument is a boolean: if True the characters will have smooth edges
# The color argument is the color of the text [e.g.: (0,0,255) for blue]
# The optional background argument is a color to use for the text background
text_surface = sysFont_obj.render("Hello!", True, (0, 0, 255), None)
# 在main surface上render出文字
main_surface.blit(text_surface, (0, 0))

# 3.2 "bold" property，獲取和設置該字體對象是否粗體
print(f"原字體是否粗體: {sysFont_obj.bold}")
sysFont_obj.bold = True
print(f"更改後字體是否粗體: {sysFont_obj.bold}")
text_surface_bold = sysFont_obj.render("Hello!", True, (0, 0, 255), None)
main_surface.blit(text_surface_bold, (0, 80))

# 5.3 "italic" property，獲取和設置該字體對象是否斜體
print(f"原字體是否斜體: {sysFont_obj.italic}")
sysFont_obj.italic = True
print(f"更改後字體是否斜體: {sysFont_obj.italic}")
text_surface_bold_italic = sysFont_obj.render("Hello!", True, (0, 0, 255), None)
main_surface.blit(text_surface_bold_italic, (0, 160))

# 5.4 "underline" property，獲取和設置該字體對象是否有下底線
print(f"原字體是否有下底線: {sysFont_obj.underline}")
sysFont_obj.underline = True
print(f"更改後字體是否有下底線: {sysFont_obj.underline}")
text_surface_bold_italic_underline = sysFont_obj.render("Hello!", True, (0, 0, 255), None)
main_surface.blit(text_surface_bold_italic_underline, (0, 240))

# 5.5 "strikethrough" property，獲取和設置該字體對象是否有刪除線
print(f"原字體是否有有刪除線: {sysFont_obj.strikethrough}")
sysFont_obj.strikethrough = True
print(f"更改後字體是否有有刪除線: {sysFont_obj.strikethrough}")
text_surface_bold_italic_underline_strikethrough = sysFont_obj.render("Hello!", True, (0, 0, 255), None)
main_surface.blit(text_surface_bold_italic_underline_strikethrough, (0, 320))

pygame.display.update()
time.sleep(5)

# quit()釋放內存，pygame.font.quit() -> None
pygame.font.quit()

pygame.quit()
