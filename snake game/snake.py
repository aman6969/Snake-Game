import pygame
import random
pygame.init()

# Colours (RGB)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
orange = (255,128,0)
pink = (255,0,255)

screen_width = 800
screen_height = 600
# Creating game window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Game title
pygame.display.set_caption('Snake Game')
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',20)


with open ('hiscore.txt','r') as f:
    hiscore = f.read()

def text_screen(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    gameWindow.blit(screen_text,(x,y))

def plot_snake(gameWindow,colour,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, colour, [x,y,snake_size, snake_size])



# Game loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45  # position of snake in x axis
    snake_y = 55  # position of snake in y axis
    velocity_x = 0
    velocity_y = 0
    init_velocity = 6
    snake_list = []
    snake_length = 1

    with open('hiscore.txt','r') as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width//2)
    food_y = random.randint(20, screen_height//2)
    score = 0
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open('hiscore.txt', 'w') as f:
                f.write(str(hiscore))

            gameWindow.fill('sky blue')
            text_screen('Game Over! Press Enter to Continue',red,240,240)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:


                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:    # keydown ka mtlb hmne key press ki hai.
                    if event.key==pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key==pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key==pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key==pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score = score + 10


                food_x = random.randint(20, screen_width // 2)
                food_y = random.randint(20, screen_height // 2)
                snake_length = snake_length + 5

                if score>int(hiscore):
                    hiscore = score


            gameWindow.fill(white)
            text_screen('Score:' + str(score) + '  Highscore: '+str(hiscore), red, 580, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[ :-1]:
                game_over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True



            plot_snake(gameWindow,black,snake_list,snake_size)
            # game me koi v change krne se iss function ko run krna hota hai.
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()