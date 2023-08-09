import pygame
import os

import random

pygame.init()
pygame.font.init()

BG_COLOR = (14, 41, 84)

# Aliens
ALIEN1 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien1.png')), 270)
ALIEN2 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien2.png')), 270)
ALIEN3 = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien3.png')), 270)

ALIEN_IMAGES = {"ALIEN_1": pygame.transform.scale(ALIEN1, (50, 50)),
                "ALIEN_2": pygame.transform.scale(ALIEN2, (50, 50)),
                "ALIEN_3": pygame.transform.scale(ALIEN3, (50, 50))}
A_BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'alien_bullet.png')), 180)
ALIEN_BULLET = pygame.transform.scale(A_BULLET, (12, 12))

# Ship
SHIP = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
SPACE_SHIP = pygame.transform.scale(SHIP, (60, 60))
BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 90)

# Background
BG = pygame.image.load(os.path.join('Assets', 'space_bg.png'))

# SOUND FX
BULLET_SHIP_PATH = "Assets/sounds/hitt.wav"
BULLET_SHIP_SOUND = pygame.mixer.Sound(BULLET_SHIP_PATH)
LASER_PATH = "Assets/sounds/laser.wav"
LASER_SOUND = pygame.mixer.Sound(LASER_PATH)
ALIEN_CRASH_PATH = "Assets/sounds/alien_crash2.wav"
ALIEN_CRASH_SOUND = pygame.mixer.Sound(ALIEN_CRASH_PATH)
HIT_SHIP_PATH = "Assets/sounds/hit_ship.wav"
HIT_SHIP_SOUND = pygame.mixer.Sound(HIT_SHIP_PATH)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, alien):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 10):
            img = pygame.image.load(f"Assets/explosions/{alien}/{num}.png")
            img = pygame.transform.rotate(pygame.transform.scale(img, (50, 50)), 90)
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect = [x, y]
        self.counter = 0

    def update(self):
        speed = 2
        self.counter += 1
        if self.counter >= speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
        if self.index >= len(self.images) - 1 and self.counter >= speed:
            self.kill()


class TheShip:
    def __init__(self, x, y, image):
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
    def __init__(self):
        self.x = random.randrange(25, 500)
        self.y = random.randrange(-100, -10)
        self.random_alien = random.choice(["ALIEN_1", "ALIEN_2", "ALIEN_3"])
        self.image = ALIEN_IMAGES[self.random_alien]
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
        self.alien_laser = []
        self.run = True
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('comicsans', 15)
        self.score = 0
        self.lives = 5
        self.bullet_mask = pygame.mask.from_surface(BULLET)
        self.bullet_image = self.bullet_mask.to_surface()
        self.alien_refresh = 0
        self.alien_count = 4
        self.explosion_group = pygame.sprite.Group()

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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "space":
                    LASER_SOUND.play()
                    en = Laser(self.bullet.x, self.bullet.y, BULLET)
                    self.fired.append(en)

    def update_window(self):
        self.window.blit(BG, (0, 0))
        self.alien_shoot_laser()
        self.the_aliens()
        self.the_ship()
        self.fire_bullet()
        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(lives_text, (10, 10))
        self.window.blit(score_text, (600 - score_text.get_width() - 10, 10))

        self.explosion_group.draw(self.window)
        self.explosion_group.update()
        pygame.display.update()

    def fire_bullet(self):
        for i in self.fired:
            i.draw(self.window)
            i.y -= 15
            if i.y < 0:
                self.fired.remove(i)

    def append_aliens(self):
        chances = random.randrange(0, 100)
        if chances == 22:
            for i in range(0, 1):
                eyl = Aliens()
                self.aliens.append(eyl)

    def the_aliens(self):
        for i in self.aliens:
            i.produce_aliens(self.window)
            i.y += 1
            if self.detect_collision(i, self.the_ship()):
                self.lives -= 1
                HIT_SHIP_SOUND.play()
                # detect if the ship is on the right side or left side of the alien
                if self.ship.x >= i.x:
                    self.ship.x += 50
                    self.bullet.x += 50
                if self.ship.x < i.x:
                    self.ship.x -= 50
                    self.bullet.x -= 50
            if i.y > 600:
                self.aliens.remove(i)
            for j in self.fired:
                if self.detect_collision(i, j):
                    ALIEN_CRASH_SOUND.play()
                    self.aliens.remove(i)
                    self.score += 1
                    explosion = Explosion(i.x, i.y, i.random_alien)
                    self.explosion_group.add(explosion)

            chances = random.randrange(0, 200)
            for k in range(0, 1):
                if chances == 22:
                    laser = self.alien_shoot(i.x + 19, i.y +12)
                    self.alien_laser.append(laser)





    def detect_collision(self, alien, target):
        off_set_x = target.x - alien.x
        off_set_y = target.y - alien.y
        return alien.mask.overlap(target.mask, (off_set_x, off_set_y)) != None

    def the_ship(self):
        ship = TheShip(self.ship.x, self.ship.y, SPACE_SHIP)
        ship.draw_ship(self.window)
        return ship

    def alien_shoot(self, x, y):
        laser = Laser(x, y, ALIEN_BULLET)
        return laser

    def alien_shoot_laser(self):
        for i in self.alien_laser:
            i.draw(self.window)
            i.y += 3
            if self.detect_collision(i, self.the_ship()):
                self.alien_laser.remove(i)
                self.lives -= 1
                BULLET_SHIP_SOUND.play()
                explosion = Explosion(i.x, i.y, "bullet_ship")
                self.explosion_group.add(explosion)
