import pygame
from pygame.locals import *
from collections import deque

class Snake:
    def __init__(self, init_pos):
        self.body = deque([init_pos])
        self.head = self.body[0] # Get head position
        self.colour = Color(0, 255, 0)
        
    def move(self, new_head_pos):
        self.body.appendleft(new_head_pos) # Add new head position
        self.body.pop() # Remove tail position
        
    def eat(self, new_head_pos):
        self.body.appendleft(new_head_pos) # Add new head position without removing tail position
        
    def draw(self, screen, cell_size):
        for pos in self.body:
            pygame.draw.rect(screen, self.colour, (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))