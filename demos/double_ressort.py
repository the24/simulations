import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

import simulation
from gui.colors import CLOUD, SILVER
from physics.objects.basic import Circle
from physics.objects.spring import Spring

simulation.set_name("Double ressort")

centery = simulation.height//2

m1 = 100
fixed_l1 = 100
k1 = 2
x1 = 100
v1 = 0

m2 = 100
fixed_l2 = 100
k2 = 1
x2 = 150
v2 = 0


ressort1 = Spring((0, centery), (100, centery), 20, fixed_l1//10, 2, color=CLOUD)
simulation.add_object(ressort1)
mass1 = Circle(x1, centery, 25, movable=True, color=SILVER)
simulation.add_object(mass1)
ressort2 = Spring((x1, centery), (x2, centery), 20, fixed_l2//10, 2, color=CLOUD)
simulation.add_object(ressort2)
mass2 = Circle(x2, centery, 25, movable=True, color=SILVER)
simulation.add_object(mass2)

@simulation.update
def update():
    global v1, v2

    l1 = (ressort1.lenght() - fixed_l1) / 10
    l2 = (ressort2.lenght() - fixed_l2) / 10

    if  simulation.object_draging is not mass1 and \
        simulation.object_draging is not mass2:

        a1 = -(k1/m1)*l1 + (k2/m2)*l2
        a2 = -(k2/m2)*l2
        
        v1 += a1
        mass1.pos.x += v1
        
        v2 += a2
        mass2.pos.x += v2

    ressort1.end_pos = mass1.pos.x - 25, mass1.pos.y
    ressort2.start_pos = mass1.pos.x + 25, mass1.pos.y
    ressort2.end_pos = mass2.pos.x - 25, mass2.pos.y


simulation.run()
