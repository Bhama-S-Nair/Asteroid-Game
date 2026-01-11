import random

import pygame

from .config import WIDTH

ASTEROID_IMG = pygame.image.load("assets/asteroid.png")
ASTEROID_IMG = pygame.transform.scale(ASTEROID_IMG, (60, 60))

BROKEN_ASTEROID_IMG = pygame.image.load("assets/asteroid_broken.png")
BROKEN_ASTEROID_IMG = pygame.transform.scale(BROKEN_ASTEROID_IMG, (60, 60))
class Asteroid:
    def __init__(self, speed):
        self.radius = 30
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = 0 - self.radius
        self.speed = speed
        self.broken = False
        self.alpha = 255

    def update(self):
        if not self.broken:
            self.y += self.speed
        else:
            self.alpha -= 5
            if self.alpha < 0:
                self.alpha = 0

    def draw(self, screen):
        if not self.broken:
            screen.blit(ASTEROID_IMG, (self.x - 30, self.y - 30))
        else:
            img = BROKEN_ASTEROID_IMG.copy()
            img.set_alpha(self.alpha)
            screen.blit(img, (self.x - 30, self.y - 30))

    def get_rect(self):
        return pygame.Rect(self.x - 30, self.y - 30, 60, 60)

    def is_faded(self):
        return self.broken and self.alpha == 0
