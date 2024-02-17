import pygame
from pygame.locals import *
from entities.snake import Snake
from entities.fruit import generate_fruit
from settings import *
from game_state import GameState, display
    
            
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
state = GameState()
snake = Snake()


def draw_background():
    for row in range(MAP_WIDTH):
        for column in range(MAP_HEIGHT):
            pygame.draw.rect(screen, (0,0,0), (row * CELL_SIZE, column * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (51, 44, 44), (row * CELL_SIZE + 0.2, column * CELL_SIZE + 0.2, CELL_SIZE - 1, CELL_SIZE - 1))
    
# -------- Main Program Loop ----------
game_loop = True
while game_loop:
    
    # Draw background
    # screen.fill((0, 0, 0))
    draw_background()
    
    # Draw the score
    state.draw_score(screen)
    
    # Draw the fruit
    if not state.fruit_placed:
        fruit = generate_fruit(snake)
        state.fruit_placed = True
    
    # Draw the fruit
    fruit.draw(screen)
    
    # Draw the snake and move it on each tick
    snake.move()
    snake.draw(screen)
    
    # If the snake has eaten the fruit
    if snake.head == (fruit.x, fruit.y):
        state.update()
        state.fruit_placed = False
    else:
        snake.body.pop()
                
    # If the snake has collided with itself
    if len(snake.body) != len(set(snake.body)):
        state.game_over(screen)
        
    # If the snake has collided with the wall
    if snake.head[0] < 0 or snake.head[0] >= MAP_WIDTH or snake.head[1] < 0 or snake.head[1] >= MAP_HEIGHT:
        state.game_over(screen) 
    
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            game_loop = False
        elif(event.type == KEYDOWN):
            if event.key == K_ESCAPE:
                game_loop = False
    
    pygame.display.flip()
    clock.tick(state.speed)
        
pygame.quit()