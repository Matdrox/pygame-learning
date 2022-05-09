import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Mytholos')

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.transform.scale(pygame.image.load('img/triton.png'), (128, 128))

while True:
    screen.blit(player_image, (50, 50))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(144)
