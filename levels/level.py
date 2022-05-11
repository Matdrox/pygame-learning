import pygame
from levels.level1 import Level1
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.tiles = Camera_group_y()
        self.obstacle_sprites = pygame.sprite.Group()
        Level1((0, 0), [self.tiles])
        self.player = Player((0, 0), [self.tiles], self.obstacle_sprites)

    def run(self):
        self.tiles.draw(self.player)
        self.tiles.update()
        # self.display_surface.blit(self.image, (0, 0))

class Camera_group_y(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.w = self.display_surface.get_size()[0] // 2.
        self.h = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def draw(self, player):
        self.offset.x = player.rect.centerx - self.w
        self.offset.y = player.rect.centery - self.h

        for sprite in self.sprites():
        # for sprite in sorted(self.sprites(), key= lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)