import pygame
from pygame.sprite import Sprite
from src.utils import load_image


class Platform(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load_image("assets/images/platform.png", colorkey=-1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
