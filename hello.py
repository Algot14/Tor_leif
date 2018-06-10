# Imports
# -------

import time
from poppy.creatures import PoppyTorso


# Setup
# -----


# With a real robot
# poppy = PoppyTorso()

# Using the V-REP simulator
poppy = PoppyTorso(simulator='vrep')

# Check motors and sensors
# ------------------------

# How many motors do I have
print(len(poppy.motors))

# What are the positions
for m in poppy.motors:
    print(m.present_position)

# What are their names
for m in poppy.motors:
    print(m.name)

#print([m.name for m in poppy.motors])

# Access motor #3
m = poppy.m3


# What sensors do I have
print([s.name for s in poppy.sensors])

# The camera
img = poppy.camera.frame


# Make it move
# ------------

poppy.m3.compliant = False
poppy.m3.goal_position = 0

for _ in range(3):
    poppy.m3.goal_position = 30
    time.sleep(0.5)
    poppy.m3.goal_position = -30
    time.sleep(0.5)


# Again
for _ in range(3):
    poppy.m3.goto_position(30, 0.5, wait=True)
    poppy.m3.goto_position(-30, 0.5, wait=True)


# Use to motors
pos_1 = {'m1': -20, 'm3': 30}
pos_2 = {'m1': 20, 'm3': -30}

for _ in range(3):
    poppy.goto_position(pos_1, 0.5, wait=True)
    poppy.goto_position(pos_2, 0.5, wait=True)



