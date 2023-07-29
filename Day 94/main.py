import pygame
import os
from assets import Assets

FPS = 60
assets = Assets()


def main():
    while assets.run:
        assets.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                assets.run = False

        assets.ship_movement()
        assets.update_window()

    pygame.quit()


if __name__ == "__main__":
    main()
