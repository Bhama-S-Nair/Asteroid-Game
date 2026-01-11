import os

import pygame

from .config import HIGH_SCORE_FILE, font, WHITE


def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as f:
            try:
                return int(f.read())
            except:
                return 0
    return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, "w") as f:
        f.write(str(score))

def draw_hearts(screen, heart_image, lives, WIDTH):
    for i in range(lives):
        screen.blit(heart_image, (WIDTH - 30 * (i + 1), 10))

def draw_button(screen, text, x, y, w, h):
    pygame.draw.rect(screen, WHITE, (x, y, w, h), 2)
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))
    return pygame.Rect(x, y, w, h)
