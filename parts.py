####################################
#                                  #
#              PART ONE            #
#                                  #
####################################

# Create variables that define our colors we will need for the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 180, 0)

# Define variables that will definte the level width and height
display_width = 800
display_height = 600

####################################
#                                  #
#              PART TWO            #
#           LINES 105 - 115        #
####################################

# Adding the functionality to keep track of the score
def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])

####################################
#                                  #
#              PART THREE          #
#           LINES 155 - 178        #
####################################

# Allows us to change and select text for a welcome screen

    gameDisplay.fill(white)

    gameDisplay.blit(alive, [260,0])

    gameDisplay.fill(white)
    message_to_screen("Welcome to Slither",
                      green,
                      -100,
                      "large")
    message_to_screen("The objective of the game is to eat red apples",
                      black,
                      -30,
                      "small")
    message_to_screen("The more apples you eat, the longer you get",
                      black,
                      10,
                      "small")
    message_to_screen("If you run into yourself or the edges, you lose!",
                      black,
                      50,
                      "small")

    message_to_screen("Press C to play, P to pause, or Q to quit.",
                      black,
                      180,
                      "small")
    pygame.display.update()
    clock.tick(15)

####################################
#                                  #
#              PART FOUR           #
#           LINES 203 - 214        #
####################################

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              y_displace = -50,
                              size = "large")

            gameDisplay.blit(dead, [280,20])

            message_to_screen("press C to play again or Q to quit",
                              black,
                              50,
                              size = "medium")
            pygame.display.update()
