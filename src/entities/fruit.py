import pygame, random
from pygame.locals import *
from settings import *
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (255, 0, 0)
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        
def generate_fruit(snake):
    # Generate a random position for the fruit that isn't occupied by the snake
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)
    while (x, y) in list(snake.body):
        x = random.randint(0, MAP_WIDTH - 1)
        y = random.randint(0, MAP_HEIGHT - 1)
    return Fruit(x, y)
