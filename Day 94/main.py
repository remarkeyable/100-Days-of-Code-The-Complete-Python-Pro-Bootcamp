import pygame
import os
import time
from assets import Assets

assets = Assets()


def main():
    while assets.run:

        assets.clock.tick(assets.fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                assets.run = False
        assets.ship_movement()
        assets.update_window()
        if len(assets.aliens) == 0:
            assets.append_aliens()

    pygame.quit()


if __name__ == "__main__":
    main()
