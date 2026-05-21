import pygame

GRAVITY = 0.3
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("./resources/image/bluebird-downflap.png").convert_alpha()
        self.image = self.origin_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))  # 指定坦克的左中點位置
        self.speed = 0

    def update(self):
        # TODO
        # 1. 速度更新，重力
        self.speed += GRAVITY
        # 2. 圖像旋轉，需要對self.origin_image進行旋轉來獲取新的self.image
        self.image = pygame.transform.rotate(self.origin_image, -3 * self.speed)
        # 3. 更新y坐標
        self.rect.y += self.speed
        # 4. 獲取新的rect
        self.rect = self.image.get_rect(center=self.rect.center)

    def bump(self):
        # TODO
        # 按空白鍵時，速度突變
        self.speed = -6.5


class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("./resources/image/base.png")
        # TODO
        # 使用transform scale把self.origin_image的寬度改為主視窗屏寬-SCREEN_WIDTH
        self.image = pygame.transform.scale(self.origin_image, (SCREEN_WIDTH, self.origin_image.get_size()[1]))
        self.rect = self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT))  # 指定坦克的左中點位置

    # TODO
    # 思考這對象需要update()嗎? 若需要，加上
    # Ans: 若地面不作移動，則不需要更新；若需要向左移動，則需要更新


class Game:
    def __init__(self):
        pygame.init()
        # 其他對象
        # 0. 定義視窗
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 1. 時鐘對象
        self.clock = pygame.time.Clock()
        # 2. 顏色對象
        self.background_color = pygame.color.Color("darkolivegreen2")
        # 3. Bird對象
        self.bird = Bird()
        # 4. Base對象
        self.base = Base()
        # 變量:
        self.running = True
        # 常量:
        self.FPS = 60

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.bump()

    def update(self):
        # TODO
        # 把需要移動的對象進行更新
        self.bird.update()

    def render(self):
        # 渲染
        self.main_surface.fill(self.background_color)
        self.main_surface.blit(self.bird.image, self.bird.rect)
        self.main_surface.blit(self.base.image, self.base.rect)
        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.start()
