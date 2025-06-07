import pygame
import random
import sys
import os
import time

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroid Game")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ASTEROID_COLOR = (160, 160, 160)
RED = (255, 0, 0)

# Load and scale images
SPACESHIP_IMG = pygame.image.load("spaceship.png")
SPACESHIP_IMG = pygame.transform.scale(SPACESHIP_IMG, (150, 150))

ASTEROID_IMG = pygame.image.load("asteroid.png")
ASTEROID_IMG = pygame.transform.scale(ASTEROID_IMG, (60, 60))

BROKEN_ASTEROID_IMG = pygame.image.load("asteroid_broken.png").convert_alpha()
BROKEN_ASTEROID_IMG = pygame.transform.scale(BROKEN_ASTEROID_IMG, (60, 60))

BULLET_IMG = pygame.image.load("bullet.png")
BULLET_IMG = pygame.transform.scale(BULLET_IMG, (35, 20))

HEART_IMAGE = pygame.Surface((25, 25), pygame.SRCALPHA)
pygame.draw.polygon(HEART_IMAGE, RED, [(12, 0), (25, 12), (12, 25), (0, 12)])
pygame.draw.circle(HEART_IMAGE, RED, (6, 6), 6)
pygame.draw.circle(HEART_IMAGE, RED, (18, 6), 6)

font = pygame.font.SysFont(None, 40)
HIGH_SCORE_FILE = "highscore.txt"

# Load sounds
gun_sound = pygame.mixer.Sound("gunfire.mp3")
defeat_sound = pygame.mixer.Sound("defeat.mp3")

# NEW: Load high score music for special effect
highscore_music = pygame.mixer.Sound("highscore_music.mp3")

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

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.size = 30
        self.speed = 6

    def draw(self):
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

class Bullet:
    def __init__(self, x, y):
        self.x = x - BULLET_IMG.get_width() // 2
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, BULLET_IMG.get_width(), BULLET_IMG.get_height())

    def update(self):
        self.y -= 10
        self.rect.y = self.y

    def draw(self):
        screen.blit(BULLET_IMG, (self.x, self.y))

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

    def draw(self):
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

def draw_hearts(lives):
    for i in range(lives):
        screen.blit(HEART_IMAGE, (WIDTH - 30 * (i + 1), 10))

def draw_button(text, x, y, w, h):
    pygame.draw.rect(screen, WHITE, (x, y, w, h), 2)
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))
    return pygame.Rect(x, y, w, h)

def main():
    player = Player()
    bullets = []
    asteroids = []
    asteroid_timer = 0
    bullet_timer = 0
    bullet_delay = 10
    lives = 5
    destroyed = 0
    game_over = False
    replay_button_rect = None
    high_score = load_high_score()

    start_time = time.time()
    level = 1
    level_display_timer = 60  # 1 second at 60 FPS
    last_level = level

    show_congrats = False
    new_highscore_achieved = False
    highscore_music_played = False

    while True:
        clock.tick(FPS)
        screen.fill(BLACK)
        keys = pygame.key.get_pressed()

        current_time = time.time()
        elapsed_time = current_time - start_time

        # Level logic
        if elapsed_time > 180:
            show_congrats = True
            game_over = True
        elif elapsed_time > 120:
            level = 3
        elif elapsed_time > 60:
            level = 2
        else:
            level = 1

        if level != last_level:
            level_display_timer = 60
            last_level = level

        asteroid_speed = {1: (2, 5), 2: (4, 7), 3: (6, 9)}[level]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if replay_button_rect and replay_button_rect.collidepoint(event.pos):
                    return main()

        if not game_over:
            player.move(keys)

            if keys[pygame.K_SPACE]:
                bullet_timer += 1
                if bullet_timer >= bullet_delay:
                    bullets.append(Bullet(player.x + 35, player.y - player.size))
                    bullet_timer = 0
                    gun_sound.play()
            else:
                bullet_timer = bullet_delay

            asteroid_timer += 1
            if asteroid_timer > 30:
                asteroids.append(Asteroid(random.randint(*asteroid_speed)))
                asteroid_timer = 0

            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)

            for asteroid in asteroids[:]:
                if not asteroid.broken:
                    asteroid.update()
                    if asteroid.y - asteroid.radius > HEIGHT:
                        asteroids.remove(asteroid)
                        lives -= 1
                        if lives <= 0:
                            game_over = True
                            if destroyed > high_score:
                                high_score = destroyed
                                save_high_score(high_score)
                                new_highscore_achieved = True
                            else:
                                defeat_sound.play()
                    elif asteroid.get_rect().colliderect(player.get_rect()):
                        game_over = True
                        if destroyed > high_score:
                            high_score = destroyed
                            save_high_score(high_score)
                            new_highscore_achieved = True
                        else:
                            defeat_sound.play()
                else:
                    asteroid.update()
                    if asteroid.is_faded():
                        asteroids.remove(asteroid)

            for asteroid in asteroids[:]:
                if asteroid.broken:
                    continue
                for bullet in bullets[:]:
                    if asteroid.get_rect().colliderect(bullet.rect):
                        bullets.remove(bullet)
                        asteroid.broken = True
                        asteroid.alpha = 255
                        destroyed += 1
                        break

        player.draw()
        for bullet in bullets:
            bullet.draw()
        for asteroid in asteroids:
            asteroid.draw()

        draw_hearts(lives)
        score_text = font.render(f"Destroyed: {destroyed}", True, WHITE)
        screen.blit(score_text, (10, 10))

        highscore_text = font.render(f"High Score: {high_score}", True, WHITE)
        screen.blit(highscore_text, (10, 50))

        # NEW: Level text in center fade effect
        if level_display_timer > 0:
            level_text = font.render(f"LEVEL {level}", True, WHITE)
            text_surface = level_text.copy()
            alpha = int((level_display_timer / 60) * 255)
            text_surface.set_alpha(alpha)
            screen.blit(text_surface, (WIDTH // 2 - level_text.get_width() // 2, HEIGHT // 2 - 100))
            level_display_timer -= 1

        if show_congrats:
            congrats_text = font.render("CONGRATULATIONS YOU WON", True, WHITE)
            screen.blit(congrats_text, (WIDTH // 2 - 200, HEIGHT // 2 - 60))

        if game_over and new_highscore_achieved and not highscore_music_played:
            highscore_music.play()
            highscore_music_played = True

        if game_over and not show_congrats:
            y_offset = HEIGHT // 2 - 100

            if new_highscore_achieved:
                highscore_text_msg = font.render("NEW HIGH SCORE!", True, WHITE)
                screen.blit(highscore_text_msg, (WIDTH // 2 - highscore_text_msg.get_width() // 2, y_offset))
                y_offset += 60

            over_text = font.render("GAME OVER", True, WHITE)
            screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, y_offset))
            y_offset += 60

            replay_button_rect = draw_button("Play Again", WIDTH // 2 - 80, y_offset, 160, 50)

        level_text_top = font.render(f"LEVEL {level}", True, WHITE)
        screen.blit(level_text_top, (WIDTH // 2 - level_text_top.get_width() // 2, 10))

        pygame.display.flip()

if __name__ == "__main__":
    main()
