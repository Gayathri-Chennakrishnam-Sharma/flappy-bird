from entities.ground import Ground
from entities.bird import Bird
from entities.background import Background
import sys
from util.constants import Constants
from util.colors import Colors
import pygame


def run():
    pygame.init()
    screen = pygame.display.set_mode(Constants.game_dimention)
    
    background = Background()
    bird = Bird()
    ground = Ground()

    dy = 0
    gravity = 0.02
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    dy -= 12
                    bird.set_position(dy)
        
        dy += gravity
        bird.set_position(dy)
        background.display(screen)  
        bird.displays(screen)
        ground.display(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run()