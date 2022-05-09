import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Mytholos')

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            print()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(144)
