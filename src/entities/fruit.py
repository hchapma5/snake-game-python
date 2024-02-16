import pygame, random
from pygame.locals import *
from settings import *
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (255, 0, 0)
        self.image = pygame.image.load("src/assets/images/apple.png").convert_alpha()
        self.sprite_offset = 10
        
    def draw(self, screen):
        # pygame.draw.rect(screen, self.colour, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        screen.blit(self.image, (self.x * CELL_SIZE - self.sprite_offset, self.y * CELL_SIZE - self.sprite_offset))
    
def generate_fruit(snake):
    # Generate a random position for the fruit that isn't occupied by the snake
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)
    while (x, y) in list(snake.body):
        x = random.randint(0, MAP_WIDTH - 1)
        y = random.randint(0, MAP_HEIGHT - 1)
    return Fruit(x, y)
