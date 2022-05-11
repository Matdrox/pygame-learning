import pygame
from levels.level1 import Level1
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        Level1((0, 0), [self.sprites])
        self.player = Player((0, 0), [self.sprites], self.obstacle_sprites)

    def run(self):
        self.sprites.draw(self.display_surface)
        self.sprites.update()
        # self.display_surface.blit(self.image, (0, 0))