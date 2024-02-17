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
        self.img_tail_up = pygame.image.load("src/assets/images/tail_up.png").convert_alpha()
        self.img_tail_down = pygame.image.load("src/assets/images/tail_down.png").convert_alpha()
        self.img_tail_left = pygame.image.load("src/assets/images/tail_left.png").convert_alpha()
        self.img_tail_right = pygame.image.load("src/assets/images/tail_right.png").convert_alpha()
        self.img_body_tl = pygame.image.load("src/assets/images/body_topleft.png").convert_alpha()
        self.img_body_tr = pygame.image.load("src/assets/images/body_topright.png").convert_alpha()
        self.img_body_bl = pygame.image.load("src/assets/images/body_bottomleft.png").convert_alpha()
        self.img_body_br = pygame.image.load("src/assets/images/body_bottomright.png").convert_alpha()
        self.img_body_h = pygame.image.load("src/assets/images/body_horizontal.png").convert_alpha()
        self.img_body_v = pygame.image.load("src/assets/images/body_vertical.png").convert_alpha()
        self.img_head = self.img_head_right # Default head image
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
        # Reset direction change flag at the start of each move
        self.change_dir = False

        key = pygame.key.get_pressed()
        new_dir = None

        if key[K_UP] and self.dir != self.dir_down:
            new_dir = self.dir_up
        elif key[K_DOWN] and self.dir != self.dir_up:
            new_dir = self.dir_down
        elif key[K_LEFT] and self.dir != self.dir_right:
            new_dir = self.dir_left
        elif key[K_RIGHT] and self.dir != self.dir_left:
            new_dir = self.dir_right

        if new_dir and new_dir != self.dir:
            self.dir = new_dir

        new_head = (self.head[0] + self.dir[0], self.head[1] + self.dir[1])
        self.update_head()
        self.body.appendleft(new_head)
        self.head = new_head
     
        
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            segment_pos = (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE)
            if i == 0:  # Head segment
                screen.blit(self.img_head, segment_pos)
            else:
                prev_segment = self.body[i - 1]
                if i < len(self.body) - 1:  # Middle segments
                    next_segment = self.body[i + 1]
                    # Determine direction to draw the correct body part
                    if prev_segment[0] == next_segment[0]:  # Vertical
                        img = self.img_body_v
                    elif prev_segment[1] == next_segment[1]:  # Horizontal
                        img = self.img_body_h
                    else:  # Corner
                        # Determine the correct corner sprite
                        if (prev_segment[0] < segment[0] and next_segment[1] < segment[1]) or (next_segment[0] < segment[0] and prev_segment[1] < segment[1]):
                            img = self.img_body_tl
                        elif (prev_segment[0] > segment[0] and next_segment[1] < segment[1]) or (next_segment[0] > segment[0] and prev_segment[1] < segment[1]):
                            img = self.img_body_tr
                        elif (prev_segment[0] < segment[0] and next_segment[1] > segment[1]) or (next_segment[0] < segment[0] and prev_segment[1] > segment[1]):
                            img = self.img_body_bl
                        elif (prev_segment[0] > segment[0] and next_segment[1] > segment[1]) or (next_segment[0] > segment[0] and prev_segment[1] > segment[1]):
                            img = self.img_body_br
                        else:
                            img = self.img_body_h  # Fallback, should not reach here
                    screen.blit(img, segment_pos)
                else:  # Tail segment, now uses tail images
                    # Determine the direction for the tail
                    if prev_segment[0] == segment[0]:  # Vertical movement
                        if prev_segment[1] > segment[1]:  # Moving up
                            img_tail = self.img_tail_up
                        else:  # Moving down
                            img_tail = self.img_tail_down
                    else:  # Horizontal movement
                        if prev_segment[0] > segment[0]:  # Moving left
                            img_tail = self.img_tail_left
                        else:  # Moving right
                            img_tail = self.img_tail_right
                    
                    screen.blit(img_tail, segment_pos)

