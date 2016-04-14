
import random

import pygame


class Triangle(pygame.sprite.Sprite):
    ''' 
        Created on May 4, 2015

             The constructor has 6 required parameters: surface, color,
             starting x and y coordinates, speed and the size
             
        This class draws a triangle with the given parameters
        It has 5 methods: move, draw, reset, static_draw, rotateXaxis
        move: sets new coordinates for the square to be drawn
        draw: paints the triangle onto the surface with given coordinates
        reset: moves the triangle out of the screen from x axis
        static_draw: paints the triangle with the coordinates it was set with
        rotateXaxis: rotates the triangle against the x axis
        
        @author: Armen Seksenyan
        
        last Modified: June 2, 2015
    '''

    def __init__(self, surface,color, x_coordinate, y_coordinate, speed, size):
        

        super().__init__();
        pygame.init()
        
        self.screen = surface
        
        self.size = size
        self.color = color
        self.speed = speed
        
        self.first_x_coordinate = x_coordinate
        self.first_y_coordinate = y_coordinate
        
        self.second_x_coordinate = x_coordinate + size
        self.second_y_coordinate = y_coordinate
        
        self.third_x_coordinate = x_coordinate
        self.third_y_coordinate = y_coordinate + size
        
    
    def move(self, screen):
        ''' changes the x coordinates of the triangle 
            takes a surface: screen to be used if the x coordinate is below
            or equal to 0 to call reset function
        '''
        self.first_x_coordinate = self.first_x_coordinate - self.speed
        self.second_x_coordinate = self.second_x_coordinate - self.speed
        self.third_x_coordinate = self.third_x_coordinate - self.speed
        
        if(self.first_x_coordinate <= 0):
            self.reset(screen)
    
    def reset(self, screen):
        ''' takes a surface: screen to get the screen size
            resets the x value 5 pixels passed the screen width
            resets the y value randomly within the screen height
            changes the triangle with a random size between (10 - 50)
            
        '''
        self.size = random.randint(10, 50)
        self.first_x_coordinate = screen.get_size()[0]+5
        self.first_y_coordinate = random.randint(0, screen.get_size()[1])
        
        self.second_x_coordinate = self.first_x_coordinate + self.size
        self.second_y_coordinate = self.first_y_coordinate
        
        self.third_x_coordinate = screen.get_size()[0] + 5
        self.third_y_coordinate = self.first_y_coordinate + self.size

    def draw(self, x, y):
        ''' paints the triangle with
            int: x coordinate and 
            int: y coordinate for the location
        '''
        self.first_x_coordinate = x
        self.first_y_coordinate= y
        
        self.second_x_coordinate = x + self.size
        self.second_y_coordinate = y
        
        self.third_x_coordinate = x
        self.third_y_coordinate = y + self.size
        
        self.triangle = pygame.draw.polygon(self.screen, self.color, ((x,y), (x+ self.size, y),(x, y+ self.size)), 0)

    def rotateXaxis(self):
        ''' Rotates the triangle along the x axis'''
        
        self.third_y_coordinate = self.second_y_coordinate - self.size
            
    def static_Draw(self, screen):
        ''' takes a surface: screen
            uses the properties set to paint the triangle
        '''
        pygame.draw.polygon(self.screen, self.color, ((self.first_x_coordinate,self.first_y_coordinate), (self.second_x_coordinate, self.second_y_coordinate),(self.third_x_coordinate, self.third_y_coordinate)), 0)
        