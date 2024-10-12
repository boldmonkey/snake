import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 10

# Clock
clock = pygame.time.Clock()

# Font
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

# Load sounds
eat_sound = pygame.mixer.Sound("eat_sound.mp3")
game_over_sound = pygame.mixer.Sound("game_over_sound.mp3")
burp_sound = pygame.mixer.Sound("burp_sound.mp3")

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    win.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0

    while not game_over:

        while game_close == True:
            win.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
            game_over_sound.play()  # Play sound when game over

        x1 += x1_change
        y1 += y1_change
        win.fill(black)
        pygame.draw.rect(win, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                game_over_sound.play()  # Play sound when game over


        for x in snake_List:
            pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

        display_score(score)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 1
            if score % 5 == 0:
                burp_sound.play() # Burp sound when score is multiple of 5
            else:
                eat_sound.play()  # Play sound when snake eats food

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()