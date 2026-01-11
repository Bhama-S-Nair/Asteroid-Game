import pygame

from .config import RED

# Initialize variables
SPACESHIP_IMG = None
ASTEROID_IMG = None
BROKEN_ASTEROID_IMG = None
BULLET_IMG = None
HEART_IMAGE = None

gun_sound = None
defeat_sound = None
highscore_music = None


def load_assets():
    global SPACESHIP_IMG, ASTEROID_IMG, BROKEN_ASTEROID_IMG, BULLET_IMG
    global HEART_IMAGE, gun_sound, defeat_sound, highscore_music

    SPACESHIP_IMG = pygame.transform.scale(pygame.image.load("../assets/spaceship.png"), (150, 150))
    ASTEROID_IMG = pygame.transform.scale(pygame.image.load("../assets/asteroid.png"), (60, 60))
    BROKEN_ASTEROID_IMG = pygame.transform.scale(
        pygame.image.load("../assets/asteroid_broken.png").convert_alpha(), (60, 60))
    BULLET_IMG = pygame.transform.scale(pygame.image.load("../assets/bullet.png"), (35, 20))

    gun_sound = pygame.mixer.Sound("../assets/gunfire.mp3")
    defeat_sound = pygame.mixer.Sound("../assets/defeat.mp3")
    highscore_music = pygame.mixer.Sound("../assets/highscore_music.mp3")

    HEART_IMAGE = pygame.Surface((25, 25), pygame.SRCALPHA)
    pygame.draw.polygon(HEART_IMAGE, RED, [(12, 0), (25, 12), (12, 25), (0, 12)])
    pygame.draw.circle(HEART_IMAGE, RED, (6, 6), 6)
    pygame.draw.circle(HEART_IMAGE, RED, (18, 6), 6)
