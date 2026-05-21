import pygame


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

    def update(self):  # 重寫update，使用get_pressed()判斷上下
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


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


class Game:
    def __init__(self):
        pygame.init()
        # 其他對象
        # 0. 定義視窗
        self.main_surface = pygame.display.set_mode((600, 400))
        # 1. 時鐘對象
        self.clock = pygame.time.Clock()
        # 2. 坦克對象
        self.tank = Tank()
        # 3. ScrollingTree對象
        self.tree_group = ScrollingTree()
        # 變量:
        self.running = True
        # 常量:
        self.FPS = 60

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 更新位置
            self.tank.update()
            self.tree_group.update()

            # 渲染
            self.main_surface.fill((192, 192, 255))
            pygame.draw.rect(self.main_surface, (64, 128, 64), (0, 250, 600, 150))
            self.main_surface.blit(self.tree_group.image, self.tree_group.rect)
            self.main_surface.blit(self.tank.image, self.tank.rect)
            pygame.display.update()

if __name__ == '__main__':
    my_APP = Game()
    my_APP.start()
