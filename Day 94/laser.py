import pygame


class Laser:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.mask = pygame.mask.from_surface(self.image)
        self.bullet_image = self.mask.to_surface()

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))