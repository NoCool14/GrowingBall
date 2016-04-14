
from GrowingBall.ball import Ball


class Player(Ball):
    '''
        Created on May 6, 2015
        The constructor has 5 required parameters:
            surface: screen
            color: color
            int: x_coord
            int: y_coord
            int: radius
        This class draws a circle with the given parameters
        It inherits the Ball class so it has the four methods it inherits 
        4 methods: move, draw, reset, statdraw
        move: redraws the circle with new coordinates
        draw: paints the circle onto the surface with given coordinates
        reset: moves the circle out of the screen from x axis
        static_draw: paints the circle with the coordinates it was set with
        Two more methods of it's own
        distroyed: to return whether the player has been distroyed
        resizeBall: to resize the player
        
        @author: Armen Seksenyan
        
        last Modified: June 1, 2015
        @author: NoCool
    '''
    def __init__(self, screen, color,  x_coord, y_coord, radius):
        
        #super().__init__(screen, color, x_coord, y_coord, radius);
        self.screen = screen
        self.x = x_coord
        self.y = y_coord
        self.radius = radius
        self.color = color
        self.killed = False
        
    def resizeBall(self, multiplier):
        '''
            changes the radius of the ball
            takes a double: multiplier
        '''
        self.radius = int (self.radius + multiplier)
        if( self.radius <=1):
            self.killed = True
    def distroyed(self):
        '''
            returns if the player has been killed or not
        '''
        return self.killed