import pygame

class Level1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('img/maps/map.png').convert()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
