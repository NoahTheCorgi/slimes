import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys, slimeClass, time
#from pygame.locals import *
"""
#Remaining Tasks: (might have fixed this... need to double check...)
# I found a bug where if a BallTheSlime corners one of the slimes completely perfectly in the corner,
#the BallTheSlime stops moving and the game is in a stale
# fixing this bug should be easy just an extra claus
"""

pygame.init() #set up for general variables and general prepartion

keys = [False, False, False, False, False, False] #up, left, down, right, space, ESC

black = 0, 0, 0
red = 200, 0, 0
green = 0,200,0
white = 255,255,255

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

#starting velocity for general non BallTheSlime sprites/slimes
speed = [2, 2] #velocity is a better variable name for this since vector

########___BallTheSlime Coordinates#######
x = 200
y = 200
####################################

###############___set up for displaying the title etc###############
####################################################################
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('Slimes The Game by NoahTheCorgi', False, (0, 200, 0))
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


###################set up non BallTheSlime sprites using the slimeClass###################
####################################################################################
####################################################################################
"""Set up for the first original non BallTheSlime slime (this should thus be integrated for the rest of the slimes"""
ball = pygame.image.load("animation/red_slime.png")
ballrect = ball.get_rect(center = (300,300))
####################################################################################
BallTheSlime = slimeClass.slime("animation/green_slime_0.png", "slime2", (100,100), 0 , 0)
BallTheSlime.set_animation("animation")

########################################################
######################The_Frames########################
########################################################
i=0
while 1:
    #time.sleep(1)

    if i > 99:
        i = 0

    ###################___Get information about user inputs___##################
    ############################################################################
    ############################################################################
    for event in pygame.event.get():

        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                keys[5] = True

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_LEFT:
                keys[1]=True
            elif event.key==pygame.K_DOWN:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True
            elif event.key==pygame.K_SPACE:
                keys[4]=True


        if event.type == pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
            elif event.key==pygame.K_DOWN:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
            elif event.key==pygame.K_SPACE:
                keys[4]=False
    ###################################################################
    ###################################################################
    ###################################################################


    ########################___Update with respect to the user inputs#########################
    if keys[4]:

        if i%25 < 13:
            PlayerSlime = pygame.image.load("animation/green_slime_0.png")
        else:
            PlayerSlime = pygame.image.load("animation/green_slime_1.png")

        if keys[0]:#UP
            keep_inside_screen(x,y)
            if check_inside_screen(x, y-10) and not ballrect.colliderect(PlayerSlime_rect):
                y-=10
        if keys[1]:#LEFT
            keep_inside_screen(x,y)
            if check_inside_screen(x-10, y) and not ballrect.colliderect(PlayerSlime_rect):
                x-=10
        if keys[2]:#DOWN
            keep_inside_screen(x,y)
            if check_inside_screen(x, y+10) and not ballrect.colliderect(PlayerSlime_rect):
                y+=10
        if keys[3]:#RIGHT
            keep_inside_screen(x+10,y)
            if check_inside_screen(x+10, y) and not ballrect.colliderect(PlayerSlime_rect):
                x+=10
    else:
        if i%25 < 13:
            PlayerSlime = pygame.image.load("animation/slime.png")
        else:
            PlayerSlime = pygame.image.load("animation/slime_1.png")
        if keys[0]:#UPs
            keep_inside_screen(x,y)
            if check_inside_screen(x, y-10) and not ballrect.colliderect(PlayerSlime_rect):
                y-=5
        if keys[1]:#LEFT
            keep_inside_screen(x,y)
            if check_inside_screen(x-10, y) and not ballrect.colliderect(PlayerSlime_rect):
                x-=5
        if keys[2]:#DOWN
            keep_inside_screen(x,y)
            if check_inside_screen(x, y+10) and not ballrect.colliderect(PlayerSlime_rect):
                y+=5
        if keys[3]:#RIGHT
            keep_inside_screen(x+10,y)
            if check_inside_screen(x+10, y) and not ballrect.colliderect(PlayerSlime_rect):
                x+=5
    ###################################################################



    ##################___UPDATE ALL WITH RESPECT TO VELOCITY... ALL SPRITES___#######################
    #################################################################################################
    #################################################################################################
    ballrect = ballrect.move(speed)
    if ballrect.left < 0:
        ballrect.left = 1
        speed[0] = -speed[0]
    if ballrect.right > width:
        ballrect.right = width -1
        speed[0] = -speed[0]

    if ballrect.top < 0 :
        ballrect.top = 1
        speed[1] = -speed[1]
    if ballrect.bottom > height:
        ballrect.bottom = height -1
        speed[1] = -speed[1]


    PlayerSlime_rect = PlayerSlime.get_rect(center = (x,y)) #this is how you update the BallTheSlime slime location
    #a better way to do this would be to use the rectangle.move() function and update the speed to zero when not moving,,,

    x_axis_diff = (ballrect.center[0] - PlayerSlime_rect.center[0])
    y_axis_diff = (ballrect.center[1] - PlayerSlime_rect.center[1])
    if ballrect.colliderect(PlayerSlime_rect):
        if x_axis_diff!=0 and y_axis_diff!=0:
            speed[0] = 2*x_axis_diff/abs(x_axis_diff)
            speed[1] = 2*y_axis_diff/abs(y_axis_diff)
    ###################################################################
    ###################################################################
    ###################################################################



    #########################_ANIMATE_#################################
    ###################################################################
    if i%25 < 13:
        ball = pygame.image.load("animation/red_slime_1.png")
    else:
        ball = pygame.image.load("animation/red_slime.png")

    if i%25 <6:
        #we skip zero because there is always a hidden file at the start created.
        BallTheSlime.slimeSurface = pygame.image.load(BallTheSlime.animation[1])
    elif i%25 <12:
        BallTheSlime.slimeSurface = pygame.image.load(BallTheSlime.animation[2])
    elif i%25 <18:
        BallTheSlime.slimeSurface = pygame.image.load(BallTheSlime.animation[3])
    elif i%25 <25:
        BallTheSlime.slimeSurface = pygame.image.load(BallTheSlime.animation[4])
    ###################################################################
    ###################################################################


    #########################___"Blits"___#############################
    ###################################################################
    screen.fill(white)
    screen.blit(textsurface,(0,0))
    ##################################
    screen.blit(ball, ballrect)
    screen.blit(PlayerSlime, PlayerSlime_rect)

    ########test slime####### <---- SWITCH TO UPDATE NON BallTheSlime SPRITES
    screen.blit(BallTheSlime.slimeSurface, BallTheSlime.rectangle)
    ###################################################################
    ###################################################################

    ########UPDATE EVERYTHING THAT HAD BEEN PREPARED FOR THE NEXT "FRAME########
    pygame.time.wait(26)
    pygame.display.flip()

    if keys[5]:
        pygame.quit()
        sys.exit()

    i+=1


#############
pygame.quit()
sys.exit()
#############
