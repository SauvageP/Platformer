import pygame

from src.utils import load_image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = load_image("assets/images/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0.5)
        self.jump_speed = -10
        self.on_ground = False

    def update(self, platforms):
        self.velocity += self.acceleration
        self.rect.move_ip(self.velocity.x, self.velocity.y)
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0 and self.rect.bottom <= platform.rect.bottom + self.velocity.y:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                elif self.velocity.y < 0 and self.rect.top >= platform.rect.top + self.velocity.y:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0

        if not self.on_ground:
            self.velocity.y = min(self.velocity.y, 10)

    def move_left(self):
        self.velocity.x = -5

    def move_right(self):
        self.velocity.x = 5

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_speed
