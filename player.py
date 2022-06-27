from matplotlib import scale
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('img/triton.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)    # hitbox
        self.hb = self.rect.inflate(0, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1  # Update for grid-based movement
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1  # Update for grid-based movement
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1  # Update for grid-based movement
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1  # Update for grid-based movement
        else:
            self.direction.y = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hb.x += self.direction.x * speed
        self.collision('horizontal')
        self.hb.y += self.direction.y * speed
        self.collision('vertival')
        self.rect.center = self.hb.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hb.colliderect(self.hb):
                    if self.direction.x < 0:    # left
                        self.hb.left = sprite.hb.right
                    if self.direction.x > 0:    # right
                        self.hb.right = sprite.hb.left
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hb.colliderect(self.hb):
                    if self.direction.y < 0:    # up
                        self.hb.top = sprite.hb.bottom
                    if self.direction.y > 0:    # left
                        self.hb.bottom = sprite.hb.top

    def update(self):
        self.input()
        self.move(self.speed)
