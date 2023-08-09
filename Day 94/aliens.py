import random
import pygame
import os



class Aliens:
    def __init__(self, images):
        self.x = random.randrange(25, 500)
        self.y = random.randrange(-100, -10)
        self.random_alien = random.choice(["ALIEN_1", "ALIEN_2", "ALIEN_3"])
        self.image = images[self.random_alien]
        self.mask = pygame.mask.from_surface(self.image)
        self.alien_image = self.mask.to_surface()

    def produce_aliens(self, window):
        window.blit(self.image, (self.x, self.y))
