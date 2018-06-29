import time

from pypot.creatures import PoppyHumanoid
from pypot.vrep import from_vrep

poppy = PoppyHumanoid(simulator='vrep')

poppy.abs_y.goal_position = 40
poppy.r_shoulder_y.goal_position = -90
poppy.l_shoulder_y.goal_position = -90
time.sleep(0.6)

poppy.r_knee_y.goal_position = 90
poppy.l_knee_y.goal_position = 90

time.sleep(0.3)
poppy.r_knee_y.goal_position = 0
poppy.l_knee_y.goal_position = 0


time.sleep(0.6)

poppy.abs_y.goal_position = -0
