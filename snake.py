import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Set up the snake
snake_block_size = 20
snake_speed = 15
snake_list = []

# Function to draw the snake
def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Game loop
game_over = False
game_quit = False

snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0
snake_list.append([snake_x, snake_y])

while not game_quit:
    while game_over:
        # Game over screen
        window.fill(black)
        font_style = pygame.font.SysFont(None, 50)
        message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, white)
        window.blit(message, [window_width / 2 - 200, window_height / 2 - 50])
        pygame.display.update()

        # Check for quit or play again
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_quit = True
                    game_over = False
                if event.key == pygame.K_c:
                    # Reset game variables
                    snake_x = window_width / 2
                    snake_y = window_height / 2
                    snake_x_change = 0
                    snake_y_change = 0
                    snake_list = []
                    snake_list.append([snake_x, snake_y])
                    game_over = False

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block_size
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block_size
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block_size
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with boundaries
    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_over = True

    # Update game window
    window.fill(black)
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > 1:
        del snake_list[0]

    # Check for collision with self
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    # Draw the snake
    draw_snake(snake_block_size, snake_list)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()