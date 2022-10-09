import os
import random
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, slimeClass, time
#from pygame.locals import *
"""
#Remaining Tasks: (might have fixed this... need to double check...)
# I found a bug where if a slimeTheSlime corners one of the slimes completely perfectly in the corner,
#the slimeTheSlime stops moving and the game is in a stale
# fixing this bug should be easy just an extra claus
"""

pygame.init() #set up for general variables and general prepartion

keys = [False, False, False, False, False, False] #up, left, down, right, space, ESC

slimesArray = []
# for i in range(10):
#     slimesArr

black = 0, 0, 0
red = 200, 0, 0
green = 0,200,0
white = 255,255,255

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

#starting velocity for general non slimeTheSlime sprites/slimes
# speed = [2, 2] #velocity is a better variable name for this since vector

########___slimeTheSlime Coordinates#######
x = 200
y = 200
####################################

PlayerSlime = pygame.image.load("animation/green_slime_0.png")
PlayerSlime_rect = PlayerSlime.get_rect(center = (x,y)) #this is how you update the slimeTheSlime slime location
playerLifePoints = 100
playerCombatScore = 0
playerTime = 0

gameOver = False



###############___set up for displaying the title etc###############
####################################################################
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Slimes Game - NoahTheCorgi -- Press Space to Speed Up! :D', False, (0, 200, 0))
####################################################################
####################################################################

########___predefined functions to use later___#######
def check_inside_screen(x,y):
    if (0<x<width) and (0<y<height):
        return True
    else:
        return False

def keep_inside_screen(x,y):
    if x < 0:
        x = 1
    if x > width:
        x = width - 1
    if y < 0:
        y = 1
    if y > width:
        y = height - 1

def checkIfCollision():
    for i in range(len(slimesArray)):
        if slimesArray[i][1].colliderect(PlayerSlime_rect):
            return True
    return False


###################set up non slimeTheSlime sprites using the slimeClass###################
####################################################################################
####################################################################################
"""Set up for the first original non slimeTheSlime slime (this should thus be integrated for the rest of the slimes"""
for i in range(30):
    slimeImage = pygame.image.load("animation/red_slime.png")
    slimeRectangle = slimeImage.get_rect(center = (random.randint(0, 500), random.randint(0, 500)))
    slimesArray.append([slimeImage, slimeRectangle, [random.randint(-5, 5), random.randint(-5, 5)]])

####################################################################################

# slimeTheSlime = slimeClass.slime("animation/green_slime_0.png", "slime2", (100,100), 0 , 0)
# slimeTheSlime.set_animation("animation")

########################################################
######################The_Frames########################
########################################################
counter = 0
while True:
    #time.sleep(1)

    if counter >= 1000:
        if gameOver == False:
            playerLifePoints += 10
        counter = 0

    ###################___Get information about user inputs___##################
    ############################################################################
    ############################################################################
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keys[5] = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                print("left")
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                print("down")
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                print("right")
                keys[3] = True
            elif event.key == pygame.K_SPACE:
                print("space")
                keys[4] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False
            elif event.key == pygame.K_SPACE:
                keys[4] = False


    if playerLifePoints > 0:

        ########################___Update with respect to the user inputs#########################

        if keys[4]:
            #for i in range(len(slimesArray)):
            #    slimerect = slimesArray[i][1]
            #    valid = False
            if counter%25 < 13:
                print(0)
                PlayerSlime = pygame.image.load("animation/green_slime_0.png")
            else:
                print(1)
                PlayerSlime = pygame.image.load("animation/green_slime_1.png")
            if keys[0]:#UP
                keep_inside_screen(x,y)
                #if check_inside_screen(x, y-10) and not slimerect.colliderect(PlayerSlime_rect):
                if check_inside_screen(x, y - 10) and not checkIfCollision():
                    #y-=10
                    PlayerSlime_rect.centery -= 10
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[1]:#LEFT
                keep_inside_screen(x,y)
                if check_inside_screen(x-10, y) and not checkIfCollision():
                    #x-=10
                    PlayerSlime_rect.centerx -= 10
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[2]:#DOWN
                keep_inside_screen(x,y)
                if check_inside_screen(x, y+10) and not checkIfCollision():
                    #y+=10
                    PlayerSlime_rect.centery += 10
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[3]:#RIGHT
                keep_inside_screen(x+10,y)
                if check_inside_screen(x+10, y) and not checkIfCollision():
                    #x+=10
                    PlayerSlime_rect.centerx += 10
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
        else:
            if counter%25 < 13:
                PlayerSlime = pygame.image.load("animation/slime.png")
            else:
                PlayerSlime = pygame.image.load("animation/slime_1.png")
            if checkIfCollision():
                playerLifePoints -= 1
                playerCombatScore += 1
            if keys[0]:#UPs
                keep_inside_screen(x,y)
                #if check_inside_screen(x, y-10) and not slimerect.colliderect(PlayerSlime_rect):
                if check_inside_screen(x, y - 10) and not checkIfCollision():
                    #y-=5
                    PlayerSlime_rect.centery -= 5
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[1]:#LEFT
                keep_inside_screen(x,y)
                if check_inside_screen(x-10, y) and not checkIfCollision():
                    PlayerSlime_rect.centerx -= 5
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[2]:#DOWN
                keep_inside_screen(x,y)
                if check_inside_screen(x, y+10) and not checkIfCollision():
                    #y+=5
                    PlayerSlime_rect.centery += 5
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
            if keys[3]:#RIGHT
                keep_inside_screen(x+10,y)
                if check_inside_screen(x+10, y) and not checkIfCollision():
                    #+=5
                    PlayerSlime_rect.centerx += 5
                else:
                    playerLifePoints -= 1
                    playerCombatScore += 1
        ###################################################################



        ##################___UPDATE ALL WITH RESPECT TO VELOCITY... ALL SPRITES___#######################
        #################################################################################################
        #################################################################################################
        for i in range(len(slimesArray)):
            #print("was here ")
            slimerect = slimesArray[i][1]
            #print(slimerect)
            slimesArray[i][1] = slimesArray[i][1].move(slimesArray[i][2])
            if slimesArray[i][1].left < 0:
                slimesArray[i][1].left = 1
                slimesArray[i][2][0] = -slimesArray[i][2][0]
            if slimesArray[i][1].right > width:
                slimesArray[i][1].right = width -1
                slimesArray[i][2][0] = -slimesArray[i][2][0]

            if slimesArray[i][1].top < 0 :
                slimesArray[i][1].top = 1
                slimesArray[i][2][1] = -slimesArray[i][2][1]
            if slimesArray[i][1].bottom > height:
                slimesArray[i][1].bottom = height -1
                slimesArray[i][2][1] = -slimesArray[i][2][1]

            x_axis_diff = (slimesArray[i][1].center[0] - PlayerSlime_rect.center[0])
            y_axis_diff = (slimesArray[i][1].center[1] - PlayerSlime_rect.center[1])
            if slimesArray[i][1].colliderect(PlayerSlime_rect):
                if x_axis_diff!=0 and y_axis_diff!=0:
                    slimesArray[i][2][0] = 2*x_axis_diff/abs(x_axis_diff)
                    slimesArray[i][2][1] = 2*y_axis_diff/abs(y_axis_diff)
        ###################################################################
        ###################################################################
        ###################################################################



        #########################_ANIMATE_#################################
        ###################################################################
        # if i%25 < 13:
        #     slime = pygame.image.load("animation/red_slime_1.png")
        # else:
        #     slime = pygame.image.load("animation/red_slime.png")

        # if i%25 <6:
        #     #we skip zero because there is always a hidden file at the start created.
        #     slimeTheSlime.slimeSurface = pygame.image.load(slimeTheSlime.animation[1])
        # elif i%25 <12:
        #     slimeTheSlime.slimeSurface = pygame.image.load(slimeTheSlime.animation[2])
        # elif i%25 <18:
        #     slimeTheSlime.slimeSurface = pygame.image.load(slimeTheSlime.animation[3])
        # elif i%25 <25:
        #     slimeTheSlime.slimeSurface = pygame.image.load(slimeTheSlime.animation[4])
        ###################################################################
        ###################################################################


        #########################___"Blits"___#############################
        ###################################################################
        screen.fill(white)
        screen.blit(textsurface, (0,0))
        screen.blit(myfont.render("LifePointsLeft: " + str(playerLifePoints), False, (200, 0, 0)), (10, 35))
        screen.blit(myfont.render("Combat Score: " + str(playerCombatScore), False, (200, 100, 0)), (10, 65))
        screen.blit(myfont.render("Time/Frames Survived: " + str(playerTime), False, (200, 200, 100)), (10, 95))
        ##################################
        # player rendered first
        screen.blit(PlayerSlime, PlayerSlime_rect)
        # all the npc slimes rendered
        for i in range (len(slimesArray)):
            screen.blit(slimesArray[i][0], slimesArray[i][1])

        ########test slime####### <---- SWITCH TO UPDATE NON slimeTheSlime SPRITES
        # screen.blit(slimeTheSlime.slimeSurface, slimeTheSlime.rectangle)
        ###################################################################
        ###################################################################

        ########UPDATE EVERYTHING THAT HAD BEEN PREPARED FOR THE NEXT "FRAME########
        pygame.time.wait(26)
        pygame.display.flip()

        if keys[5]:
            pygame.quit()
            sys.exit()

        playerTime += 1
    else:
        gameOver = True
        screen.fill(white)
        screen.blit(textsurface, (0, 0))
        screen.blit(myfont.render("LifePointsLeft: " + str(playerLifePoints), False, (200, 0, 0)), (10, 35))
        screen.blit(myfont.render("Combat Score: " + str(playerCombatScore), False, (200, 100, 0)), (10, 65))
        screen.blit(myfont.render("Time/Frames Survived: " + str(playerTime), False, (200, 200, 100)), (10, 95))
        ##################################
        # player rendered first
        screen.blit(PlayerSlime, PlayerSlime_rect)
        # all the npc slimes rendered
        for i in range(len(slimesArray)):
            screen.blit(slimesArray[i][0], slimesArray[i][1])

        screen.blit(myfont.render("Game Over at Time/Frame: " + str(playerTime), False, (200, 0, 0)), (300, 300))

        ########test slime####### <---- SWITCH TO UPDATE NON slimeTheSlime SPRITES
        # screen.blit(slimeTheSlime.slimeSurface, slimeTheSlime.rectangle)
        ###################################################################
        ###################################################################

        ########UPDATE EVERYTHING THAT HAD BEEN PREPARED FOR THE NEXT "FRAME########
        pygame.time.wait(26)
        pygame.display.flip()

        if keys[5]:
            pygame.quit()
            sys.exit()


    counter += 1

#############
pygame.quit()
sys.exit()
#############
