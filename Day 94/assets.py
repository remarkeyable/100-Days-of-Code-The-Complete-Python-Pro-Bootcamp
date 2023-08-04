import pygame
import os

import random

pygame.font.init()

BG_COLOR = (14, 41, 84)

# Aliens
ALIEN1 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien1.png')), 270)
ALIEN2 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien2.png')), 270)
ALIEN3 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien3.png')), 270)

# Ship
SHIP = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 90)
SPACE_SHIP = pygame.transform.scale(SHIP, (60, 60))
THE_BUL = []

# RESIZED ALIENS
ALIEN_1 = pygame.transform.scale(ALIEN1, (40, 40))
ALIEN_2 = pygame.transform.scale(ALIEN2, (60, 60))
ALIEN_3 = pygame.transform.scale(ALIEN3, (80, 80))

# Background
BG = pygame.image.load(os.path.join('Assets', 'space_bg.png'))


class Ship:
    def __abs__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.ship_image = self.mask.to_surface()

    def draw_ship(self, window):
        window.blit(self.image, (self.x, self.y))


class Laser:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.bullet_image = self.mask.to_surface()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))


class Aliens:
    def __init__(self, image):
        self.x = random.randrange(25, 500)
        self.y = random.randrange(-100, -10)
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.alien_image = self.mask.to_surface()

    def produce_aliens(self, window):
        window.blit(self.image, (self.x, self.y))


class Assets:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Space Invader')
        self.fps = 30
        self.ship = pygame.Rect(295, 500, 60, 60)
        self.bullet = pygame.Rect(self.ship.x, self.ship.y, 60, 60)
        self.fired = []
        self.aliens = []
        self.run = True
        self.num = 0
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('comicsans', 15)
        self.score = 0
        self.lives = 5
        self.bullet_mask = pygame.mask.from_surface(BULLET)
        self.bullet_image = self.bullet_mask.to_surface()

    def ship_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.ship.x > 0:
            self.ship.x -= 10
            self.bullet.x -= 10
        elif keys_pressed[pygame.K_RIGHT] and self.ship.x < 550:
            self.ship.x += 10
            self.bullet.x += 10
        elif keys_pressed[pygame.K_UP] and self.ship.y > 0:
            self.ship.y -= 10
            self.bullet.y -= 10
        elif keys_pressed[pygame.K_DOWN] and self.ship.y < 550:
            self.ship.y += 10
            self.bullet.y += 10

    def update_window(self):
        self.window.blit(BG, (0, 0))
        self.fire_bullet()
        self.the_aliens()
        self.window.blit(SPACE_SHIP, (self.ship.x, self.ship.y))
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(lives_text, (10, 10))
        self.window.blit(score_text, (600 - score_text.get_width() - 10, 10))
        pygame.display.update()

    def fire_bullet(self):
        for i in self.fired:
            i.draw(self.window)
            i.y -= 15
            if i.y < 0:
                self.fired.remove(i)

    def append_aliens(self):
        random_aliens = [ALIEN_1, ALIEN_2, ALIEN_3]
        if len(self.aliens) == 0:
            for i in range(5):
                eyl = Aliens(random.choice(random_aliens))
                self.aliens.append(eyl)

    def the_aliens(self):
        for i in self.aliens:
            i.produce_aliens(self.window)
            i.y += 1
            if i.y > 550:
                self.aliens.remove(i)
            for j in self.fired:
                if self.detect_collision(i, j):
                    self.aliens.remove(i)
                    self.score += 1  # if self.detect_collision(i,self.ship)

    def detect_collision(self, alien, bullet):
        off_set_x = bullet.x - alien.x
        off_set_y = bullet.y - alien.y
        return alien.mask.overlap(bullet.mask, (off_set_x, off_set_y)) != None

    def the_ship(self):
        ship = Ship(SPACE_SHIP)