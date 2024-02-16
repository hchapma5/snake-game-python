import pygame
from pygame.locals import *
from settings import *
from collections import deque

class Snake:
    def __init__(self):
        self.body = deque([SNAKE_INIT_POS])
        self.head = self.body[0]
        self.colour = (0, 255, 0)
        self.next_x = 0
        self.next_y = 1
        
    def move(self):
        key = pygame.key.get_pressed()

        if key[K_UP] and self.next_y != 1:
            self.next_x = 0
            self.next_y = -1
        elif key[K_DOWN] and self.next_y != -1:
            self.next_x = 0
            self.next_y = 1
        elif key[K_LEFT] and self.next_x != 1:
            self.next_x = -1
            self.next_y = 0
        elif key[K_RIGHT] and self.next_x != -1:
            self.next_x = 1
            self.next_y = 0
            
        new_head = (self.head[0] + self.next_x, self.head[1] + self.next_y)
        self.body.appendleft(new_head)
        self.head = new_head
            
        
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.colour, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
        