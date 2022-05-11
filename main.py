import pygame
import sys
from pygame.locals import *
from settings import *
from levels.level import Level
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mytholos')
        self.screen = pygame.display.set_mode(WINDOW_SIZE, SCALED)
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.sprites = pygame.sprite.Group()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.screen.fill(0)
            self.level.run()

            pygame.display.update()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()

player_image = pygame.image.load('img/triton.png')
bg_image = pygame.image.load('img/maps/map.png').convert()

move_speed = 1.8

player_location = [50, 50]
scroll = [0, 0]

player_rect = pygame.Rect(
    50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)


def gameWindow():
    # pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.update()


run = True
while run:
    clock.tick(60)

    display.fill(0)
    display.blit(bg_image, (-scroll[0], -scroll[1]))

    scroll[0] += (player_rect.x - scroll[0] -
                  (display.get_width()/2-player_rect.width/2))/7
    scroll[1] += (player_rect.y - scroll[1] -
                  (display.get_height()/2-player_rect.height/2))/7

    player_movement = [0, 0]
    player_rect = pygame.Rect.move(player_rect, player_movement)

    display.blit(player_image, (player_rect.x -
                 scroll[0], player_rect.y-scroll[1]))

    velocity_x, velocity_y = 0, 0
    keys = pygame.key.get_pressed()

    if keys[K_LEFT] or keys[K_a]:
        player_rect.x -= move_speed
    if keys[K_RIGHT] or keys[K_d]:
        player_rect.x += move_speed
    if keys[K_UP] or keys[K_w]:
        player_rect.y -= move_speed
    if keys[K_DOWN] or keys[K_s]:
        player_rect.y += move_speed

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
pygame.quit()
