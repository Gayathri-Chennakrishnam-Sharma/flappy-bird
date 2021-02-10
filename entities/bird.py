from entities.sprite import Sprite
import os
import pathlib
from util.constants import Constants

import pygame


class Bird(Sprite):
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path =  os.path.join(current_path, "assets", "images", "bird.png")
        self.image = pygame.image.load(path)

    def displays(self, screen):
        bird_rect = self.image.get_rect()
        bird_rect.center = Constants.width//2, Constants.height//2
        screen.blit(self.image, bird_rect)   