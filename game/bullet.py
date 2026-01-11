import pygame

from .assets import BULLET_IMG


class Bullet:
    def __init__(self, x, y):
        self.x = x - BULLET_IMG.get_width() // 2
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, BULLET_IMG.get_width(), BULLET_IMG.get_height())

    def update(self):
        self.y -= 10
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(BULLET_IMG, (self.x, self.y))
