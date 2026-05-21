import pygame
import random
import time
from FlappyMark import FlappyMark

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

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.speed += GRAVITY
        self.image = pygame.transform.rotate(self.origin_image, -3 * self.speed)
        self.rect.y += self.speed
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.mask = pygame.mask.from_surface(self.image)

    def bump(self):
        self.speed = -6.5


class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/base.png").convert_alpha()
        self.image = pygame.transform.scale(self.origin_image, (SCREEN_WIDTH, self.origin_image.get_size()[1]))
        self.rect = self.image.get_rect(bottomleft=(0, SCREEN_HEIGHT))  # 指定坦克的左中點位置

        self.mask = pygame.mask.from_surface(self.image)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, inverted, init_xpos, show_height):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/pipe-green.png")
        self.image = pygame.transform.scale(self.origin_image, (PIPE_WIDTH, PIPE_HEIGHT))

        self.mask = pygame.mask.from_surface(self.image)

        self.is_calculated_mark = False

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect = self.image.get_rect()
            self.rect.x = init_xpos
            self.rect.y = show_height - PIPE_HEIGHT
        else:
            self.rect = self.image.get_rect()
            self.rect.x = init_xpos
            self.rect.y = SCREEN_HEIGHT - show_height

        self.speed = 4

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= self.speed

    def set_calculated(self):
        self.is_calculated_mark = True

    def get_is_calculated(self):
        return self.is_calculated_mark


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
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
        # 6. Mark Show Obj
        self.flappy_mark = FlappyMark(1.5)
        # 7. 音效 相關
        self.wing_sound_obj = pygame.mixer.Sound('resources/audio/wing.wav')
        self.hit_sound_obj = pygame.mixer.Sound('resources/audio/hit.wav')
        self.die_sound_obj = pygame.mixer.Sound('resources/audio/die.wav')
        self.get_point_sound_obj = pygame.mixer.Sound('resources/audio/point.wav')
        # 8. 背景圖像
        # TODO 1 加入背景圖像，把它scale成遊戲的size
        self.background_original_img = pygame.image.load("resources/image/background-day.png")
        self.background_img = pygame.transform.scale(self.background_original_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # 變量:
        self.running = True
        self.mark = 0
        # 常量:
        self.FPS = 60

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.add_mark()
            self.collision_detection()
            self.render()

        time.sleep(1)
        self.die_sound_obj.play()
        time.sleep(1)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.bump()
                    self.wing_sound_obj.play()

    def update(self):
        # 更新
        self.bird.update()
        self.pipe_group.update()
        if self.is_off_screen(self.pipe_group.sprites()[0]):
            self.pipe_group.empty()
            self.get_random_height_pipe()

    def render(self):
        # 渲染
        # self.main_surface.fill(self.background_color)
        # TODO 2 render的第一步先畫背景圖像
        self.main_surface.blit(self.background_img, (0,0))
        self.pipe_group.draw(self.main_surface)
        self.main_surface.blit(self.base.image, self.base.rect)
        self.main_surface.blit(self.bird.image, self.bird.rect)
        mark_sub_obj = self.flappy_mark.get_num_surface_obj(self.mark)
        self.main_surface.blit(mark_sub_obj, (SCREEN_WIDTH // 2 - mark_sub_obj.get_width() // 2, 50))
        pygame.display.update()

    def collision_detection(self):
        hit_pipe_list = pygame.sprite.spritecollide(self.bird, self.pipe_group, False, pygame.sprite.collide_mask)
        hit_base = pygame.sprite.collide_mask(self.bird, self.base)  # 使用self.rect去比較

        # 有碰撞
        if len(hit_pipe_list) != 0 or hit_base:
            self.hit_sound_obj.play()
            self.running = False

    def add_mark(self):
        pipe = self.pipe_group.sprites()[0]
        pipe_x = pipe.rect.x
        bird_x = self.bird.rect.x
        if pipe_x < bird_x:
            if not pipe.get_is_calculated():
                self.mark += 1
                self.get_point_sound_obj.play()
                pipe.set_calculated()

    def get_random_height_pipe(self):
        show_pipe_height = random.randint(100, 300)
        pipe = Pipe(False, SCREEN_WIDTH, show_pipe_height)  # 正放pipe
        inverted_pipe = Pipe(True, SCREEN_WIDTH, SCREEN_HEIGHT - TOP_DOWN_PIPE_GAP - show_pipe_height)
        self.pipe_group.add([pipe, inverted_pipe])

    def is_off_screen(self, check_sprite):
        return check_sprite.rect.x < -check_sprite.rect.w


if __name__ == '__main__':
    game = Game()
    game.start()
