import pygame
from assets import Assets

assets = Assets()


def main():
    while assets.run:
        assets.clock.tick(assets.fps)
        assets.append_aliens()
        assets.ship_movement()
        assets.update_window()
        if assets.lives <= 0:
            assets.restart_game()
    pygame.quit()


if __name__ == "__main__":
    main()
