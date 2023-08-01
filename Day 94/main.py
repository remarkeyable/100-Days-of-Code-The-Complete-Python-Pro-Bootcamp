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
        keys_pressed = pygame.key.get_pressed()  # if keys_pressed[pygame.K_SPACE]:  #     assets.fire_bullet()

    pygame.quit()


if __name__ == "__main__":
    main()
