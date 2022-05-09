import pygame
import sys
from pygame.locals import *
from math import sqrt

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Mytholos')

WINDOW_SIZE = (800, 600)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

player_image = pygame.transform.scale(
    pygame.image.load('img/triton.png'), (128, 128))

move_speed = 5
moving_left = False
moving_right = False
moving_up = False
moving_down = False

player_location = [50, 50]

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)


while True:
    screen.fill(0)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.blit(player_image, player_location)
    if moving_left:
        if moving_up or moving_down:
            player_location[0] -= move_speed*0.7071
        else:
            player_location[0] -= move_speed
    if moving_right:
        if moving_up or moving_down:
            player_location[0] += move_speed*0.7071
        else:
            player_location[0] += move_speed
    if moving_up:
        if moving_left or moving_right:
            player_location[1] -= move_speed*0.7071
        else:
            player_location[1] -= move_speed
    if moving_down:
        if moving_left or moving_right:
            player_location[1] += move_speed*0.7071
        else:
            player_location[1] += move_speed
    
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 255, 0), test_rect)
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False
        
            
            

    pygame.display.update()
    clock.tick(144)
