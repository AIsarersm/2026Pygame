import pygame


class Button:
    def __init__(self, x, y, image, scale, name):
        self.name = name
        self.image = image
        self.image = pygame.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def checkifclick(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return self.clicked
