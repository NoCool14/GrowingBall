
import random
import pygame


class Ball(pygame.sprite.Sprite):
    '''
        Created: April 29, 2015
        
        The constructor has 5 required parameters
        This class draws a circle with the given parameters
        it has 4 methods: move, draw, reset, statdraw
        move: redraws the circle with new coordinates
        draw: paints the circle onto the surface with given coordinates
        reset: moves the circle out of the screen from x axis
        static_draw: paints the circle with the coordinates it was set with
        
        @author: Armen Seksenyan
        
        last Modified: June 1, 2015
    '''
 

    def __init__(self, color,  x_coord, y_coord,  speed, radius):
        '''
            Constructor
        '''
        super().__init__();
        pygame.init()
        
        self.x = x_coord
        self.y = y_coord
        self.speed = speed
        self.radius = radius
        self.color = color
        
    def move(self, screen):
        ''''changes the x coordinates of the circle 
            takes a surface: screen to be used if the x coordinate is below
            or equal to 0 to call reset function
        '''
        self.x = self.x - self.speed
        if(self.x <0):
            self.reset(screen)
            
    def draw(self,screen,  x, y):
        ''' paints the circle onto a surface: screen using
            int: x coordinate and int: y coordinate for the location
        '''
        self.x = x
        self.y = y    
        pygame.draw.circle(screen, self.color, (x, y), self.radius, 0)
        
    
    def reset(self, screen):
        ''' takes a surface: screen to get the screen size
            resets the x value 30 pixels passed the screen width
            resets the y value randomly within the screen height
            
        '''
        self.x = screen.get_size()[0]+30
        self.y = random.randint(0, screen.get_size()[1])
        self.radius = random.randint(10, 60)
        
    def static_Draw(self, screen):
        ''' takes a surface: screen
            uses the properties set to paint the circle
        '''
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)