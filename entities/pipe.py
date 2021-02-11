import os
import pathlib
from util.constants import Constants

import pygame

from entities.sprite import Sprite
import random


class Pipe(Sprite):
    def __init__(self) -> None:
        self.width = Constants.pipe_width
        self.height = Constants.pipe_height

        current_path = pathlib.Path(__file__).parent.parent.absolute()
        path = os.path.join(current_path, "assets", "images", "pipe.png")
        self.image = pygame.image.load(path)
        self.pipes = list()

    def spawn_pipe(self):
        rect_bottom = self.image.get_rect()
        dy_bottom = random.randint(10, 200)
        rect_bottom.midbottom = (
            Constants.width + self.width, Constants.height + self.height // 2 + dy_bottom)

        dy_top = random.randint(10, 50)
        rect_top = self.image.get_rect()
        rect_top.midtop = (Constants.width + self.width,  -
                           self.height // 2 + dy_top)

        self.pipes.append(rect_bottom)
        self.pipes.append(rect_top)

    def move_pipe(self):
        for pipe in self.pipes:
            pipe.centerx -= 2

    def display(self, screen):
        for pipe in self.pipes:
            if pipe.midtop[1] < 0:
                screen.blit(pygame.transform.rotate(self.image, 180), pipe)
            else:
                screen.blit(self.image, pipe)
