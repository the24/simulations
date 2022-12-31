from abc import ABC, abstractmethod
from typing import Self

import pygame

from gui.colors import Color
from physics.vector import Vector2D


class Object(ABC):
    
    def __init__(self,  pos: Vector2D, size: Vector2D, 
                        movable: bool = False,
                        color: Color = (0, 0, 0),
                        priority: int = 0) -> None:
        
        self.pos: Vector2D  = pos
        self.size: Vector2D = size

        self.movable: bool  = movable
        self.color: Color   = color
        self.priority: int  = priority
        
        self.dragging: bool = False

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        pass

    def collidepoint(self, point: Vector2D) -> bool:
        return all(self.pos < point) and all(point < (self.pos + self.size))

    def centerx(self, screen: pygame.Surface) -> Self:
        self.x = screen.get_width() // 2 - self.size.x // 2
        return self

    def centery(self, screen: pygame.Surface) -> Self:
        self.y = screen.get_height() // 2 - self.size.y // 2
        return self

    def center(self, screen: pygame.Surface) -> Self:
        self.centerx(screen)
        self.centery(screen)
        return self
