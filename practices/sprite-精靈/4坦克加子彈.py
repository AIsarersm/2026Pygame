import pygame

# 視窗大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
# 最大子彈數量
MAX_BULLETS_NUM = 5


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        # 為父類初始化
        super().__init__()
        # 定義image屬性
        temp_surface = pygame.Surface((60, 40), pygame.SRCALPHA)
        pygame.draw.rect(temp_surface, (0, 96, 0), (0, 00, 50, 40))
        pygame.draw.rect(temp_surface, (0, 128, 0), (10, 10, 30, 20))
        pygame.draw.rect(temp_surface, (32, 32, 96), (20, 16, 40, 8))
        self.image = temp_surface
        # 定義rect，一般都是使用get_rect()
        self.rect = self.image.get_rect(midleft=(20, 330))  # 指定坦克的左中點位置
        # 額外變量
        self.speed = 5

    def update(self):  # 重寫update
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    # TODO 4
    def shoot(self):
        return Bullet(self.rect.midright[0], self.rect.midright[1])


class ScrollingTree(pygame.sprite.Sprite):
    def __init__(self):
        # 為父類初始化
        super().__init__()
        # 定義樹群Group的寬和高
        self.width = 600
        self.height = 400
        # 定義image屬性
        tree_image = pygame.image.load("./resources/image/tree_resize.png")
        # 把12個樹組合為一個surface
        bg_layer_tree_group = pygame.Surface((self.width*2, 400), pygame.SRCALPHA)
        for i in range(12):
            bg_layer_tree_group.blit(tree_image, (i * 100, 15))

        self.image = bg_layer_tree_group
        self.rect = self.image.get_rect()  # 此時生成的rect，其x和y坐標為(0,0)
        self.rect.x = 0
        self.rect.y = 150

        self.speed = 5

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x <= -self.width:
            self.rect.x = 0


# TODO 1
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # 為父類初始化
        super().__init__()
        # 創建透明surface對象
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        # 畫circle
        pygame.draw.circle(self.image, (64, 64, 62), (5, 5), 5)
        self.rect = self.image.get_rect(midleft=(x, y))
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > SCREEN_WIDTH:  # 超出屏幕結束
            self.kill()  # TODO 1


class Game:
    def __init__(self):
        pygame.init()
        # 其他對象
        # 0. 定義視窗
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 1. 時鐘對象
        self.clock = pygame.time.Clock()
        # 2. 坦克對象
        self.tank = Tank()
        # 3. ScrollingTree對象
        self.tree_group = ScrollingTree()
        # 4. bullets group # TODO 2
        self.bullets = pygame.sprite.Group()
        # 變量:
        self.running = True
        self.current_time = pygame.time.get_ticks()
        self.next_bullet_time = 0  # 記錄發射時間的變量
        # 常量:
        self.FPS = FPS
        self.MAX_BULLETS = MAX_BULLETS_NUM
        self.BULLET_DELTA_TIME = 100  # 控制相鄰子彈間發射的最小時間間隔

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

        # 生成子彈的函數
        self.check_space_key()  # TODO 3

    def update(self):
        # 更新
        self.tank.update()
        self.tree_group.update()
        self.bullets.update()  # 子彈Group統一自動更新，group中每一個子彈都自動做update() TODO 5

    def render(self):
        # 渲染
        self.main_surface.fill((192, 192, 255))
        pygame.draw.rect(self.main_surface, (64, 128, 64), (0, 250, 600, 150))
        self.main_surface.blit(self.tree_group.image, self.tree_group.rect)
        self.main_surface.blit(self.tank.image, self.tank.rect)
        # 子彈Group統一自動渲染，group中每一個子彈都自動做self.main_surface.blit(self.image, self.rect)  TODO 6
        self.bullets.draw(self.main_surface)
        pygame.display.update()

    # TODO 3
    def check_space_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.current_time = pygame.time.get_ticks()
            if len(self.bullets.sprites()) < self.MAX_BULLETS and self.current_time >= self.next_bullet_time:
                self.next_bullet_time = self.current_time + self.BULLET_DELTA_TIME  # 控制子彈發射間隔
                bullet = self.tank.shoot()  # 坦克對象生成一個midright位置的子彈 TODO 4
                self.bullets.add(bullet)

        print(f"子彈數量: {len(self.bullets.sprites())}")


if __name__ == '__main__':
    my_APP = Game()
    my_APP.start()
