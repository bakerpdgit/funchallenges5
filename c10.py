import pygame
import random

pygame.init()

# Define colours
# ==> Task 2
background_colour = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up window
# ==> Task 1
display_width = 600
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# Control game speed
clock = pygame.time.Clock()
snake_speed = 15

# Dimension for each block
snake_block = 10

# Font for text
font_style = pygame.font.SysFont(None, 30)

game_close = False


# Formatting for text
def message(text, colour):
    message_text = font_style.render(text, True, colour)
    display.blit(
        message_text,
        [display_width / 6, display_height / 3]
    )


# Drawing the snake
def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(
            display,
            green,
            [segment[0], segment[1], snake_block, snake_block]
        )


# Getting new food coordinates
def add_food(food, snake_list):
    while True:
        food_x = random.randrange(0, display_width, snake_block)
        food_y = random.randrange(0, display_height, snake_block)

        if [food_x, food_y] not in snake_list:
            break

    food.append((food_x, food_y))
    return food


while not game_close:

    game_over = False

    # Starting coordinates for the snake
    snake_x = display_width // 2
    snake_y = display_height // 2

    # Snake starts stationary
    x_change = 0
    y_change = 0

    # Initialise the snake
    snake_list = []
    snake_length = 1

    # Initialise the food
    food = []
    # ==> Task 5

    food = add_food(food, snake_list)
    

    while not game_over:

        # Get user input
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True
                game_close = True

            if event.type == pygame.KEYDOWN:

                # Prevent the snake from reversing direction
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -snake_block
                    y_change = 0

                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = snake_block
                    y_change = 0

                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -snake_block
                    x_change = 0

                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = snake_block
                    x_change = 0

        # Move the snake
        snake_x += x_change
        snake_y += y_change

        # Snake dies if it hits a boundary
        if (
            snake_x >= display_width
            or snake_x < 0
            # ==> Task 4


        ):
            game_over = True
            continue

        # Add the new snake coordinate
        snake_list.append((snake_x, snake_y))

        # Keep the snake the correct length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if the snake hits itself
        for segment in snake_list[:-1]:
            if segment == snake_list[-1]:
                game_over = True

        # Draw everything
        display.fill(background_colour)

        # Draw the snake
        draw_snake(snake_list)

        # Draw the food
        for food_x, food_y in food:
            pygame.draw.rect(
                display,
                red,
                [food_x, food_y, snake_block, snake_block]
            )

        pygame.display.update()

        # Check if the snake has eaten food
        if (snake_x, snake_y) in food:
            food.remove((snake_x, snake_y))
            # ==> Task 3
            
            food = add_food(food, snake_list)

        # Control game speed
        clock.tick(snake_speed)

    # If the player closed the window, stop immediately
    if game_close:
        break

    # Game-over screen
    play_again = False

    while not play_again and not game_close:

        display.fill(background_colour)
        message("You Lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_close = True
                play_again = True

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    game_close = True
                    play_again = True

                elif event.key == pygame.K_c:
                    play_again = True

pygame.quit()
