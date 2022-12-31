import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import simulation
from gui.colors import *
from physics.objects.basic import Circle, Rect
from physics.vector import Vector2D

simulation.set_name("Collitions")

centery = simulation.height//2

m1 = 25
pos1 = Vector2D.from_vec([100, centery])
v1 = Vector2D.from_vec([2, 0])

m2 = 25
pos2 = Vector2D.from_vec([400, centery])
v2 = Vector2D.from_vec([0, 0])


ball1 = Circle(*pos1, m1, movable=True, color=SILVER)
simulation.add_object(ball1)
ball2 = Circle(*pos2, m1, movable=True, color=SILVER)
simulation.add_object(ball2)

rect_left = Rect(Vector2D.from_vec([50, centery-50]), Vector2D.from_vec([10, 100]))
simulation.add_object(rect_left)

rect_right = Rect(Vector2D.from_vec([simulation.width - 50, centery-50]), Vector2D.from_vec([10, 100]))
simulation.add_object(rect_right)

@simulation.update
def update():
    global v1, v2

    if  not ball1.dragging and not ball2.dragging:

        a1 = 0
        a2 = 0
        
        #v1 += a1
        ball1.pos += v1
        
        #v2 += a2
        ball2.pos += v2
    
    if ball1.collidecircle(ball2):
        u1 = v1
        u2 = v2
        v1 = (u2*2*m2 + u1*(m1 - m2)) / (m1 + m2)
        v2 = (u1*2*m1 + u2*(m2 - m1)) / (m1 + m2)
    
    if ball1.colliderect(rect_left) or ball1.colliderect(rect_right):
        v1 *= -1
    if ball2.colliderect(rect_left) or ball2.colliderect(rect_right):
        v2 *= -1


simulation.run()
