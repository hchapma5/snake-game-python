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
        self.img_body_h = pygame.image.load("src/assets/images/body_horizontal.png").convert_alpha()
        self.img_body_v = pygame.image.load("src/assets/images/body_vertical.png").convert_alpha()
        self.images = [self.img_head, self.img_body_h]
        
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
        self.update_head()
        self.images[0] = self.img_head
        image_body = self.img_body_h if self.dir in [self.dir_left, self.dir_right] else self.img_body_v
        self.images.append(image_body)
        self.body.appendleft(new_head)
        self.head = new_head        
        
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            if i == 0:  # Head segment
                img = self.img_head
            else:
                # Determine the direction of the segment relative to the previous segment
                prev_segment = self.body[i-1]
                if segment[0] == prev_segment[0]:  # If x-coordinates are equal, segment is vertical
                    img = self.img_body_v
                else:  # Otherwise, it's horizontal
                    img = self.img_body_h

            # Scale and draw the image
            img_scaled = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
            screen.blit(img_scaled, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE))
    
        