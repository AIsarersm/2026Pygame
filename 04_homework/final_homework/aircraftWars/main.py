import pygame
import random
from Button import Button  # 按鈕模塊

# 定義全局常量
# 視窗寬度
SCREEN_WIDTH = 500
# 視窗高度
SCREEN_HEIGHT = 600
# 最大子彈數量
MAX_BULLETS = 5
# 敵人出現時間間隔
ENEMY_DELTA_TIME = 2000
# 敵方子彈出現最大時間間隔
ENEMY_BULLET_DELTA_TIME = 1500


# 自身飛機子類
class Aircraft(pygame.sprite.Sprite):
    def __init__(self):
        # 父類初始化
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/hero1.png").convert_alpha()
        # TODO 1 把圖像按比例縮到原來的0.8倍
        self.image = TODO
        self.rect = self.image.get_rect()
        # 初始化位置放在中間
        self.rect.x = SCREEN_WIDTH // 2 - self.image.get_width() // 2
        # 初始化y放在距底邊110處
        self.rect.y = SCREEN_HEIGHT - 110
        self.speed = 6
        self.mask = pygame.mask.from_surface(self.image)

    # TODO 2 飛機只可以左右移動
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and TODO:  # TODO 2.1 添加邊界檢查，只有當飛機的x坐標 > 0時才可以繼續向左走
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and TODO:  # TODO 2.2 添加邊界檢查，只有當飛機的right坐標 < 視窗寬度時才可以繼續向右走
            self.rect.x += self.speed

    def shoot(self):
        # TODO 3 子彈的初始化位置飛機的midtop的位置
        return Bullet(TODO, TODO, 1)


# 敵方飛機類
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image_type):  # image_type=0或1，代表兩種敵方飛機，
        # 父類初始化
        super().__init__()
        if image_type == 0:
            self.image = pygame.image.load("resources/image/enemy0.png")
        else:
            self.image = pygame.image.load("resources/image/enemy1.png")

        self.rect = self.image.get_rect(midbottom=(random.randint(50, SCREEN_WIDTH - 50), -30))
        self.speed = random.randint(1, 5)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speed  # 敵方飛機不停向下走
        if TODO:  # TODO 4 當敵方飛機的y位置起出了視窗外時
            self.kill()

    def shoot(self):
        # TODO 5 子彈的初始化位置飛機的midbottom的位置
        return Bullet(TODO, TODO, -1)


# 子彈子類
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pox, y_pox, speed_sign=1):  # speed_sign用於判斷是自身子彈還是敵方子彈
        # 父類初始化
        super().__init__()
        self.speed_sign = speed_sign
        if speed_sign == 1:
            self.image = pygame.image.load("resources/image/bullet.png")
        elif speed_sign == -1:
            self.image = pygame.image.load("resources/image/enemy_bullet.png")

        self.rect = self.image.get_rect(midbottom=(x_pox, y_pox))
        self.speed = -6 * speed_sign
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speed
        if self.speed_sign == 1:  # 我方子彈
            if TODO:  # TODO 6 我方子彈消失的條件。提示: 我方子彈是往上升的
                self.kill()
        elif self.speed_sign == -1:  # 敵方子彈
            if TODO:  # TODO 7 敵方子彈消失的條件。提示: 敵方子彈是往下跌的
                self.kill()


# 滾動窗口類
class ScrollingBackground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origin_image = pygame.image.load("resources/image/background.png")
        self.resize_image = pygame.transform.scale(self.origin_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        two_background_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2), pygame.SRCALPHA)
        two_background_surface.blit(self.resize_image, (0, 0))
        two_background_surface.blit(self.resize_image, (0, SCREEN_HEIGHT))
        self.image = two_background_surface
        self.rect = self.image.get_rect()  # 此時生成的rect，其x和y坐標為(0,0)
        self.rect.y = -SCREEN_HEIGHT
        self.speed = 5
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.y += self.speed  # 向下移動
        if self.rect.y >= 0:
            self.rect.y = TODO  # TODO 8 窗口需要重新放置位置


# 遊戲管理主類
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.mixer.init()
        # 其他對象
        # 0. 定義視窗
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 1. 時鐘對象
        self.clock = pygame.time.Clock()
        # 2. 創建滾動背景子類
        self.scrolling_background = ScrollingBackground()
        # 3. 創建飛機子類
        self.aircraft = Aircraft()
        # 4. 創建我方子彈Group
        self.hero_bullet_group = pygame.sprite.Group()
        # 5. 創建敵方Group
        self.enemies_group = pygame.sprite.Group()
        # 6. 創建敵方子彈Group
        self.enemies_bullets_group = pygame.sprite.Group()
        # 7. 創建子彈中擊時的音效bomb.wav TODO 9
        self.bomb_sound_obj = TODO
        self.bomb_sound_obj.set_volume(0.5)
        # 8. 加載背景音樂
        # TODO 10 加載background_music.ogg
        TODO
        # 9. 創建分數子體對象
        self.mark_obj = pygame.font.SysFont("calibri", 26)
        self.mark_obj.underline = True
        self.mark_obj.bold = True

        # 10. 新增首頁相關
        self.name_img = pygame.image.load("resources/image/name.png").convert_alpha()
        self.start_img = pygame.image.load('resources/image/new-game-button.png').convert_alpha()
        self.start_button = Button(160, 400, self.start_img, 0.6, "start")
        self.aircraft_img = pygame.image.load("resources/image/hero1.png")
        # 11. 新增尾頁相關
        self.gameover_img = pygame.image.load("resources/image/gameover.png").convert_alpha()
        self.gameOver_alpha = 0
        self.aircraft_page_alpha = 0
        # 變量:
        self.running = True
        self.mark = 0
        self.current_time = 0
        self.hero_next_bullet_time = 0
        self.next_enemy_time = 0
        self.next_enemy_bullet_time = 0
        self.page = 1  # 新增頁控制變量
        # 常量:
        self.FPS = 60
        self.MAX_BULLETS = MAX_BULLETS
        self.BULLET_DELTA_TIME = 100
        self.ENEMY_DELTA_TIME = ENEMY_DELTA_TIME

    def start(self):
        # TODO 11 播放背景音樂，無限不停地播放，由0.0秒開始播
        TODO
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            if self.page == 1:  # 首頁
                self.first_page_update()
                self.first_page_render()
            elif self.page == 2:  # 主遊戲頁面
                self.update()
                self.collision_detection()
                self.render()
            elif self.page == 3:  # 尾頁
                self.end_page_update()
                self.end_page_render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        if self.page == 2:
            self.check_space_key()
            self.generate_enemy()
            self.generate_enemy_bullets()

    def update(self):
        # TODO 14 各對象進行更新，包括滾動背景類->飛機類->敵方Group->我方子彈Group->敵方子彈Group


    def collision_detection(self):
        # TODO 15 檢測自身飛機和敵方子彈Group的碰撞情況，使用 pygame.sprite.collide_mask
        hit_tank_list = TODO
        if len(hit_tank_list) != 0:
            self.running = False

        # TODO 16 檢測自身子類Group和敵方Group的碰撞情況，若有撞碰，我方和敵方的group中對象都要消失
        hit_enemy_list = pygame.sprite.groupcollide(
            TODO, TODO, TODO, TODO, pygame.sprite.collide_mask)

        for bullet, hit_enemies in hit_enemy_list.items():
            for hit_enemy in hit_enemies:  # 每打中一個敵人
                # TODO 17 播音效
                TODO
                # TODO 18 分數變量加分
                TODO

        print(f"分數是: {self.mark}")

    def render(self):
        self.main_surface.blit(self.scrolling_background.image, self.scrolling_background.rect)
        self.main_surface.blit(self.aircraft.image, self.aircraft.rect)
        self.enemies_group.draw(self.main_surface)
        self.hero_bullet_group.draw(self.main_surface)
        self.enemies_bullets_group.draw(self.main_surface)

        text_surface = self.mark_obj.render(f"Mark: {self.mark}", True, (0, 0, 100), None)
        self.main_surface.blit(text_surface, (450 - text_surface.get_width() // 2, 0))
        pygame.display.update()

    def first_page_update(self):
        self.scrolling_background.update()

    def end_page_update(self):
        self.scrolling_background.update()
        # TODO 20 實現self.gameOver_alpha和self.aircraft_page_alpha逐漸遞增，然後使用set_alpha()設置img的透明度
        if self.gameOver_alpha <= 255:
            # TODO
            TODO
        else:
            self.gameover_img.set_alpha(255)

        if self.aircraft_page_alpha <= 255:
            # TODO
            TODO
        else:
            self.aircraft_img.set_alpha(255)

    def first_page_render(self):
        self.main_surface.blit(self.scrolling_background.image, self.scrolling_background.rect)
        self.main_surface.blit(self.name_img, (40, 100))
        self.main_surface.blit(self.aircraft_img, (200, 230))
        self.start_button.draw(self.main_surface)
        if self.start_button.checkifclick():
            # TODO 19 跳轉到頁面2
            TODO
        pygame.display.update()

    def end_page_render(self):
        self.main_surface.fill((0, 0, 0))
        self.main_surface.blit(self.scrolling_background.image, self.scrolling_background.rect)
        self.main_surface.blit(self.gameover_img, (40, 100))
        self.main_surface.blit(self.aircraft_img, (200, 230))

        pygame.display.update()

    def check_space_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.current_time = pygame.time.get_ticks()
            if len(self.hero_bullet_group.sprites()) < self.MAX_BULLETS and self.current_time >= self.hero_next_bullet_time:
                self.hero_next_bullet_time = self.current_time + self.BULLET_DELTA_TIME  # 控制子彈發射間隔
                bullet = TODO  # TODO 12 bullet為我方shoot()生成的子彈類
                self.hero_bullet_group.add(bullet)

        print(f"我方子彈數量: {len(self.hero_bullet_group.sprites())}")

    def generate_enemy(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time >= self.next_enemy_time:
            self.next_enemy_time = self.current_time + self.ENEMY_DELTA_TIME
            enemy = Enemy(random.randint(0,1))
            self.enemies_group.add(enemy)

        print(f"敵人數量: {len(self.enemies_group.sprites())}")

    def generate_enemy_bullets(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time >= self.next_enemy_bullet_time:
            self.next_enemy_bullet_time = self.current_time + random.randint(1000, ENEMY_BULLET_DELTA_TIME)
            # TODO 13 enemies_group中每一個enemy都要shoot()子彈，然後每一粒敵方子彈add到enemies_bullets_group中
            TODO

        print(f"敵人子彈數量: {len(self.enemies_bullets_group.sprites())}")


if __name__ == '__main__':
    game = Game()
    game.start()
