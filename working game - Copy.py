# 1 - Import library
import pygame
from pygame.locals import *
import math
import time
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
keys = [False, False]
keys2 = [False, False]
keys3 = [True, True]
player1pos=[5,5]
player2pos=[605,5]
ballpos = [320,240]
yspeed = 0.15
xspeed = 0.15
count = 0
flag = 0
flag2 = 0



# 3 - Load images
player1 = pygame.image.load("resources/redstick.png")
player2 = pygame.image.load("resources/bluestick.png")
ball = pygame.image.load("resources/ball.png")
gameover = pygame.image.load("resources/gameover2.png")
pause = pygame.image.load("resources/paused.png")
# 4 - keep looping through
while 1:
    if xspeed<0:
        xspeed = -0.15
    elif xspeed>0:
        xspeed = 0.15
    if yspeed<0:
        yspeed = -0.15
    else:
        yspeed = 0.15
  #   5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player1, player1pos)
    screen.blit(player2, player2pos)
    screen.blit(ball, ballpos)
    
  
        
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_s:
                keys[1]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_s:
                keys[1]=False
        if event.type == pygame.KEYDOWN:
            if event.key==K_i:
                keys2[0]=True
            elif event.key==K_k:
                keys2[1]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_i:
                keys2[0]=False
            elif event.key==pygame.K_k:
                keys2[1]=False
        if event.type == pygame.KEYDOWN:
            if event.key==K_p :
                flag2 = 1
                keys = [False,False]
                keys2 = [False,False]
                keys3 = [False,False]
                while flag2 == 1:
                     screen.blit(pause, [180,150])
                     pygame.display.flip()
                     time.sleep(3)
                     break
                     #if event.type == pygame.KEYDOWN:
                      #   if event.key==K_r:
                       #      flag2=0
                        #     break
                    
                    

     
        # 9 - Move player
    
    if keys[0]:
        if player1pos[1] < 0:
            keys[0] = False
        else:
            player1pos[1]-=0.5
    elif keys[1]:
        if player1pos[1] + 66 > 480:
            keys[1] = False
        else:
            player1pos[1]+=0.5
    if keys2[0]:
        if player2pos[1] < 0:
            keys2[0] = False
        else:
            player2pos[1]-=0.5
    elif keys2[1]:
        if 479<player2pos[1]+66<480:
            keys2[1] = False
        else:
            player2pos[1]+=0.5

  
    ballpos[1]+=yspeed
    ballpos[0]+=xspeed
    if ballpos[1] > 470 :
        #ballpos[1]+= -1*xspeed
        yspeed = -0.12
    elif ballpos[1] < 0 :
        yspeed = 0.12
        
  #  if ballpos[0] > 630 :
   #     xspeed = -0.12
    #elif ballpos[0] < 0 :
    #    xspeed = 0.12
    y = ballpos[1]
    x = ballpos[0]
    #print("hii" + str(y))
    #print("hii2" + str(player2pos[1]))
    if player2pos[1]-1 < y and y < player2pos[1]+67 and 595.16>ballpos[0]>595  :
        colp = y
        a = player2pos[1]+33-colp
        if a < 0 :
            yspeed = 0.12 + 0.01*abs(a)
            xspeed =-1*math.sqrt(abs(0.0288-yspeed))
        elif a >0:
            yspeed = -0.12 - 0.01*abs(a)
            xspeed =-1*math.sqrt(abs(0.0288-yspeed))
        
    if player1pos[1]-1<y and player1pos[1]+67 > y and 24.35< ballpos[0] < 25 :
        
        colp = y
        b = player1pos[1]+33-colp
        if b < 0 :
            yspeed = 0.12 + 0.01*abs(a)
            xspeed =1*math.sqrt(abs(0.0288-yspeed))
        elif b >0:
            yspeed = -0.12 - 0.01*abs(a)
            xspeed =1*math.sqrt(abs(0.0288-yspeed))


    if ballpos[0]+15 < 0 or ballpos[0] > 640 :
        flag = 1
        keys = [False,False]
        keys2 = [False,False]
        keys3 = [False,False]

    while flag == 1 :
        screen.blit(gameover, [180,150])
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        exit(0)
    
       
  

        
     
    

      

     
  
