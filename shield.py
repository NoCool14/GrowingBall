import random

import pygame


class Shield(pygame.sprite.Sprite):
    '''
        Created on May 4, 2015



             The constructor has 6 required parameters: surface, color,
             starting x and y coordinates, speed and the size
         
        This class draws a pentagon with the given parameters
        along with a letter inside the pentagon.
        It has 4 methods: move, draw, reset, static_draw
        move: redraws the pentagon with new coordinates
        draw: paints the pentagon onto the surface with given coordinates
        reset: moves the pentagon out of the screen from x axis
        static_draw: paints the pentagon with the coordinates it was set with
        
        @author: Armen Seksenyan
        
        last Modified: June 1, 2015
    '''

    def __init__(self, surface, color, x_coordinate, y_coordinate, speed, size):
    
        super().__init__();
        pygame.init()
        self.screen = surface
        self.color = color
        self.speed = speed
        
        self.font=pygame.font.Font(None,30)
        self.ShieldLogo = self.font.render(" S ", 1, (0,0,0))

        
        self.x = x_coordinate
        self.y = y_coordinate
        self.x_size = size
        self.y_size = size
        self.x_middle = int(self.x_size/2)
        self.y_middle = int(self.y_size/8)+ 10
        
        self.firstPoint  = (x_coordinate, y_coordinate)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x + self.x_size- self.x_middle,self.y + self.y_middle + self.y_size)
        self.fifthPoint  = (self.x, self.y+ self.y_size)
  
    def move(self, screen):
        ''' changes the x coordinates of the hexagon 
            takes a surface: screen to be used if the x coordinate is below
            or equal to 0 to call reset function
        '''
        self.x = self.x - self.speed
        
        self.firstPoint  = (self.x, self.y)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x + self.x_size- self.x_middle,self.y + self.y_middle + self.y_size)
        self.fifthPoint  = (self.x, self.y+ self.y_size)
        
        if(self.x <= 0):
            self.reset(screen)
    
    def reset(self, screen):
        ''' takes a surface: screen to get the screen size
            resets the x value 1500 pixels passed the screen width
            resets the y value randomly within the screen height
            
        '''
        self.x =  screen.get_size()[0]+1500
        self.y = random.randint(0, screen.get_size()[1])
    def draw(self, x_coordinate, y_coordinate, size):
        ''' paints the pentagon with a letter S using
            int: x coordinate and int: y coordinate for the location
            int: size for the size
        '''
        self.x = x_coordinate
        self.y = y_coordinate
        self.x_size = size
        self.y_size = size
        self.x_middle = int(self.x_size/2)
        self.y_middle = int(self.y_size/8)+ 10
        
        self.firstPoint  = (x_coordinate, y_coordinate)
        self.secondPoint = (self.x + self.x_size ,self.y)
        self.thirdPoint  = (self.x + self.x_size ,self.y+ self.y_size)
        self.forthPoint  = (self.x + self.x_size- self.x_middle,self.y + self.y_middle + self.y_size)
        self.fifthPoint  = (self.x, self.y+ self.y_size)

        pygame.draw.polygon(self.screen, self.color, ((self.firstPoint), (self.secondPoint),(self.thirdPoint), (self.forthPoint), (self.fifthPoint), (self.firstPoint)), 0)
        self.screen.blit(self.freezerLogo, (self.x, self.y+ 5))
              
    def static_Draw(self, screen):
        ''' takes a surface: screen
            uses the properties set to paint the pentagon with a S
        '''
        pygame.draw.polygon(self.screen, self.color, (self.firstPoint, self.secondPoint,self.thirdPoint, self.forthPoint, self.fifthPoint,self.firstPoint), 0)
        self.screen.blit(self.ShieldLogo, (self.x, self.y + 5))
