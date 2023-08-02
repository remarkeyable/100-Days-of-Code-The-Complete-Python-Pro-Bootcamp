import pygame
import os
import time
from assets import Assets
from assets import Laser

assets = Assets()
BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 90)


def main():
    while assets.run:
        assets.clock.tick(assets.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                assets.run = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "space":
                    en = Laser(assets.bullet.x, assets.bullet.y, BULLET)
                    assets.fired.append(en)
        if len(assets.aliens) == 0:
            for i in range(5):
                assets.append_aliens()

        assets.ship_movement()
        assets.update_window()


    pygame.quit()


if __name__ == "__main__":
    main()
