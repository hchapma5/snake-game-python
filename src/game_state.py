import sys
import pygame
from pygame.locals import *
from settings import *
from pygame import font

class GameState:
    def __init__(self):
        self.speed = 10
        self.score = 0
        
    def update(self, screen):
        self.speed += 1
        self.score += 1
        
    def game_over(self, screen):
        paused = True
        while paused:
            display("GAME OVER", screen, GAME_OVER_POSITION, GAME_OVER_COLOUR)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

def display(text, screen, pos, colour):
    font = pygame.font.Font(FONT, 72)
    text = font.render(text, 0, colour)
    screen.blit(text, pos)
    pygame.display.update()
            
