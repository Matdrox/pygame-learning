from curses import KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP
import pygame
import sys
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Mytholos')

WINDOW_SIZE = (1200, 800)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface((300, 200))

player_image = pygame.image.load('img/triton.png')
bg_image = pygame.image.load('img/map.png').convert()

move_speed = 1.5
moving_left = False
moving_right = False
moving_up = False
moving_down = False

player_location = [50, 50]
scroll = [0, 0]

player_rect = pygame.Rect(
    50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while True:
    display.fill(0)
    display.blit(bg_image, (-scroll[0], -scroll[1]))

    scroll[0] += (player_rect.x - scroll[0] -
                  (display.get_width()/2-player_rect.width/2))/12
    scroll[1] += (player_rect.y - scroll[1] -
                  (display.get_height()/2-player_rect.height/2))/12

    player_movement = [0, 0]

    if moving_left:
        if moving_up or moving_down:
            player_movement[0] -= move_speed*0.7071
        else:
            player_movement[0] -= move_speed
    if moving_right:
        if moving_up or moving_down:
            player_movement[0] += move_speed*0.7071
        else:
            player_movement[0] += move_speed
    if moving_up:
        if moving_left or moving_right:
            player_movement[1] -= move_speed*0.7071
        else:
            player_movement[1] -= move_speed
    if moving_down:
        if moving_left or moving_right:
            player_movement[1] += move_speed*0.7071
        else:
            player_movement[1] += move_speed

    player_rect = pygame.Rect.move(player_rect, player_movement)
    display.blit(player_image, (player_rect.x -
                 scroll[0], player_rect.y-scroll[1]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moving_left = True
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = True
            if event.key == K_UP or event.key == K_w:
                moving_up = True
            if event.key == K_DOWN or event.key == K_s:
                moving_down = True

        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moving_left = False
            if event.key == K_RIGHT or event.key == K_d:
                moving_right = False
            if event.key == K_UP or event.key == K_w:
                moving_up = False
            if event.key == K_DOWN or event.key == K_s:
                moving_down = False

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update()
    clock.tick(144)
