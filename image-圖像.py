import pygame

# 從本地中輸入圖像並返回surface對像
# 1. 加載圖片
# pygame.image.load(filename) -> Surface
# 可加載的圖片格式為BMP、GIF (non-animated)、JPEG、LBM (and PBM, PGM, PPM)、PCX、PNG、PNM、
# SVG (limited support, using Nano SVG)、TGA (uncompressed)、TIFF、WEBP、XPM
image_1 = pygame.image.load("./resources/image/bluebird-downflap.png") # .convert_alpha() #convert_alpha()‌，既能正确处理透明度，又能优化性能‌
# 如果路徑不存在，會報錯FileNotFoundError，可通過try except 查看圖片是否被加載成功

# 2. 保存圖片
# pygame.image.save(Surface, filename) -> None
pygame.image.save(image_1, "./test.png")
