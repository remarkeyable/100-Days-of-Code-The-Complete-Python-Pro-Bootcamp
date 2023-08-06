import pygame
import os
import time
from assets import Assets
from assets import Laser
from assets import TheShip

SHIP = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
BULLET = pygame.transform.rotate(pygame.image.load(os.path.join('Assets', 'bullet.png')), 90)
SPACE_SHIP = pygame.transform.scale(SHIP, (60, 60))
LASER_PATH = "Assets/sounds/laser.wav"
LASER_SOUND = pygame.mixer.Sound(LASER_PATH)
assets = Assets()


def main():
    while assets.run:
        assets.clock.tick(assets.fps)
        assets.append_aliens()
        assets.ship_movement()
        assets.update_window()
    pygame.quit()


if __name__ == "__main__":
    main()
