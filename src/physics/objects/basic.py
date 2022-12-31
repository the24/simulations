from math import floor
from typing import List, Self

import numpy as np
import pygame

from gui.colors import Color
from physics.objects import Object
from physics.vector import Vector2D


class Rect(Object):
    
    def __init__(self,  pos: Vector2D, size: Vector2D,
                        movable: bool = False,
                        color: Color = (0, 0, 0),
                        priority: int = 0) -> None:
        
        super().__init__(pos, size, movable, color, priority)
    
    @property
    def edges(self) -> List:
        edges = []

        start = Vector2D(self.pos.x, self.pos.y)
        end = Vector2D(self.pos.x, self.pos.y+self.size.y)
        edges.append(Line(start, end))

        start = Vector2D(self.pos.x, self.pos.y)
        end = Vector2D(self.pos.x+self.size.x, self.pos.y)
        edges.append(Line(start, end))

        start = Vector2D(self.pos.x+self.size.x, self.pos.y)
        end = Vector2D(self.pos.x+self.size.x, self.pos.y+self.size.y)
        edges.append(Line(start, end))

        start = Vector2D(self.pos.x, self.pos.y+self.size.y)
        end = Vector2D(self.pos.x+self.size.x, self.pos.y+self.size.y)
        edges.append(Line(start, end))

        return edges
    
    def draw(self, screen):
        rect = (*self.pos, *self.size)
        pygame.draw.rect(screen, self.color, rect)


class Square(Rect):

    def __init__(self,  pos: Vector2D, side_size: int,
                        movable: bool = False,
                        color: Color = (0, 0, 0),
                        priority: int = 0) -> None:
        
        super().__init__(pos, np.array([side_size, side_size]), movable, color, priority)

        self.side_size = side_size


class Line(Object):

    def __init__(self,  start: Vector2D, end: Vector2D,
                        movable: bool = False,
                        color: Color = (0, 0, 0),
                        priority: int = 0,
                        weight: int = 1) -> None:
        size = abs(end - start)
        super().__init__(start, size, movable, color, priority)
        self.weight = weight
        self._start_pos = start
        self._end_pos = end
    
    @property
    def start_pos(self):
        return self._start_pos

    @start_pos.setter
    def start_pos(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            if len(value) != 2: raise Exception
            self._start_pos = np.array(value)
        elif isinstance(value, np.ndarray):
            self._start_pos = value
        else: raise Exception

    @property
    def end_pos(self):
        return self._end_pos

    @end_pos.setter
    def end_pos(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            if len(value) != 2: raise Exception
            self._end_pos = np.array(value)
        elif isinstance(value, np.ndarray):
            self._end_pos = value
        else: raise Exception

    def center_start_y(self, screen: pygame.Surface):
        self.y = screen.get_height() // 2
        return self

    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, self.color, self._start_pos, self.start_pos, floor(self.weight))


class Circle(Object):
    
    def __init__(self, x, y, r, movable=False, color=(0, 0, 0), priority=0) -> None:
        center = Vector2D(x, y)
        super().__init__(center, Vector2D(r, r), movable, color, priority)
        self.r = r

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.pos.to_vec(), self.r)
    
    def collidepoint(self, point: Vector2D) -> bool:
        diff: Vector2D = self.pos - point
        return diff.longer_than(self.size)
    
    def collidecircle(self, circle: Self) -> bool:
        diff: Vector2D = self.pos - circle.pos
        return diff.x**2 + diff.y**2 < (self.r + circle.r)**2
    
    #FIXME
    def collideline(self, line: Line) -> bool:
        x1 = line.start_pos.x
        y1 = line.start_pos.y
        x2 = line.end_pos.x
        y2 = line.end_pos.y
        xc = self.pos.x
        yc = self.pos.y
        return abs((x2-x1)*(y1-yc) - (x1 - xc)*(y2 - y1)) <= 0

    def colliderect(self, rect: Rect) -> bool:
        edges = rect.edges
        return (rect.collidepoint(self.pos) or
            self.collideline(edges[0]) or
            self.collideline(edges[1]) or
            self.collideline(edges[2]) or
            self.collideline(edges[3]))