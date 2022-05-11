import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('img/triton.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        # self.display_surface = pygame.display.get_surface()


    # def run(self):
        # self.display_surface.blit(self.image, (0, 0))
