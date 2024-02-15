import random
from settings import *
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (255, 0, 0)
        
def generate_fruit(game_map):
    x = random.randint(0, MAP_WIDTH - 1)
    y = random.randint(0, MAP_HEIGHT - 1)
    while game_map.map[y][x] != 0:
        x = random.randint(0, MAP_WIDTH - 1)
        y = random.randint(0, MAP_HEIGHT - 1)
    return Fruit(x, y)

