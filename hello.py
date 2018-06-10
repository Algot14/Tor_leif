import math
import time
import pypot

from pypot.creatures import PoppyHumanoid
from pylab import *

pypot.vrep.close_all_connections()

poppy = PoppyHumanoid(simulator='vrep')
#poppy.reset_simulation()


print('Motors:')
print(poppy.motors)

print('\n\nMotor positions:')
print([m.present_position for m in poppy.motors])

print('\n\nMotor aliases:')
print(poppy.alias)

print('\n\nRight leg motors:')
print({m.name: m.present_position for m in poppy.r_leg})

print('\n\nSet head position')
poppy.head_z.goal_position = 90.

print('Waiting 5 seconds, switch to the simulator')
for _ in range(0,5):
  time.sleep(1)
  print('.')

print('\n\nSet position for left arms')
for m in poppy.l_arm:
    m.goal_position = 30.
print([m for m in poppy.l_arm])

print('Reset the simulation and move the head')
poppy.head_z.goto_position(-45, 2)

poppy.head_z.goto_position(45, 2, wait=False)
poppy.head_y.goto_position(-30, 2, wait=True)
poppy.head_z.goto_position(0, 2, wait=True)
poppy.head_y.goto_position(20, 1, wait=True)

print(poppy.head_y.goto_behavior)
poppy.head_y.goto_behavior = 'minjerk'

amp = 30 # in degrees
freq = 0.5 # in Hz
t0 = time.time()
while True:
    t = time.time()
    
    # run for 10s
    if t - t0 > 10:
        break

    poppy.head_z.goal_position = amp * math.sin(2 * 3.14 * freq * t)
    
    time.sleep(0.04)


#
# Move the head and record the position

current, goal = [], []
t0 = time.time()
while True:
    t = time.time()
    
    # run for 5s
    if t - t0 > 5:
        break

    poppy.head_z.goal_position = amp * math.sin(2 * 3.14 * freq * t)

    current.append(poppy.head_z.present_position)
    goal.append(poppy.head_z.goal_position)
    
    time.sleep(0.04)


t = linspace(0, 5, len(current))
plot(t, goal)
plot(t, current)

legend(('goal', 'current'))
plot.show()

