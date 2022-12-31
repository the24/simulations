from math import sqrt

import pygame

from physics.objects import Object
from physics.vector import Vector2D


#TODO: A refaire
class Spring(Object):

    def __init__(self, start_pos: Vector2D, end_pos: Vector2D, height: int, nb_loops: int, weight: int,
                       movable=False, color=(0, 0, 0), priority=0) -> None:
        w = abs(start_pos[0] - end_pos[0])
        super().__init__(start_pos, [w, height], movable, color, priority)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.nb_loops = nb_loops
        self.h = height
        self.weight = weight
    
    def lenght(self):
        return sqrt((self.end_pos[0] - self.start_pos[0])**2 + (self.end_pos[1] - self.start_pos[1])**2)

    def draw(self, screen):
        lenght = self.lenght()
        loop_size = lenght/self.nb_loops
        prev_coord = self.start_pos
        
        for i in range(self.nb_loops):
            #print(prev_coord)
            start_pos = prev_coord
            end_pos = (prev_coord[0] + loop_size/2, prev_coord[1] + self.h/2)
            if i % 2 == 0: end_pos = (end_pos[0], end_pos[1] - self.h)
            pygame.draw.line(screen, self.color, start_pos, end_pos, self.weight)
            start_pos = end_pos
            end_pos = (prev_coord[0] + loop_size, prev_coord[1])
            pygame.draw.line(screen, self.color, start_pos, end_pos, self.weight)
            prev_coord = end_pos