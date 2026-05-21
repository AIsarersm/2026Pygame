import pygame


class FlappyMark:
    def __init__(self, scale):
        self.zero = pygame.image.load('resources/image/0.png').convert_alpha()
        self.one = pygame.image.load('resources/image/1.png').convert_alpha()
        self.two = pygame.image.load('resources/image/2.png').convert_alpha()
        self.three = pygame.image.load('resources/image/3.png').convert_alpha()
        self.four = pygame.image.load('resources/image/4.png').convert_alpha()
        self.five = pygame.image.load('resources/image/5.png').convert_alpha()
        self.six = pygame.image.load('resources/image/6.png').convert_alpha()
        self.seven = pygame.image.load('resources/image/7.png').convert_alpha()
        self.eight = pygame.image.load('resources/image/8.png').convert_alpha()
        self.nine = pygame.image.load('resources/image/9.png').convert_alpha()

        self.zero = pygame.transform.scale_by(self.zero, scale)
        self.one = pygame.transform.scale_by(self.one, scale)
        self.two = pygame.transform.scale_by(self.two, scale)
        self.three = pygame.transform.scale_by(self.three, scale)
        self.four = pygame.transform.scale_by(self.four, scale)
        self.five = pygame.transform.scale_by(self.five, scale)
        self.six = pygame.transform.scale_by(self.six, scale)
        self.seven = pygame.transform.scale_by(self.seven, scale)
        self.eight = pygame.transform.scale_by(self.eight, scale)
        self.nine = pygame.transform.scale_by(self.nine, scale)

        self.image_list = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]

        self.width, self.height = self.zero.get_size()

    def get_num_surface_obj(self, num:int):
        str_num = str(num)
        count_digit_number = len(str_num)  # 9 -> "9" ->1個位, 11->"11"->2個位
        join_image = pygame.Surface((count_digit_number * self.width, self.height), pygame.SRCALPHA)
        for i in range(count_digit_number):  # 個位開始，到十位，到百位
            # 如"43"  -> "43"[0] = "3" --> 3
            #         -> "43"[1] = "4" -->4
            digit = int(str_num[i])
            join_image.blit(self.image_list[digit], (i * self.width, 0))

        return join_image
