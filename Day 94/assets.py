import pygame
import os

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

# Background
BG = pygame.image.load(os.path.join('Assets', 'space_bg.png'))


class Laser:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.lasers = image
        self.mask = pygame.mask.from_surface(self.lasers)

    def move(self, vel):
        self.y += vel

    def draw(self, window):
        window.blit(self.lasers, (self.x, self.y))


class Assets:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Space Invader')
        self.fps = 60
        self.ship = pygame.Rect(295, 500, 60, 60)
        self.bullet = pygame.Rect(self.ship.x, self.ship.y, 60, 60)
        self.bul = None
        self.action = None
        self.fired = []
        self.run = True
        self.num = 0
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('comicsans', 15)
        self.score = 0
        self.lives = 5

    def ship_movement(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and self.ship.x > 0:
            self.ship.x -= 3
            self.bullet.x -= 3
        elif keys_pressed[pygame.K_RIGHT] and self.ship.x < 550:
            self.ship.x += 3
            self.bullet.x += 3
        elif keys_pressed[pygame.K_UP] and self.ship.y > 0:
            self.ship.y -= 3
            self.bullet.y -= 3
        elif keys_pressed[pygame.K_DOWN] and self.ship.y < 550:
            self.ship.y += 3
            self.bullet.y += 3
        elif keys_pressed[pygame.K_a]:

            if len(self.fired) == 0:
                en = Laser(self.bullet.x, self.bullet.y, BULLET)
                self.fired.append(en)

    def update_window(self):

        self.window.blit(BG, (0, 0))
        self.fire_bullet()
        self.window.blit(SPACE_SHIP, (self.ship.x, self.ship.y))
        self.action = None

        lives_text = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(lives_text, (10, 10))
        self.window.blit(score_text, (600 - score_text.get_width() - 10, 10))

        pygame.display.update()

    def fire_bullet(self):
        for i in self.fired:
            i.draw(self.window)
            i.y -= 10
            if i.y < 0:
                self.fired = []

    def move_lasers(self, vel):
        for i in self.fired:
            i.move(vel)
