import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import simulation
from gui.colors import *
from physics.objects.basic import Circle
from physics.objects.spring import Spring

simulation.set_name("Ressort")

screen = simulation.screen
centery = simulation.height//2

# Mass
x = simulation.width//2
m = 50
v = 0

# Spring
k = 1
fixed_l = 250


# Objects
ressort = Spring((0, centery), (x - 20, centery), 20, fixed_l//10, 2, color=CLOUD)
simulation.add_object(ressort)
mass = Circle(x, centery, 20, SILVER)
mass.movable = True
simulation.add_object(mass)

@simulation.update
def update():
    global v, x

    actual_l = ressort.end_pos[0] - ressort.start_pos[0]
    l = (actual_l - fixed_l) / 10
    
    if not mass.dragging:
        a = (-k / m) * l
        v += a
        mass.pos += [v, 0]

    ressort.end_pos = [mass.pos.x - 20, mass.pos.y]

simulation.run()
