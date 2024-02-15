from settings import *
from entities.snake import Snake
from entities.fruit import Fruit

class GameMap:
    def __init__(self):
        self.map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self.colour = (0, 0, 0)
        self.fruit_placed = False
    
    def clear(self):
        self.map = [[0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

    def update_snake(self, snake):
        for segment in snake.body:
            self.map[segment[1]][segment[0]] = Snake
    
    def update_fruit(self, fruit):
        self.map[fruit.y][fruit.x] = Fruit