import pygame
import time
import random

pygame.init()


# 1. 遊戲對象的基類，繼承類必須定義rect和image.
class Player(pygame.sprite.Sprite):  # 新遊戲對象繼承基類
    def __init__(self, name):
        super().__init__()
        self.image = pygame.image.load("./resources/image/bluebird-downflap.png")  # 定義image名稱的成員，用於顯示
        self.rect = self.image.get_rect()  # 定義rect名稱的成員，用於定立和碰撞檢測，大小一般和image大小相同
        # 这样get_rect()後的原點在(0,0)
        # 若想初始化角度的位置在其他地方，可以為rect.x和rect.y賦值
        self.rect.x = 100 + random.randint(100, 200)
        self.rect.y = 102 + random.randint(100, 200)
        print(f"{name}的初始化位置是({self.rect.x, self.rect.y})")

        # 除了必要元素，可加入自己的邏輯
        self.name = name

    #  可以override基類的update() function.
    #  用於控制角度行为的方法
    #  若有多個角色時，可以把他們組成Groups，由Group統一對Group中成員組成update()
    def update(self):
        self.rect.x += 1
        print(f"{self.name} rect.x is {self.rect.x}")

    def other_fun(self):  # 其他邏輯
        pass






print("----------------------------------------------------------------------")
# 2. 用於管理多個角度的容器類，支持批量更新、繪圖和碰撞檢測
sprites_groups = pygame.sprite.Group()
# 2.1 加入角色對象，add(*sprites) -> None
player1 = Player("player1")
player2 = Player("player2")
player3 = Player("player3")
sprites_groups.add(player1)  # group 包含player1
sprites_groups.add([player2, player3])  # group 包今player1,2,3

# 2.2 查看group中包含哪些sprite，返回其對象的名稱。sprites() -> sprite_list
print(f"2.2:  Group中包含了: {sprites_groups.sprites()}")

# 2.3 從Group中移除某個對象，remove(*sprites) -> None
sprites_groups.remove(player1)
print(f"2.3:  移除後，Group中包含了: {sprites_groups.sprites()}")

# 2.4 判斷Group中有沒有特定的sprite，has(*sprites) -> bool
print(f"2.4:  group中有沒有player1: {sprites_groups.has(player1)}")
print(f"2.4:  group中有沒有player2: {sprites_groups.has(player2)}")

# 2.5 對Group中所有成員進行批量update()，update(*args, **kwargs) -> None
sprites_groups.update()  # group中每個對象都會進行update

# 2.6 把group中所有obj畫到指定畫面上，draw(Surface, bgsurf=None, special_flags=0) -> List[Rect]
main_surface = pygame.display.set_mode((480, 640))
sprites_groups.draw(main_surface)  # group中所冈對象都會把其self.image畫到main_surface中，位置由self.rect決定
pygame.display.update()
time.sleep(5)

# 2.7 清空group中所有成員
sprites_groups.empty()
print(f"2.7:  清空後，Group中包含了: {sprites_groups.sprites()}")






print("----------------------------------------------------------------------")
# 3. 碰撞檢測
bird_1 = Player("bird1")
tree_1 = Player("tree1")
tree_2 = Player("tree2")

tree_group = pygame.sprite.Group()
tree_group.add(tree_1)
tree_group.add(tree_2)

# 3.1 利用rect檢測兩個sprite間的碰撞
# collide_rect(left, right) -> bool
if_two_obj_collide_rect = pygame.sprite.collide_rect(bird_1, tree_1)  # 使用self.rect去比較
print(f"bird1和tree1使用rect判斷下有沒有產生碰撞:{if_two_obj_collide_rect}")

# 3.2 利用circle檢測兩個sprite間的碰撞
# collide_circle(left, right) -> bool
# 需要角色具有self.radius屬性，否則將使用rect的外接圓去代替
if_two_obj_collide_circle = pygame.sprite.collide_circle(bird_1, tree_1)
print(f"bird1和tree1使用circle判斷下有沒有產生碰撞:{if_two_obj_collide_circle}")

# 3.3 利用mask檢測兩個sprite間的碰撞，最精確
# collide_mask(sprite1, sprite2) -> (int, int)  # 返回碰撞點坐標
# collide_mask(sprite1, sprite2) -> None
# 比較碰撞的obj需要擁有self.mask的屬性，否則將會根據圖像自動生成(使用pygame.mask.from_surface())
mask_collide_point_or_None = pygame.sprite.collide_mask(bird_1, tree_1)
if mask_collide_point_or_None:
    print(f"使用mask判斷，發生碰撞的點在:{mask_collide_point_or_None}")
else:
    print("使用mask判斷，沒有發生碰撞")

# 3.4 檢測一個sprite與另一個group間所有sprites的碰撞。注意，这里會使用rect的方法進行碰撞比較
# spritecollide(sprite, group, dokill, collided = None) -> Sprite_list
# 判斷bird_1有沒有和tree_group相撞，返回在group中有被碰撞的sprites[].
hit_list = pygame.sprite.spritecollide(bird_1, tree_group, False)
print(f"Tree Group中與bird1產生碰撞的sprites有:{hit_list}")
# 使用者可以通過for hit in hit_list:去遍歷所有被撞的sprite class obj.
# for hit in hit_list: # 就可以把list中所以有sprite進行訪問，例如
#     print(hit.name)

# 3.5 檢測兩個group間的碰撞
# groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict
# 若collided不添加，默認使用self.rect去比較
# pygame.sprite.groupcollide() ‌返回一个字典‌，格式为：
# {group1_sprite: [group2_sprite1, group2_sprite2, ...], ...}
bird_group = pygame.sprite.Group(bird_1)
collisions = pygame.sprite.groupcollide(
    bird_group, tree_group, False, False,
    None
    # collided=pygame.sprite.collide_mask  #可以使用mask去代替
)
# 可通過for bird, trees in collisions.items():獲取所有的組合
# print(f"碰撞的組合為:{collisions}")
# for bird, trees in collisions.items():
#     for tree in trees:
#         print(f"{bird.name} collide in {tree.name}")
pygame.quit()
