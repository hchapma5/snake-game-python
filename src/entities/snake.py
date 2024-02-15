
from settings import *
from collections import deque
class Snake:
    def __init__(self):
        self.body = deque([SNAKE_INIT_POS])
        self.head = self.body[0]
        self.direction = 'RIGHT'
        self.colour = (0, 255, 0)
        
    def move(self):
        if self.direction == 'UP':
            new_head_pos = (self.head[0], self.head[1] - 1)
        elif self.direction == 'DOWN':
            new_head_pos = (self.head[0], self.head[1] + 1)
        elif self.direction == 'LEFT':
            new_head_pos = (self.head[0] - 1, self.head[1])
        elif self.direction == 'RIGHT':
            new_head_pos = (self.head[0] + 1, self.head[1])
            
        self.body.appendleft(new_head_pos)
        self.head = new_head_pos
        