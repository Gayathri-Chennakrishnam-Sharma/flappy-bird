import sys
from util.constants import Constants
from util.colors import Colors
import pygame
import pathlib

import os


def get_background():
    current_path = pathlib.Path(__file__).parent.absolute()
    background_path =  os.path.join(current_path, "assets", "images", "background.png")
    background = pygame.image.load(background_path)
    return background

def run():
    pygame.init()
    screen = pygame.display.set_mode(Constants.game_dimention)
    background = get_background()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(background, background.get_rect())   
        pygame.display.flip()


if __name__ == '__main__':
    run()