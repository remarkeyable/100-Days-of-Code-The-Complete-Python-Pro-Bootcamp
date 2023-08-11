import pygame
from assets import Assets
pygame.init()
assets = Assets()


def main():
    while assets.run:
        assets.clock.tick(assets.fps)
        assets.append_aliens()
        assets.ship_movement()
        assets.update_window()
        if assets.lives <= 0:
            assets.restart_game()
            you_lost()
    pygame.quit()

def start():
    run = True
    while run:
        assets.game_start()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

def you_lost():
    run = True
    assets.over_sound()
    while run:
        assets.game_over()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


start()
