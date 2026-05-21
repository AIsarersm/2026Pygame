import pygame
import random

# 視窗大小
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60
# 最大子彈數量
MAX_BULLETS_NUM = 15
# 敵方生成間隔時間
ENEMY_DELTA_TIME = 2000
ENEMY_BULLET_DELTA_TIME = 1500


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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_sign=1):  # speed_sign指的是子彈的傳播方向，1代表向右射(主角的子彈)，-1代表向左射(敵人的子彈)
        # 為父類初始化
        super().__init__()
        # 創建透明surface對象
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        # 畫circle
        pygame.draw.circle(self.image, (64, 64, 62), (5, 5), 5)
        self.rect = self.image.get_rect(midleft=(x, y))
        # 速度方向
        self.speed_sign = speed_sign
        self.speed = 5 * speed_sign  # 1就speed為正，-1就

    def update(self):
        self.rect.x += self.speed
        if self.speed_sign == 1:  # 1 時就超右屏結束
            if self.rect.x > SCREEN_WIDTH:  # 超出屏幕結束
                self.kill()
        else:
            if self.rect.right < 0:  # -1 時就超左屏結束
                self.kill()


# 生成敵方坦克
class EnemyTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 0, 0), (0, 0, 50, 40))
        pygame.draw.rect(self.image, (255, 128, 50), (10, 10, 30, 20))
        pygame.draw.rect(self.image, (32, 32, 96), (20, 16, 40, 8))
        self.image = pygame.transform.flip(self.image, True, False)  # 和tank一樣的圖案，只是水平翻轉了
        # 初始化位置在超出右方屏的30位置，y方向隨機在50~screen_height-50中生成
        self.rect = self.image.get_rect(midleft=(SCREEN_WIDTH + 30, random.randint(50, SCREEN_HEIGHT - 50)))
        # 移動速度都是隨機的1~4
        self.speed = random.randint(1, 4)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:  # 超出屏幕或寿命结束
            self.kill()

    def shoot(self):
        return Bullet(self.rect.midleft[0], self.rect.midleft[1], -1)


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
        # 4. bullets group
        self.bullets = pygame.sprite.Group()
        # 5. enemy group
        self.enemies_group = pygame.sprite.Group()  # 創建一個敵方坦克的管理Group
        # 6. enemy bullets group
        self.enemies_bullets_group = pygame.sprite.Group()  # 創建一個敵方坦克子彈的管理Group
        # 變量:
        self.running = True
        self.current_time = pygame.time.get_ticks()
        self.next_bullet_time = 0  # 記錄發射時間的變量
        self.next_enemy_time = 0  # 記錄敵人生成時間的變量
        self.next_enemy_bullet_time = 0  # 記錄敵人子彈發射的變量
        # 常量:
        self.FPS = FPS
        self.MAX_BULLETS = MAX_BULLETS_NUM
        self.BULLET_DELTA_TIME = 100  # 控制相鄰子彈間發射的最小時間間隔
        self.ENEMY_DELTA_TIME = ENEMY_DELTA_TIME  # 控制敵人生生的最小時間間隔

    def start(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.handle_events()
            self.update()
            self.collision_detection()  # 碰撞檢測 TODO
            self.render()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # 生成子彈的函數
        self.check_space_key()
        # 生成敵人的函數
        self.generate_enemy()
        # 生成敵人子彈的函數
        self.generate_enemy_bullets()

    def update(self):
        # 更新
        self.tank.update()
        self.tree_group.update()
        self.bullets.update()  # 子彈Group統一自動更新，group中每一個子彈都自動做update()
        self.enemies_group.update()  # 敵人所有坦克自動向左移動
        self.enemies_bullets_group.update()  # 敵人所有子彈自動向左移動

    def render(self):
        # 渲染
        self.main_surface.fill((192, 192, 255))
        pygame.draw.rect(self.main_surface, (64, 128, 64), (0, 250, 600, 150))
        self.main_surface.blit(self.tree_group.image, self.tree_group.rect)
        self.main_surface.blit(self.tank.image, self.tank.rect)
        # 子彈Group統一自動渲染，group中每一個子彈都自動做self.main_surface.blit(self.image, self.rect)
        self.bullets.draw(self.main_surface)
        self.enemies_group.draw(self.main_surface)  # 敵人所有坦克自動渲染
        self.enemies_bullets_group.draw(self.main_surface)  # 敵人所有子彈自動渲染
        pygame.display.update()

    def collision_detection(self):
        # 敵方子彈有沒有打中我方坦克，若有，遊戲結束
        hit_tank_list = pygame.sprite.spritecollide(self.tank, self.enemies_bullets_group, False)
        if len(hit_tank_list) != 0:
            self.running = False

        # 我方子彈有沒有打中敵方坦克，若有，敵方坦克和子彈均消失
        hit_enemy_list = pygame.sprite.groupcollide(
            self.bullets, self.enemies_group, True, True,
            None
            # collided=pygame.sprite.collide_mask  #可以使用mask去代替
        )

    def check_space_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.current_time = pygame.time.get_ticks()
            if len(self.bullets.sprites()) < self.MAX_BULLETS and self.current_time >= self.next_bullet_time:
                self.next_bullet_time = self.current_time + self.BULLET_DELTA_TIME  # 控制子彈發射間隔
                bullet = self.tank.shoot()
                self.bullets.add(bullet)

        print(f"子彈數量: {len(self.bullets.sprites())}")

    def generate_enemy(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time >= self.next_enemy_time:
            self.next_enemy_time = self.current_time + self.ENEMY_DELTA_TIME
            enemy = EnemyTank()
            self.enemies_group.add(enemy)

        print(f"敵人數量: {len(self.enemies_group.sprites())}")

    def generate_enemy_bullets(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time >= self.next_enemy_bullet_time:
            self.next_enemy_bullet_time = self.current_time + random.randint(1000, ENEMY_BULLET_DELTA_TIME)
            for enemy in self.enemies_group.sprites():
                bullet = enemy.shoot()  # 坦克對象生成一個midright位置的子彈
                self.enemies_bullets_group.add(bullet)

        print(f"敵人子彈數量: {len(self.enemies_bullets_group.sprites())}")


if __name__ == '__main__':
    my_APP = Game()
    my_APP.start()
