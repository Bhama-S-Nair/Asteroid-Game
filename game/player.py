import pygame

from .config import WIDTH, HEIGHT

SPACESHIP_IMG = pygame.image.load("./assets/spaceship.png")
SPACESHIP_IMG = pygame.transform.scale(SPACESHIP_IMG, (150, 150))
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.size = 30
        self.speed = 6

    def draw(self, screen):
        screen.blit(SPACESHIP_IMG, (self.x - 40, self.y - 40))

    def move(self, keys):
        if keys[pygame.K_a] and self.x - self.size > 0:
            self.x -= self.speed
        if keys[pygame.K_d] and self.x + self.size < WIDTH:
            self.x += self.speed
        if keys[pygame.K_w] and self.y - self.size > 0:
            self.y -= self.speed
        if keys[pygame.K_s] and self.y + self.size < HEIGHT:
            self.y += self.speed

    def get_rect(self):
        return pygame.Rect(self.x - 40, self.y - 40, 150, 150)
