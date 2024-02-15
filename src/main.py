import pygame, sys
from pygame.locals import *
from entities.snake import Snake
from entities.map import GameMap
from entities.fruit import Fruit, generate_fruit
from settings import *
    
def draw(screen, game_map, snake, fruit):
    for y, row in enumerate(game_map.map):
        for x, cell in enumerate(row):
            if cell == 0:
                colour = game_map.colour
            elif cell == Snake:
                colour = snake.colour
            elif cell == Fruit:
                colour = fruit.colour
            pygame.draw.rect(screen, colour, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
def main():
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH * CELL_SIZE, MAP_HEIGHT * CELL_SIZE))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    game_speed = 10;
    game_score = 0;
    snake = Snake()
    game_map = GameMap()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
                    
        # Move the snake on each tick
        snake.move()
        
        # Check if the snake has collided with the game map boundaries
        if snake.head[0] < 0 or snake.head[0] >= MAP_WIDTH or snake.head[1] < 0 or snake.head[1] >= MAP_HEIGHT:
            break
        
        # Check if the snake has collided with itself
        if snake.head in list(snake.body)[1:]:
            break
        
        if not game_map.fruit_placed:
            fruit = generate_fruit(game_map)
            game_map.fruit_placed = True
            
        # Check if the snake has collided with the fruit
        if snake.head == (fruit.x, fruit.y):
            game_score += 1
            game_speed += 1
            game_map.fruit_placed = False
        else:
            snake.body.pop()
        
        # Clear the game map and add the snake and fruit.random_fruit(game_map)
        game_map.clear()
        game_map.update_snake(snake)
        game_map.update_fruit(fruit)
        
        # Update the game state and draw operations
        draw(screen, game_map, snake, fruit)
        pygame.display.update()
        clock.tick(game_speed)
        
main()