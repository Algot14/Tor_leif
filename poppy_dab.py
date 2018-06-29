import time

from pypot.creatures import PoppyHumanoid
from pypot.vrep import from_vrep



poppy.r_shoulder_x.goal_position = -115
poppy.l_shoulder_y.goal_position = -110
poppy.l_elbow_y.goal_position = -90
poppy.l_arm_z.goal_position = -80

time.sleep(2)

poppy.r_shoulder_x.goal_position = 0.1
poppy.l_shoulder_y.goal_position = 0.1
poppy.l_elbow_y.goal_position = 0.1
poppy.l_arm_z.goal_position = 0.1

time.sleep(2)

poppy.l_shoulder_x.goal_position = 115
poppy.r_shoulder_y.goal_position = -110
poppy.r_elbow_y.goal_position = -90
poppy.r_arm_z.goal_position = 80

time.sleep(2)

poppy.l_hip_y.goal_position = -30
poppy.l_knee_y.goal_position = 30
