import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, alien, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 10):
            img = pygame.image.load(f"Assets/explosions/{alien}/{num}.png")
            img = pygame.transform.rotate(pygame.transform.scale(img, (w, h)), 90)
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
