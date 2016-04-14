        
import math
import pygame


class CollisionDetection(object):

    def __init__(self):  
        
        '''
            Created: May 6, 2015
            
            Detects different types of collisions between sprites
            it has 7 methods: circle_fiveSidedPolygon_collision,
                              circle_fourSidedPolygon_collision
                              circle_sixSidedPolygon_collision,
                              circle_triangle_collision,
                              circle_circle_collision,
                              circle_line_collision,
                              closest_point_on_seg
                              
                              
            @author: Armen Seksenyan
            
            Last modified: May, 29, 2015

        '''
            
    
    def circle_fiveSidedPolygon_collision(self, firstSprite, secondSprite):
        circleRadius = firstSprite.radius
        circleCenter = (firstSprite.x, firstSprite.y)
        
        if(self.circle_line_collision(secondSprite.firstPoint, secondSprite.secondPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.secondPoint, secondSprite.thirdPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.thirdPoint, secondSprite.forthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.forthPoint, secondSprite.fifthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.fifthPoint, secondSprite.firstPoint, circleCenter, circleRadius)):
            return True
        else:
            return False
    def circle_fourSidedPolygon_collision(self, firstSprite, secondSprite):
        circleRadius = firstSprite.radius
        circleCenter = (firstSprite.x, firstSprite.y)
        
        if(self.circle_line_collision(secondSprite.firstPoint, secondSprite.secondPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.secondPoint, secondSprite.thirdPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.thirdPoint, secondSprite.forthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.forthPoint, secondSprite.firstPoint, circleCenter, circleRadius)):
            return True
        else:
            return False
        
    def circle_sixSidedPolygon_collision(self, firstSprite, secondSprite):
        circleRadius = firstSprite.radius
        circleCenter = (firstSprite.x, firstSprite.y)
        if(self.circle_line_collision(secondSprite.firstPoint, secondSprite.sixthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.sixthPoint, secondSprite.secondPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.secondPoint, secondSprite.thirdPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.thirdPoint, secondSprite.forthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.forthPoint, secondSprite.fifthPoint, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(secondSprite.fifthPoint, secondSprite.firstPoint, circleCenter, circleRadius)):
            return True
        else:
            return False
    # find collisions with triangle
    def circle_triangle_collision(self, firstSprite, secondSprite):
        circleRadius = firstSprite.radius
        circleCenter = (firstSprite.x, firstSprite.y)
        trianglesFirstCoordinate = (secondSprite.first_x_coordinate, secondSprite.first_y_coordinate)
        triangelsSecondCoordinate = (secondSprite.second_x_coordinate, secondSprite.second_y_coordinate)
        trianglesThirdCoordinate = (secondSprite.third_x_coordinate, secondSprite.third_y_coordinate)
        
        if(self.circle_line_collision(trianglesFirstCoordinate, triangelsSecondCoordinate, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(trianglesFirstCoordinate, trianglesThirdCoordinate, circleCenter, circleRadius)):
            return True
        elif(self.circle_line_collision(triangelsSecondCoordinate, trianglesThirdCoordinate, circleCenter, circleRadius)):
            return True
        else:
            return False
    def circle_circle_collision(self, firstBall, secondBall):
        dx = firstBall.x - secondBall.x;
        dy = firstBall.y - secondBall.y;
        distance = math.sqrt(dx * dx + dy * dy);

        if (distance < firstBall.radius + secondBall.radius):
            return True
        else:
            return False
    
    def closest_point_on_seg(self, seg_a, seg_b, circ_pos):
        seg_a = pygame.math.Vector2(seg_a)
        seg_b = pygame.math.Vector2(seg_b)
        
        circ_pos = pygame.math.Vector2(circ_pos)
        
        seg_v = seg_b - seg_a
        if (seg_v.length() <= 0):
            seg_v = seg_a - seg_b
       
        pt_v = circ_pos - seg_a
        if seg_v.length() <= 0:
            raise ValueError("Invalid segment length")
        seg_v_unit = seg_v / seg_v.length()
        proj = pt_v.dot(seg_v_unit)
        
        if proj <= 0:
            return seg_a
        if proj >= seg_v.length():
            return seg_b
        
        proj_v = seg_v_unit * proj
        closest = proj_v + seg_a
        return closest

    def circle_line_collision(self, linesFirstPoint, linesSecondPoint, circleCenter, circleRadius):
        closest = self.closest_point_on_seg(linesFirstPoint, linesSecondPoint, circleCenter)
        dist_v = circleCenter - closest
        if dist_v.length() > circleRadius:
            return False
        else:
            return True