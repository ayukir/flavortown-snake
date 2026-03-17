import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
brown = (139, 69, 19)
dark_brown = (65, 33, 11)
skin_color = (255, 224, 189)

# Screen dimensions
width = 600
height = 400
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Cookies')

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("bahnschrift", 35)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])

def draw_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def show_start_screen():
    dis.fill(black)
    message("Press any arrow key to start", yellow)
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                    waiting = False
    dis.fill(black)
    pygame.display.update()

def draw_cookie(x, y):
    # Main cookie body
    pygame.draw.circle(dis, brown, (x + snake_block // 2, y + snake_block // 2), snake_block // 2)
    # Chocolate chips
    chip_offsets = [(4, 4), (12, 6), (7, 12), (14, 14)]
    for ox, oy in chip_offsets:
        pygame.draw.circle(dis, dark_brown, (x + ox, y + oy), 2)

def draw_snake(snake_list):
    for i, segment in enumerate(snake_list):
        # Draw body
        pygame.draw.rect(dis, white, [segment[0], segment[1], snake_block, snake_block])
        
        # If it's the head, draw a simple smiley
        if i == len(snake_list) - 1:
            hx, hy = segment[0], segment[1]
            cx = hx + snake_block // 2
            cy = hy + snake_block // 2
            radius = snake_block // 2
            pygame.draw.circle(dis, skin_color, (cx, cy), radius)
            pygame.draw.circle(dis, black, (hx + 6, hy + 7), 2)
            pygame.draw.circle(dis, black, (hx + 14, hy + 7), 2)
            pygame.draw.arc(dis, black, [hx + 5, hy + 10, 10, 6], 3.14, 2 * 3.14, 2)

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
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
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        
        draw_cookie(foodx, foody)
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_List)
        draw_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

show_start_screen()
gameLoop()