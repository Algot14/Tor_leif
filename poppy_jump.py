import time

from pypot.creatures import PoppyHumanoid
from pypot.vrep import from_vrep

poppy = PoppyHumanoid(simulator='vrep')

poppy.abs_y.goal_position = 40
poppy.r_shoulder_y.goal_position = -90
poppy.l_shoulder_y.goal_position = -90
time.sleep(1)

poppy.r_knee_y.goal_position = 90
poppy.l_knee_y.goal_position = 90

time.sleep(1)
poppy.r_knee_y.goal_position = 0
poppy.l_knee_y.goal_position = 0

time.sleep(0.04)

poppy.l_hip_x.goal_position = 20
poppy.r_hip_x.goal_position = -20

time.sleep(1)

poppy.l_elbow_y.goal_position = -130
poppy.r_elbow_y.goal_position = -130
poppy.r_shoulder_y.goal_position = -10
poppy.l_shoulder_y.goal_position = -10

time.sleep(0.6)

poppy.l_elbow_y.goal_position = 0.1
poppy.r_elbow_y.goal_position = 0.1
poppy.r_shoulder_y.goal_position = -90
poppy.l_shoulder_y.goal_position = -90

time.sleep(1)
