import rtde_control

import time
import socket

from robotiq_gripper_control import RobotiqGripper
from rtde_control import RTDEControlInterface
from rtde_receive import RTDEReceiveInterface

ROBOT_IP = "192.168.12.52"  # change to your robotâ€™s IP
PORT = 63352            # Robotiq URCap port

NEUTRAL_POSE = [-0.368, 0.16622, 0.78466, 0.906, 2.629, -2.443]
NEUTRAL_POSE2 = [0.3, 0.6, 0.5, 3.18, 0.47, -0.148]
DROP_OFF_POSE = [0.710, -0.3876, -.145, 0, 3.14, 0.0]
RETURN_POSE = [0.710, -0.3876, 0.08622, 0, 3.14, 0.0]


GRIP_FLASK_POSE = [-1.04735, -0.57252, 0.46079, 1.571, 0.0, 0.0]
LIFTED_FLASK_POSE = [-1.04735, -0.57252, 0.46821, 1.571, 0.0, 0.0]
AWAY_FLASK_POSE = [-1.04735, -0.128, 0.46821, 1.571, 0.0, 0.0]
# WRONG_ON_TABLE_FLASK_POSE = [-0.61903, -0.41346, 0.22833, 0.0, 0.0, 0.0]
ON_TABLE_FLASK_POSE = [-0.52117, -0.43925, 0.14785, 1.571, 0.0, 0.0]



SPEED = 0.1        # m/s
ACCEL = 0.1        # m/s^2


def main():

    # Connect to robot
    rtde_c = RTDEControlInterface(ROBOT_IP)
    rtde_r = RTDEReceiveInterface(ROBOT_IP)
    gripper = RobotiqGripper(rtde_c)

    # Move to neutral/home

    print("Moving to neutral pose...")
    gripper.activate()
    gripper.open()
    rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
    rtde_c.moveL(LIFTED_FLASK_POSE, SPEED, ACCEL)
    rtde_c.moveL(GRIP_FLASK_POSE, SPEED, ACCEL)
    gripper.close()
    rtde_c.moveL(LIFTED_FLASK_POSE, SPEED, ACCEL)
    rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
    rtde_c.moveL(ON_TABLE_FLASK_POSE, SPEED, ACCEL)
    gripper.open()


    rtde_c.stopScript()
    rtde_c.disconnect()
    # print("Control session ended.")




main()

