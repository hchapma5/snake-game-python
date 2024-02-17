import sys
import pygame
from pygame.locals import *
from settings import *

class GameState:
    def __init__(self):
        self.speed = 10
        self.score = 0
        self.fruit_placed = False
    
    def draw_score(self, screen):
        display("SCORE: " + str(self.score), screen, SCORE_POSITION, SCORE_SIZE, SCORE_COLOUR)
        
    def update(self):
        self.speed += 0.25
        self.score += 1
        
    def game_over(self, screen):
        paused = True
        while paused:
            display("YOU DIED", screen, GAME_OVER_POSITION, GAME_OVER_SIZE, GAME_OVER_COLOUR)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()

def display(text, screen, pos, size, colour):
    font = pygame.font.Font(FONT, size)
    text = font.render(text, 0, colour)
    screen.blit(text, pos)
    pygame.display.update()
            