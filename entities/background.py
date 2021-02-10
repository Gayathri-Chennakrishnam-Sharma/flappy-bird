from entities.sprite import Sprite
import os
import pathlib

import pygame


class Background(Sprite):
    def __init__(self) -> None:
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path =  os.path.join(current_path, "assets", "images", "background.png")
        self.image = pygame.image.load(path)

    def display(self, screen):
        screen.blit(self.image, self.image.get_rect())   