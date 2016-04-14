import random

import pygame


class Square(pygame.sprite.Sprite):
    ''' 
        Created on May 3, 2015

             The constructor has 6 required parameters: surface, color,
             starting x and y coordinates, speed and the size
             
        This class draws a square with the given parameters
        It has 4 methods: move, draw, reset, static_draw
        move: sets new coordinates for the square to be drawn
        draw: paints the square onto the surface with given coordinates
        reset: moves the square out of the screen from x axis
        static_draw: paints the square with the coordinates it was set with
        
        @author: Armen Seksenyan
        
        last Modified: June 2, 2015
    '''


    def __init__(self, screen, color, top, left, speed, size ):
        
        super().__init__();
        pygame.init()
        
        self.screen = screen
        self.color = color
        self.x = left
        self.y = top
        self.speed = speed
        self.size = size
        
        
        self.x_size = size
        self.y_size = size
       
        self.firstPoint  = (self.x, self.y)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x ,self.y + self.y_size)
  
        
    def draw(self, top, left, size): 
        ''' paints the square
            int: top and int: left for the location
            int: size for the size of the square
        ''' 
        self.x = top
        self.y = left
        self.x_size = size
        self.y_size = size
        
        self.firstPoint  = (self.x, self.y)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x ,self.y + self.y_size)
          
        pygame.draw.rect(self.screen, self.color, ((left, top), (size, size)) ,0)
        
    def move(self, screen):
        ''' takes a surface: screen to be used to change the x coordinate 
            and if the x coordinate is below or equal to 0 to call reset function
        '''
        self.x = self.x - self.speed
        
        self.firstPoint  = (self.x, self.y)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x ,self.y + self.y_size)
        
        if(self.x <0):
            self.reset(screen)
        
    def static_Draw(self, screen):  
        ''' takes a surface: screen
            uses the properties set to paint the square
        '''
        pygame.draw.rect(self.screen, self.color, ((self.x, self.y), (self.x_size, self.y_size)) ,0)
        
    def reset(self, screen):
        ''' takes a surface: screen to get the screen size
            resets the x value 5 pixels passed the screen width
            resets the y value randomly within the screen height
            
        '''
        self.x = screen.get_size()[0]+5
        self.y = random.randint(0, screen.get_size()[1]) 

