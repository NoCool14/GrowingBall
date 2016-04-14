'''
Created on Apr 29, 2015

A game that the player needs to collect circles and avoid other objects
until the countdown to the next level.
The goal of the game is to get the highest score.

The player has a couple of powerUps: 

    Shield which prevents objects from shrinking and taking away points
    Freezer which freezes objects for a few seconds.
@author: Armen Seksenyan

Last modified: June 7, 2015
'''
 

import random
import threading
import time

import pygame
from pygame.locals import USEREVENT

from GrowingBall import triangle, square, shield, freezer
from GrowingBall.ball import Ball
from GrowingBall.collision_detection import CollisionDetection
from GrowingBall.freezer import Freezer
from GrowingBall.player import Player
from GrowingBall.shield import Shield
from GrowingBall.square import Square
from GrowingBall.triangle import Triangle


#list of colors to be used in the game
BLACK       = (  0,  0,    0)
WHITE       = (255,255,  255)
RED         = (255,  0,    0)
BLUE        = (0,    0,  255)
GREEN       = (0,  255,    0)
LIGHT_BLUE  = (15, 176,  225)

# Set the height and width of the screen
screen_width = 800  
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])


background_image = pygame.image.load("background.jpg").convert()

 
def main():
    # Initialize Pygame
    pygame.init()
    
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    nextLevelTimer = 40
    screen.blit(background_image, (0, 0))
    clock = pygame.time.Clock()

    score = 0
    FPS = 30 
    global player, playerShieldisOn, collectablesFreezerOn
    
    player = Player(screen, RED, 69, 69, 100)
    
    #define the playerLevel
    playerLevel = 1
    
    #playerSchield
    playerShield = Shield(screen, GREEN, 1000, 100, 25 , 25)
    
    #freezer
    freezeGame = Freezer(screen, LIGHT_BLUE, 100, 100, 10, 20)

    #define the shrinkCounter    
    shrinkCounter = 0
    
    #create a collision detector
    collisionDetector = CollisionDetection()
    
    #create the objects to for the game
    collectableCircles = gen_collectable_circles(5)
    avoidableTriangles = gen_avoidable_triangles(2)
    avoidableSquares   = gen_avoidable_squares(5)
    
    #create a shield  group
    collectableShields = pygame.sprite.Group()
    collectableShields.add(playerShield)
    
    #create a freezer group
    collectableFreezers = pygame.sprite.Group()
    collectableFreezers.add(freezeGame)
    
    
    #Used to set the countdown to the next level
    pygame.time.set_timer(USEREVENT + 1, 1000)
    
    #set the initial state of the shield
    playerShieldisOn = False
    
    #set the initial state of the freezer
    collectablesFreezerOn = False
    
     
    running = True
      
    while running:
        
        
        #hide the mounse
        pygame.mouse.set_visible(False)
        
        #determine what keys are pressed
        keys = pygame.key.get_pressed()
        
        #handle the events in teh game
        for event in pygame.event.get():
            #quit the game if window is closed
            if event.type == pygame.QUIT:
                running = False
            if(keys[pygame.K_q]):
                running = False
            #restart the game by user after the game is over
            if(keys[pygame.K_SPACE] and player.distroyed()):
                player.killed = False
                playerLevel = 1
                score = 0
                nextLevelTimer = 43
                newLevel(background, playerLevel)
            # used to countdown to the next level    
            if(event.type == USEREVENT + 1):
                nextLevelTimer = nextLevelTimer -1
                #if the coundown is done, start new level
                if(nextLevelTimer <=0 and not player.distroyed()):
                    playerLevel = playerLevel + 1
                    nextLevelTimer = (40 * playerLevel)  + 3
                    score = score + 300
                    newLevel(background, playerLevel)
        #if the player is dead, blit the game over screen   
        if(player.distroyed()):
            screen.blit(background, (0,0))
            font = pygame.font.Font(None, 50)
            font1 = pygame.font.Font(None, 30)
            gameOver = font.render("GAMEOVER!!! SCORE: " + str(score), 1, (0, 0, 0))
            startOver = font1.render("PRESS SPACEBAR TO RESTART", 1, (0,0,0))
            startOver2 = font1.render("PRESS Q TO QUIT", 1, (0,0,0))
            screen.blit(gameOver, (200, 150))
            screen.blit(startOver, (250, 250))
            screen.blit(startOver2, (275, 350))
            pygame.display.update()
        #if the player is alive     
        else:
            background.fill((0, 255, 0))
            screen.blit(background_image, (0, 0))
            #get the position of the mouse
            mousePosition = pygame.mouse.get_pos()
            #draw the player based on mouse position
            player.draw(screen, mousePosition[0], mousePosition[1])  
            
            #detect collisions between the player and collectableFreezers to stop enemy moving for a few seonnds                    
            if(not collectablesFreezerOn):
                for freezer in collectableFreezers:
                    
                    freezer.static_Draw(screen)
                    
                    if(collisionDetector.circle_sixSidedPolygon_collision(player, freezer)):
                        collectablesFreezerOn = True
                        resettingFreezer = threading.Thread(target=resetFreezer, kwargs={'seconds': 5})
                        resettingFreezer.start()
                        freezer.reset(screen)
                    freezer.static_Draw(screen) 
                    freezer.move(screen)
                    
                #if the player shield is not one detect collisions with shields 
            if(not playerShieldisOn):
                for shield in collectableShields:
                        
                    shield.static_Draw(screen)
                    #if collision is detected turn on the shield and reset the position of the shield
                    # and start the timer for the shield
                    if (collisionDetector.circle_fiveSidedPolygon_collision(player, shield)):
                        playerShieldisOn = True
                        resettingShield = threading.Thread(target=resetShield, kwargs={'seconds' : 5})
                        resettingShield.start()
                        shield.reset(screen)
                        shield.static_Draw(screen)
                    shield.move(screen)           
            #detect if there are any collisions between the player and triangles 
            for triangle in avoidableTriangles:
                triangle.static_Draw(screen)
                if(collisionDetector.circle_triangle_collision(player, triangle)):
                    triangle.reset(screen)
                    #randomly rotate triangles
                    if(not random.getrandbits(1)):
                        triangle.rotateXaxis()
                    triangle.static_Draw(screen)
                    if (not playerShieldisOn): # if the player shield is not on shrink the 
                                                #player and decrease the score
                        score = score - 1
                        player.resizeBall(-(triangle.size/20)) 
                if(not collectablesFreezerOn):
                    triangle.move(screen)
            #detect collisions between the player and squares and decrease the score and shrink the ball        
            for square in avoidableSquares:
                square.static_Draw(screen)   
                if(collisionDetector.circle_fourSidedPolygon_collision(player, square)):
                    square.reset(screen)
                    if (not playerShieldisOn): # if the player shield is not on shrink the 
                                                #player and decrease the score
                        score = score - 2
                        player.resizeBall(-1.5) 
                if(not collectablesFreezerOn):
                    square.move(screen)
            
            #detect collisions between the player and circles and increase the score and enlarge the ball        
            for ball in collectableCircles:  
                ball.static_Draw(screen)
                if (collisionDetector.circle_circle_collision(player, ball)):
                    ball.reset(screen)
                    ball.static_Draw(screen)
                    score = score + 1
                    player.resizeBall(ball.radius/20)
                ball.move(screen)    
            
            #shrink the player every second to make it harder     
            if(shrinkCounter >= FPS):
                player.resizeBall(-playerLevel - (playerLevel/2) -.5)
                shrinkCounter = 0
           
            #increase shrinkcounter to go with the FPS to make it 1 per second    
            shrinkCounter = shrinkCounter +1    
        
            #function to update score
            scoring(score)
            
            #function to blit coundown for next level
            nextLevelCountdown(screen, nextLevelTimer)
        clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()
    
def gen_collectable_circles(num):
    '''Returns a list of circle objects
        takes int: num of cirlces to make and
        returns sprite.Group: circleSprites'''
    circlesSprites = pygame.sprite.Group()

    for x in range(num):
        rand_x = random.randint(0, 600)
        rand_y = random.randint(0, 500)
        rand_size = random.randint(10, 60)
        rand_speed = random.randint(1,10)
        circleSprite = Ball(BLACK, rand_x, rand_y,rand_speed, rand_size)
        circlesSprites.add(circleSprite)
        x= x
    return circlesSprites

def gen_avoidable_triangles(num):
    '''Returns a list of triangle objects
        takes int: num of triangles to make and
        returns sprite.Group: trianglesSprites'''
    triangleSprites = pygame.sprite.Group()
    
    for x in range(num):
        rand_x = random.randint(0, 600)
        rand_y = random.randint(0, 500)
        rand_size = random.randint(10, 50)
        rand_speed = random.randint(1,10)
        triangleSprite = Triangle(screen, BLUE, rand_x, rand_y, rand_speed, rand_size)
        triangleSprites.add(triangleSprite)
        x = x
    return triangleSprites

def gen_avoidable_squares(num):
    '''Returns a list of square objects
        takes int: num of squares to make and
        returns sprite.Group: squareSprites'''
    squareSprites = pygame.sprite.Group()
    
    for x in range(num):
        rand_x = random.randint(0, 600)
        rand_y = random.randint(0, 500)
        rand_size = random.randint(20, 40)
        rand_speed = random.randint(1,10)
        squareSprite = Square(screen, WHITE, rand_x, rand_y, rand_speed, rand_size)
        squareSprites.add(squareSprite)
        x =x
    return squareSprites

def scoring(score):
    '''places the score on the screen
        gets a int: score and blits it on the screen'''
    
    font=pygame.font.Font(None,30)
    instructions = font.render("score: " + str(score), 1, (0,0,0))
    screen.blit(instructions, (50, 120))

def newLevel(background, playerLevel):
    ''' sets a new level by updating and reset the settings
        gets a surface: background and int: playerLevel to create a new level'''
   
    newLevel = 3
    player.radius = 100
    while(newLevel >0):
        screen.blit(background, (0,0))
        font = pygame.font.Font(None, 50)
        instructions = font.render("Level " + str(playerLevel)+ " Starts in: " + str(newLevel), 1, (0, 0, 0))
        screen.blit(instructions, (250, 300))
        pygame.display.update()
        pygame.time.wait(1000)
        newLevel = newLevel - 1
        
        

def nextLevelCountdown(screen, nextLevelTimer):
    ''' Counts down the timer for the next level
        takes a surface: screen and int: nextLevelTimer to blit on the screen'''
    font=pygame.font.Font(None,30)
    countDown = font.render("countDown: " + str(nextLevelTimer), 1, (0,0,0))
    screen.blit(countDown, (50, 75))         

def resetShield(seconds):
    '''resets the shield to turn off after int: seconds'''
    global playerShieldisOn
    time.sleep(seconds)
    playerShieldisOn = False

def resetFreezer(seconds):
    '''reset the freezer to turn off after int: seconds'''
    global collectablesFreezerOn
    time.sleep(seconds)
    collectablesFreezerOn = False
   
if __name__ == '__main__':
    main()
    