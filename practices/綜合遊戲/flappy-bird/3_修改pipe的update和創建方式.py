import pygame
import random

# Game constant
GRAVITY = 0.3
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Pipe constant
PIPE_WIDTH = 80
PIPE_HEIGHT = 500
TOP_DOWN_PIPE_GAP = 150


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/bluebird-downflap.png").convert_alpha()
        self.image = self.origin_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))  # 指定坦克的左中點位置
        self.speed = 0

    def update(self):
        self.speed += GRAVITY
        self.image = pygame.transform.rotate(self.origin_image, -3 * self.speed)
        self.rect.y += self.speed
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def bump(self):
        self.speed = -6.5


class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/base.png").convert_alpha()
        self.image = pygame.transform.scale(self.origin_image, (SCREEN_WIDTH, self.origin_image.get_size()[1]))
        self.rect = self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT))  # 指定坦克的左中點位置


class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, init_xpos, show_height):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/pipe-green.png")
        self.image = pygame.transform.scale(self.origin_image, (PIPE_WIDTH, PIPE_HEIGHT))

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()
            self.rect.x = init_xpos
            self.rect.y = show_height - PIPE_HEIGHT
        else:
            self.rect = self.image.get_rect()
            self.rect.x = init_xpos
            self.rect.y = SCREEN_HEIGHT - show_height

        self.speed = 5

    def update(self):  # TODO 3 樹群如果出界，不用再把它复位了，因為會被系統自動刪除
        self.rect.x -= self.speed


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
        # 5. Pipe Group
        self.pipe_group = pygame.sprite.Group()
        self.get_random_height_pipe()
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
        # 更新
        self.bird.update()
        self.pipe_group.update()
        # TODO 1 判斷pipe有沒有出界，出界就清空，然後創建新的Pipe插入Group中
        if self.is_off_screen(self.pipe_group.sprites()[0]):
            self.pipe_group.empty()  # 清空 Group
            self.get_random_height_pipe()  # 創建新pipe對放入Group中

    def render(self):
        # 渲染
        self.main_surface.fill(self.background_color)
        self.pipe_group.draw(self.main_surface)
        self.main_surface.blit(self.base.image, self.base.rect)
        self.main_surface.blit(self.bird.image, self.bird.rect)
        pygame.display.update()

    def get_random_height_pipe(self):
        show_pipe_height = random.randint(100, 400)
        pipe = Pipe(False, SCREEN_WIDTH, show_pipe_height)  # 正放pipe
        inverted_pipe = Pipe(True, SCREEN_WIDTH, SCREEN_HEIGHT - TOP_DOWN_PIPE_GAP - show_pipe_height)
        self.pipe_group.add([pipe, inverted_pipe])

    def is_off_screen(self, check_sprite):  # TODO 2
        return check_sprite.rect.x < -check_sprite.rect.w


if __name__ == '__main__':
    game = Game()
    game.start()
