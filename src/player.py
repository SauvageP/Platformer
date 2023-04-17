import pygame
from pygame.sprite import Sprite
from src.utils import load_image


class Player(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load_image("assets/images/player.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed_x = 0
        self.speed_y = 0

    def update(self, platforms):
        self.speed_y += 0.5

        self.rect.x += self.speed_x
        self.collide(platforms, "x")

        self.rect.y += self.speed_y
        self.collide(platforms, "y")

    def move_left(self):
        self.speed_x = -5

    def move_right(self):
        self.speed_x = 5

    def jump(self):
        self.speed_y = -12

    def collide(self, platforms, axis):
        for platform in pygame.sprite.spritecollide(self, platforms, False):
            if axis == "x":
                if self.speed_x > 0:
                    self.rect.right = platform.rect.left
                elif self.speed_x < 0:
                    self.rect.left = platform.rect.right
                self.speed_x = 0
            elif axis == "y":
                if self.speed_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.speed_y = 0
                elif self.speed_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.speed_y = 0
