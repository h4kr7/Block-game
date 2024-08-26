import pygame
import random

# Initialize The Constructor
pygame.init()

# Screen Size
screen_height = 480
screen_width = 720
display_screen = pygame.display.set_mode((screen_width, screen_height))
# here not giving direct value because to reduce processor load

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
ash_gray = (178, 190, 181)
yellow = (255, 255, 0)
grey = (100, 100, 100)
charcoal = (54, 69, 79)

# Screen Title of the window
pygame.display.set_caption("8 Bit Game")

# Insert Text/Button
button_font = pygame.font.SysFont("Times new Roman", 35)  # Font1
button_font2 = pygame.font.SysFont(None, 100)             # Font2
text = button_font2.render("8 Bit Game", True, yellow)
start_button = button_font.render("Start", True, white)
option_button = button_font.render("Option", True, white)
exit_button = button_font.render("Exit", True, white)

# Shape Size
width = display_screen.get_width()
height = display_screen.get_height()

# Game Over
def game_over():
    done = True
    while done:
        # Display Black Screen
        display_screen.fill(black)

        # pygame.event.get() used to empty the event queue
        # pygame.QUIT used for clickable closed button at the corner
        for event in pygame.event.get():
            # Closed Window
            if event.type == pygame.QUIT:
                pygame.quit()

            # If the mouse is clicked on the button the game is terminated
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (width - 200 <= mouse1[0] <= width - 200 + 140 and height - 150 <= mouse1[1] <= height - 150 + 40):
                    pygame.quit()
                    done = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (width - 600 <= mouse1[0] <= width - 600 + 140 and height - 150 <= mouse1[1] <= height - 150 + 40):
                        game()
                        done = False

        # Insert Text/Button
        button_font = pygame.font.SysFont(None, 100)               # Font1
        button_font2 = pygame.font.SysFont("Times new Roman", 35)  # Font2
        # gameover = button_font.render(text, True, color)  True helps to smooth text 
        gameover = button_font.render("Game Over", True, red) 
        restart_button = button_font2.render("Restart", True, white)
        exit_button = button_font2.render("Exit", True, white)
        scorer1 = button_font2.render("Score: " + str(scorer), True, white)

        # Initialise Mouse Pointer
        mouse1 = pygame.mouse.get_pos()

        # After color  text rectangle
        if (width - 600 <= mouse1[0] <= width - 600 + 140 and height - 150 <= mouse1[1] <= height - 150 + 40):
            pygame.draw.rect(display_screen, grey, [width - 600, height - 150, 140, 40])
        elif (width - 200 <= mouse1[0] <= width - 200 + 140 and height - 150 <= mouse1[1] <= height - 150 + 40):
            pygame.draw.rect(display_screen, grey, [width - 200, height - 150, 140, 40])

        # Before color text rectangle
        # pygame.draw.rect(display_screen, color, pygame.rect(x_axis, y_axis, width, height))  how to use this
        else:
            pygame.draw.rect(display_screen, black, pygame.Rect(width - 600, height - 150, 140, 40))
            pygame.draw.rect(display_screen, black, pygame.Rect(width - 200, height - 150, 140, 40))

        # Display Text on Screen
        # display_screen.blit(text, x_axis, y_axis)  how to use this
        display_screen.blit(gameover, (width - 540, height - 400))
        display_screen.blit(restart_button, (width - 600, height - 150))
        display_screen.blit(exit_button, (width - 200, height - 150))
        display_screen.blit(scorer1, (width - 450, height - 250))
        # blit() used to copy the context of one surface onto another surface

        # Update Display
        pygame.display.update()
        # or we can use this pygame.display.flip() 
def option():
    pass

def game():
    # Global Variable declare
    global scorer

    # object current co-ordinates
    x = 10
    y = 200

    # velocity or speed of movement
    vel = 10

    # Opponent path
    x_path = 720
    y_path = random.randint(40, 440)

    # score box
    x_score = 720
    y_score = random.randint(40, 440)

    # Total Score
    scorer = 0

    done = True
    while done:
        # Display Black Screen
        display_screen.fill(black)

        for event in pygame.event.get():
            # Closed Window
            if event.type == pygame.QUIT:
                pygame.quit()

            # If the mouse is clicked on the button the game is terminated
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (width - 70 <= mouse2[0] <= width - 70 + 70 and height - 480 <= mouse2[1] <= height - 480 + 40):
                    pygame.quit()
                    done = False

        # Initialise Mouse Pointer
        mouse2 = pygame.mouse.get_pos()

        # Insert Text/Button
        button_font = pygame.font.SysFont("Times new Roman", 25)  # Font
        exit = button_font.render("Exit", True, red)
        score = button_font.render("Score: " + str(scorer), True, black)

        # creates time delay of 10ms
        pygame.time.delay(10)

        # player
        # stores keys pressed
        keys = pygame.key.get_pressed()

        # if left arrow key is pressed
        if keys[pygame.K_UP] and y > 40:
            # decrement in y co-ordinate
            y -= vel

        # if left arrow key is pressed
        if keys[pygame.K_DOWN] and y < 480 - 40:
            # increment in y co-ordinate
            y += vel

        # drawing object on screen which is rectangle here (user)
        pygame.draw.rect(display_screen, blue, pygame.Rect(x, y, 40, 40))

        # Game over collision with red
        if x_path - 40 <= x <= x_path + 40 and y_path + 40 >= y >= y_path - 40:
            game_over()
        else:
            x_path -= 5

        # Collision with blue
        if x_score - 40 <= x <= x_score + 40 and y_score + 40 >= y >= y_score - 40:
            scorer += 1
            y_score = random.randint(40, 440)
            x_score = 720
            x_path = 720
            y_path = random.randint(40, 440)
        elif x_score == 0:
            game_over()
        else:
            x_score -= 5

        # red and blue box moving
        pygame.draw.rect(display_screen, blue, pygame.Rect(x_score, y_score, 40, 40))
        pygame.draw.rect(display_screen, red, pygame.Rect(x_path, y_path, 40, 40))

        # Create Border
        pygame.draw.rect(display_screen, ash_gray, pygame.Rect(width - 720, height - 480, 720, 40))

        # After color Border
        if (width - 70 <= mouse2[0] <= width - 70 + 70 and height - 480 <= mouse2[1] <= height - 480 + 40):
            pygame.draw.rect(display_screen, charcoal, pygame.Rect(width - 70, height - 480, 70, 40))

        # Before color Border
        else:
            pygame.draw.rect(display_screen, grey, pygame.Rect(width - 70, height - 480, 70, 40))

        # Display Exit on Screen
        display_screen.blit(exit, (width - 60, height - 475))
        display_screen.blit(score, (width - 700, height - 475))
        # display_screen.blit(score_result,(width-600,height-475))

        # Update Display
        pygame.display.update()

def intro():
    # Intro
    done = True
    while done:
        # Display Black Screen
        display_screen.fill(black)

        for event in pygame.event.get():
            # Closed Window
            if event.type == pygame.QUIT:
                # pygame.quit()
                done = False

        # Initialise Mouse Pointer
        mouse = pygame.mouse.get_pos()

        # If the mouse is clicked on the button the game is terminated
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (width - 420 <= mouse[0] <= width - 420 + 140 and height - 350 <= mouse[1] <= height - 350 + 40):
                game()
            if (width - 420 <= mouse[0] <= width - 420 + 140 and height - 255 <= mouse[1] <= height - 255 + 40):
                pygame.quit()
            if (width - 420 <= mouse[0] <= width - 420 + 140 and height - 150 <= mouse[1] <= height - 150 + 40):
                pygame.quit()

        # After color rectangle
        if (width - 420 <= mouse[0] <= width - 420 + 140 and height - 350 <= mouse[1] <= height - 350 + 40):
            pygame.draw.rect(display_screen, grey, [width - 420, height - 350, 140, 40])
        elif (width - 420 <= mouse[0] <= width - 420 + 140 and height - 255 <= mouse[1] <= height - 255 + 40):
            pygame.draw.rect(display_screen, grey, [width - 420, height - 255, 140, 40])
        elif (width - 420 <= mouse[0] <= width - 420 + 140 and height - 150 <= mouse[1] <= height - 150 + 40):
            pygame.draw.rect(display_screen, grey, [width - 420, height - 150, 140, 40])

        # Before color rectangle
        else:
            pygame.draw.rect(display_screen, black, pygame.Rect(width - 420, height - 350, 140, 40))
            pygame.draw.rect(display_screen, black, pygame.Rect(width - 420, height - 255, 140, 40))
            pygame.draw.rect(display_screen, black, pygame.Rect(width - 420, height - 150, 140, 40))

        # Display on Screen
        display_screen.blit(text, (width - 550, height - 450))
        display_screen.blit(start_button, (width - 420, height - 350))
        display_screen.blit(option_button, (width - 420, height - 255))
        display_screen.blit(exit_button, (width - 420, height - 150))

        # Update Display
        pygame.display.update()
intro()