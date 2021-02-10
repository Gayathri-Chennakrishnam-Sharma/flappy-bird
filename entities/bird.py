from entities.sprite import Sprite
import os
import pathlib
from util.constants import Constants

import pygame


class Bird(Sprite):
    def __init__(self):
        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path =  os.path.join(current_path, "assets", "images", "bird.png")
        self.position = Constants.width//2, Constants.height//2
        self.image = pygame.image.load(path)

    def jump(self):
        x, y = self.position
        self.position = x, y - 20

    def apply_gravity(self):
        x, y = self.position
        self.position = x, y + 2


    def displays(self, screen):
        bird_rect = self.image.get_rect()
        x, y = self.position
        bird_rect.center = x, y
        screen.blit(self.image, bird_rect)   