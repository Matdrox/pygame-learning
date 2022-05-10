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
bg_image = pygame.image.load('img/maps/map.png').convert()

move_speed = 25
velocity_x = 0
velocity_y = 0
delta_time = 0
speed = 0

player_location = [50, 50]
scroll = [0, 0]
scroll_temp = [0, 0]

player_rect = pygame.Rect(
    50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)

while True:
    delta_time = clock.tick(60)
    speed = 1/float(delta_time)

    display.fill(0)
    display.blit(bg_image, (-scroll[0], -scroll[1]))

    scroll[0] += (player_rect.x - scroll[0] -
                  (display.get_width()/2-player_rect.width/2))/10
    scroll[1] += (player_rect.y - scroll[1] -
                  (display.get_height()/2-player_rect.height/2))/10
    scroll_temp = scroll.copy()
    scroll_temp[0] = int(scroll[0])
    scroll_temp[1] = int(scroll[1])

    player_movement = [0, 0]
    player_movement[0] += velocity_x * speed
    player_movement[1] += velocity_y * speed

    player_rect = pygame.Rect.move(player_rect, player_movement)
    display.blit(player_image, (player_rect.x -
                 scroll[0], player_rect.y-scroll[1]))

    velocity_x, velocity_y = 0, 0
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] or keys[K_a]:
        velocity_x = -move_speed
    if keys[K_RIGHT] or keys[K_d]:
        velocity_x = move_speed
    if keys[K_UP] or keys[K_w]:
        velocity_y = -move_speed
    if keys[K_DOWN] or keys[K_s]:
        velocity_y = move_speed
    # if velocity_x != 0 and velocity_y != 0:
        # velocity_x *= 0.7071
        # velocity_y *= 0.7071

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    # pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.update()

