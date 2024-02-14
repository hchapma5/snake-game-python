import random
import pygame
from pygame.locals import *

class Fruit:
    def __init__(self, pos):
        self.pos = pos
        self.colour = Color(255, 0, 0)
        
    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, self.colour, (self.pos[0] * cell_size, self.pos[1] * cell_size, cell_size, cell_size))    