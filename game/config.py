import pygame

# Screen
WIDTH, HEIGHT = 600, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ASTEROID_COLOR = (160, 160, 160)
RED = (255, 0, 0)

# High Score File
HIGH_SCORE_FILE = "highscore.txt"

# Font
pygame.font.init()
font = pygame.font.SysFont(None, 40)
