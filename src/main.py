import pygame
from pygame.locals import *
from settings import MAP_WIDTH, MAP_HEIGHT, CELL_SIZE, FPS

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH * CELL_SIZE, MAP_HEIGHT * CELL_SIZE))
    clock = pygame.time.Clock()
    
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
        screen.fill(Color(0, 0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    