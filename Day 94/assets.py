import pygame
import os

BG_COLOR = (14, 41, 84)
SHIP = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 90)
SPACE_SHIP = pygame.transform.scale(SHIP, (60, 60))
THE_BUL = []


class Assets:
    def __init__(self):
        self.window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Space Invader')
        self.ship = pygame.Rect(295, 500, 60, 60)
        self.bullet = pygame.Rect(self.ship.x, self.ship.y, 60, 60)
        self.fired = []
        self.run = True
        self.clock = pygame.time.Clock()

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
        elif keys_pressed[pygame.K_SPACE]:
            bul = self.window.blit(BULLET, (self.bullet.x, self.bullet.y))
            self.fired.append(bul)
            print(self.fired)
            self.fire_bullet()

    def update_window(self):
        self.window.fill(BG_COLOR)
        self.window.blit(SPACE_SHIP, (self.ship.x, self.ship.y))
        self.window.blit(BULLET, (self.bullet.x, self.bullet.y))
        pygame.display.update()

    def fire_bullet(self):
        self.window.blit(BULLET, (self.bullet.x+20, self.bullet.y+25))

