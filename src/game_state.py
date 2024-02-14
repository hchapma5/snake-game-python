from settings import MAP_WIDTH, MAP_HEIGHT
from entities import Snake, Fruit

def snake_fruit_collision(snake, fruit):
    return snake.head == fruit.pos

def snake_wall_collision(snake):
    return snake.head[0] < 0 or snake.head[0] >= MAP_WIDTH or snake.head[1] < 0 or snake.head[1] >= MAP_HEIGHT

def snake_self_collision(snake):
    return snake.head in snake.body