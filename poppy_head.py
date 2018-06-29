import time
import math

from pypot.creatures import PoppyHumanoid
from pypot.vrep import from_vrep

amp = 30 # in degrees
freq = 0.5 # in Hz

t0 = time.time()

poppy = PoppyHumanoid(simulator='vrep')

while True:
    t = time.time()

    # run for 10s
    if t - t0 > 10:
        break

    poppy.head_z.goal_position = amp * math.sin(2 * 3.14 * freq * t)

    time.sleep(0.04)
