from typing import List

import pygame

from gui.colors import CLOUD, MIDNIGHT_BLUE, WHITE
from physics.objects import Object

pygame.init()

size = width, height = 720, 480
lauched = True

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

update_functions = []
objects: List[Object] = []
object_draging = None
offset = 0

def update(function):
    update_functions.append(function)

def add_object(obj):
    objects.append(obj)
    objects.sort(key=lambda obj: obj.priority)

def set_name(name):
    pygame.display.set_caption(name)

def run():
    global lauched, object_draging, offset
    while lauched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: lauched = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for obj in objects:
                    if obj.movable and obj.collidepoint(event.pos):
                        object_draging = obj
                        offset = obj.pos.x - event.pos[0]
            elif event.type == pygame.MOUSEMOTION:
                if object_draging != None:
                    object_draging.pos.x = event.pos[0] + offset
            elif event.type == pygame.MOUSEBUTTONUP:
                object_draging = None
    
        screen.fill(MIDNIGHT_BLUE)
        for fn in update_functions: fn()
        for obj in objects: obj.draw(screen)
        pygame.display.flip()
        clock.tick(60)
