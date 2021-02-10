import os
import pathlib
from util.constants import Constants

import pygame


class Bird:
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path =  os.path.join(current_path, "assets", "images", "bird.png")
        self.image = pygame.image.load(path)
        self.cnt = 0

    def display(self, screen):
        bird_rect = self.image.get_rect()
        bird_rect.center = Constants.width//2 + self.cnt, Constants.height//2
        self.cnt += 1
        screen.blit(self.image, bird_rect)   