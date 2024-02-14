from settings import MAP_WIDTH, MAP_HEIGHT
from entities.snake import Snake
from entities.fruit import Fruit

class GameMap:
    def __init__(self):
        self.map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        
    def is_empty(self, pos):
        return self.map[pos[1]][pos[0]] == 0
    
    def is_snake(self, pos):
        return self.map[pos[1]][pos[0]] == Snake
    
    def is_fruit(self, pos):
        return self.map[pos[1]][pos[0]] == Fruit
        