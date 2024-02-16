import pygame
from pygame.locals import *
from settings import *
from collections import deque

class Snake:
    def __init__(self):
        self.body = deque([SNAKE_INIT_POS])
        self.head = self.body[0]
        self.colour = (91, 123, 249)
        self.dir_up = [0, -1]
        self.dir_down = [0, 1]
        self.dir_left = [-1, 0]
        self.dir_right = [1, 0]
        self.dir = self.dir_right
        self.img_head_up = pygame.image.load("src/assets/images/head_up.png").convert_alpha()
        self.img_head_down = pygame.image.load("src/assets/images/head_down.png").convert_alpha()
        self.img_head_left = pygame.image.load("src/assets/images/head_left.png").convert_alpha()
        self.img_head_right = pygame.image.load("src/assets/images/head_right.png").convert_alpha()
        self.img_head = self.img_head_right
        
    def update_head(self):
        if self.dir == self.dir_right:
            self.img_head = self.img_head_right
        elif self.dir == self.dir_left:
            self.img_head = self.img_head_left
        elif self.dir == self.dir_down:
            self.img_head = self.img_head_down
        elif self.dir == self.dir_up:
            self.img_head = self.img_head_up
        
    def move(self):
        key = pygame.key.get_pressed()

        if key[K_UP] and self.dir != self.dir_down:
            self.dir = self.dir_up
        elif key[K_DOWN] and self.dir != self.dir_up:
            self.dir = self.dir_down
        elif key[K_LEFT] and self.dir != self.dir_right:
            self.dir = self.dir_left
        elif key[K_RIGHT] and self.dir != self.dir_left:
            self.dir = self.dir_right
            
        new_head = (self.head[0] + self.dir[0], self.head[1] + self.dir[1])
        self.body.appendleft(new_head)
        self.head = new_head
            
        
    def draw(self, screen):
        self.update_head()
        for segment in self.body:
            if segment == self.head:
                screen.blit(self.img_head, (segment[0] * CELL_SIZE - 10, segment[1] * CELL_SIZE - 10))
            else:
                pygame.draw.rect(screen, self.colour, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
        