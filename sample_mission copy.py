from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from base_robot_2024_submerged import *
from utils import *

# Add good comments, such as what the mission is supposed to do,
# how to align the robot in home, any initial starting instructions,
# such as how it should be loaded with anything, arm positions, etc.


# When we run this program from the master program, we will call this
# "Run(br)" method.
def Run(br: BaseRobot):
    # Your mission code goes here, step-by-step
    # It MUST be indented just like the lines below
    # br.GyroDrive(distance=680, speed=500)
    # br.WaitForMillis(millis=500)  # half second
    # br.GyroTurn(65)  # turn to the right 85 degrees
    # br.GyroDrive(distance=300)  # use the default speed
    # deg = 1000
    # br.leftAttachmentMotor.control.limits(acceleration=20000)
    # br.leftAttachmentMotor.run_angle(1000, deg)  # speed 200, 180 degrees
    # br.leftAttachmentMotor.run_angle(990, deg)  # speed 200, 180 degrees
    # br.leftAttachmentMotor.run_angle(1000, deg)  # speed 200, 180 degrees
    # br.leftAttachmentMotor.run_angle(990, deg)  # speed 200, 180 degrees
    # br.rightAttachmentMotor.run_angle(200, 180)  # speed 200, 180 degrees
    # br.TurnInPlace(angle=360, then=Stop.COAST_SMART)
    # br.WaitForButton(button=Button.LEFT)
    # br.TurnInPlace(angle=360, then=Stop.COAST_SMART)
    # br.WaitForButton(button=Button.LEFT)
    # br.moveLeftAttachmentMotorForDegrees(degrees=1000, speedPct=100)
    br.leftAttachmentMotor.run_angle(speed=500, rotation_angle=10000)
    print(RescaleConvertFarToCel(32))

# robot.settings(straight_speed=977, straight_acceleration=500)
# robot.straight(2100)


# If running this program directly (not from the master program), this is
# how we know it is running directly. In which case, this method will
# create a BaseRobot and run the Run(br) method above.
# In other words, keep these three lines at the bottom of your code and
# everything will be fine.
if __name__ == "__main__":
    br = BaseRobot()
    Run(br)