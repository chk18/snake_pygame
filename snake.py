#
#   Snake Game
#
#   With this activity you will learn some of the more complex parts of Python,
#   as well as learn about game design and what it takes to program games.
#
#   There are FOUR parts to this exercise. You will need to make sure you have
#   correctly filled in every part before trying to run your program.


# Import our dependencies
import pygame
import time
import random

# Initialized the pygame library
pygame.init()

####################################
#                                  #
#              PART ONE            #
#           LINES 25 - 33          #
####################################



######################################
#           END OF PART ONE          #
######################################

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

# Define the variable that will hold the apple that our snake is trying to eat
icon = pygame.image.load('apple.jpg')
pygame.display.set_icon(icon) #Size: 32x32

img = pygame.image.load('snake_head.png')
appleimg = pygame.image.load('apple.jpg')
alive = pygame.image.load('alive.png')
dead = pygame.image.load('dead.png')


# Define more variables
clock = pygame.time.Clock()

AppleThickness = 30

block_size = 20

FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

# Adding the functionality for our player to pause the game
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Paused",
                          black,
                          -100,
                          size = "large")

        message_to_screen("Press C to continue or Q to quit.",
                         black,
                         25)

        pygame.display.update()
        clock.tick(5)


####################################
#                                  #
#              PART TWO            #
#           LINES 105 - 115        #
####################################



######################################
#           END OF PART TWO          #
######################################

def randAppleGen():
    randAppleX = round(random.randrange(0, display_width - AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height - AppleThickness))#/10.0)*10.0


    return randAppleX, randAppleY


def game_intro():

    intro = True

    while intro:

# Making the "C" and "Q" buttons work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

####################################
#                                  #
#              PART THREE          #
#           LINES 155 - 178        #
####################################



######################################
#           END OF PART THREE        #
######################################

def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)


    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)

    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameLoop():
    global direction

    direction = 'right'
    gameEXIT = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()


    while not gameEXIT:


####################################
#                                  #
#              PART FOUR           #
#           LINES 203 - 214        #
####################################

    

######################################
#           END OF PART FOUR         #
######################################

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameEXIT = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_p:
                    pause()

    # BOUNDARIES
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True


    # LOGIC LOOP:
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        #AppleThickness = 30
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
# 1st blit
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

    # snake growth

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
# 2nd blit
        snake(block_size, snakeList)
# 3rd blit
        score(snakeLength-1)
# 4th blit
        pygame.display.update()


        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1

        clock.tick(FPS)




    pygame.quit()
    quit()

game_intro()
gameLoop()
