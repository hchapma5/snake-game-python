import pygame, random
from pygame.locals import *
from settings import *
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (255, 0, 0)
        self.image = pygame.image.load("src/assets/images/apple.png").convert_alpha()
        self.img_scale = 10
        self.img_offset = self.img_scale / 2
        
    def draw(self, screen):
        image = pygame.transform.scale(self.image, (CELL_SIZE + self.img_scale, CELL_SIZE + self.img_scale))
        screen.blit(image, (self.x * CELL_SIZE - self.img_offset, self.y * CELL_SIZE - self.img_offset))
        
    
def generate_fruit(snake):
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)
    while (x, y) in list(snake.body):
        x = random.randint(0, MAP_WIDTH - 1)
        y = random.randint(0, MAP_HEIGHT - 1)
    return Fruit(x, y)
