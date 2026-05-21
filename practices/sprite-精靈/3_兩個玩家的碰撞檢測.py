import pygame

# 定義常量
# 主畫面的寬和高
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400


class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        # 為父類初始化
        super().__init__()
        # 通過文字定義顏色
        self.color = pygame.color.Color(color)
        # 創建一個正方形
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, (0, 0, 60, 60))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 5

    def update(self):  # 重寫update，通過wsad控制方向
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed


class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        # 為父類初始化
        super().__init__()
        # 通過文字定義顏色
        self.color = pygame.color.Color(color)
        # 創建一個正方形
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, (0, 0, 60, 60))
        self.rect = self.image.get_rect(center=(x, y))

        self.speed = 5

    def update(self):  # 重寫update()，通過上下左右控制
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


class Game:
    def __init__(self):
        pygame.init()
        # 其他對象
        # 0. 定義視窗
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 1. 時鐘對象
        self.clock = pygame.time.Clock()
        # 2. 定義Font 對象
        # 創建文字對象
        self.sysFont_obj = pygame.font.SysFont("calibri", 26)
        # 設置文字對象帶有下底線
        self.sysFont_obj.underline = True
        # 設置文字對象帶有粗體
        self.sysFont_obj.bold = True
        # 3. 自定義Player對象
        self.player1 = Player1(100, 200, "red")
        # 4. 自定義Player對象
        self.player2 = Player2(300, 200, "yellow")
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

    def update(self):
        # 更新
        self.player1.update()
        self.player2.update()

    def render(self):
        self.main_surface.fill((255, 255, 255))
        self.main_surface.blit(self.player1.image, self.player1.rect)
        self.main_surface.blit(self.player2.image, self.player2.rect)
        # 使用pygame.sprite.collide_rect()進行碰撞檢測，若是True代表有重疊，反之
        text_surface = self.sysFont_obj.render(f"Is collide?: {pygame.sprite.collide_rect(self.player1, self.player2)}", True, (0, 0, 100), (0, 100, 0))
        self.main_surface.blit(text_surface, (220, 0))

        pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.start()
