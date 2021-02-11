from mechanics.collition_detector import CollitionDetector
from entities.pipe import Pipe
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
    
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    background = Background()
    bird = Bird()
    ground = Ground()
    pipe = Pipe()

    SPAWN_PIPE_EVENT = pygame.USEREVENT + 1

    pygame.time.set_timer(pygame.USEREVENT, 200)
    pygame.time.set_timer(SPAWN_PIPE_EVENT, 1500)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.jump()
            if event.type == pygame.USEREVENT:
                bird.animate()
            if event.type == SPAWN_PIPE_EVENT:
                pipe.spawn_pipe()


        if bird.collition_detected(pipe.pipes):
            textsurface = myfont.render('Game Over', False, Colors.white)
            screen.blit(textsurface,(Constants.width//2, Constants.height//2))
        else:
            pipe.move_pipe()
            bird.apply_gravity()
            background.display(screen)
            bird.display(screen)
            pipe.display(screen)
            ground.display(screen)

        pygame.display.flip()


if __name__ == '__main__':
    run()
