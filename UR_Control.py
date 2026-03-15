import rtde_control


import time
import socket


from robotiq_gripper_control import RobotiqGripper
from rtde_control import RTDEControlInterface
from rtde_receive import RTDEReceiveInterface
# from microscope import save_image

# save_image()

ROBOT_IP = "192.168.12.52"  # change to your robotâ€™s IP
PORT = 63352            # Robotiq URCap port

# NEUTRAL_POSE = [-0.368, 0.16622, 0.78466, 0.906, 2.629, -2.443]
# NEUTRAL_POSE2 = [0.3, 0.6, 0.5, 3.18, 0.47, -0.148]
# DROP_OFF_POSE = [0.710, -0.3876, -.145, 0, 3.14, 0.0]
# RETURN_POSE = [0.710, -0.3876, 0.08622, 0, 3.14, 0.0]


HOME=[-0.73126, -0.15916, -0.43193, 0.0, 2.147, -2.245]

FRIDGE_HANDLE = [-0.71027, -0.32422, -0.33378, 0.144, -2.098, 2.062]
OPEN_FRIDGE = [-0.95014, -0.32422, -0.33378, 0.144, -2.098, 2.062]
OPEN_FRIDGEINTERMEDIATE = [-0.95014, -0.128, -0.33378, 0.144, -2.098, 2.062]


# INTERMEDIATE_TOGETBOTTLE = [-0.77819, -0.128, -0.15109, 0.067, 1.946, -2.538]
# # GET_MEDIABOTTLE = [-0.77819, -0.43752, -0.15109, 0.067, 1.946, -2.538]
# GET_MEDIABOTTLE = [-0.76926, -0.44112, -0.15108, 0.0, 1.911, -2.493]
# LIFT_MEDIABOTTLE = [-0.77819, -0.43752, -0.13009, 0.067, 1.946, -2.538]
# BRINGOUT_MEDIABOTTLE = [-0.77819, -0.11173, -0.13009, 0.067, 1.946, -2.538]
# BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE = [-0.77819, -0.11173, 0.17159, 0.067, 1.946, -2.538]
# ONTABLE_MEDIABOTTLE = [-0.69509, -0.42933, 0.15159, 0.065, 2.256, -2.306]

# FRIDGE
INTERMEDIATE_TOGETBOTTLE = [-0.76926, -0.128, -0.15108, 0.0, 1.911, -2.493]
GET_MEDIABOTTLE = [-0.76926, -0.44112, -0.15108, 0.0, 1.911, -2.493]
LIFT_MEDIABOTTLE = [-0.76926, -0.44112, -0.13009, 0.0, 1.911, -2.493]
BRINGOUT_MEDIABOTTLE = [-0.76926, -0.11173, -0.13009, 0.0, 1.911, -2.493]
BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE = [-0.76926, -0.11173, 0.20159, 0.0, 1.911, -2.493]
BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE = [-0.69509, -0.42933, 0.20159, 0.0, 1.911, -2.493]
ONTABLE_MEDIABOTTLE = [-0.69509, -0.42933, 0.15159, 0.065, 2.256, -2.306]

MOVE_UP_FROM_TABLE = [-0.69509, -0.42933, 0.35130, 0.065, 2.256, -2.306]
REGRIP_POSITION_Z = [-0.69507, -0.42932, 0.35130, 0.000, 3.141, -0.013]
REGRIP_MEDIABOTTLE_Z = [-0.6959, -0.42932, 0.13045, 0.000, 3.141, -0.013]
REGRIP_ROTATING_MEDIABOTTLE = [-0.6959, -0.42932, 0.288, 0, 2.153 , -2.287]

REGRIP_PLACE_ON_TABLE_INTERMEDIATE = [-0.507, -0.49413, 0.3573, 0, 2.153 , -2.287]
REGRIP_PLACE_ON_TABLE = [-0.6959, -0.42932, 0.19468, 0, 2.153 , -2.287]


# INCUBATOR
# LIFTED_FLASK_POSE = [-1.04735, -0.57252, 0.46821, 1.571, 0.0, 0.0]
# AWAY_FLASK_POSE = [-1.04735, -0.128, 0.46821, 1.571, 0.0, 0.0]
# INCUBATOR_HANDLE = []
# OPEN_INCUBATORINTERMEDIATE = []
# OPEN_INCUBATOR = []
# INTERMEDIATE_TOGETFLASK = []
# GRIP_FLASK_POSE = [-1.04735, -0.57252, 0.46079, 1.571, 0.0, 0.0]
# LIFTED_FLASK_POSE = [-1.04735, -0.57252, 0.46821, 1.571, 0.0, 0.0]
# AWAY_FLASK_POSE = [-1.04735, -0.128, 0.46821, 1.571, 0.0, 0.0]
# BRING_OUT_TO_TABLE_INTERMEDIATE_FLASK = []
# BRING_OUT_TO_TABLE_INTERMEDIATE2_FLASK = []
# ON_TABLE_FLASK_POSE = [-0.52117, -0.43925, 0.14785, 1.571, 0.0, 0.0]

# Open Flask




SPEED = 0.3        # m/s
ACCEL = 0.3       # m/s^2




def main():


   # Connect to robot
   rtde_c = RTDEControlInterface(ROBOT_IP)
   rtde_r = RTDEReceiveInterface(ROBOT_IP)
   gripper = RobotiqGripper(rtde_c)


   # Move to neutral/home

#    gripper.open()

   print("Moving to neutral pose...")
#    gripper.open()
   rtde_c.moveL(HOME, SPEED, ACCEL)

   # Take out media from fridge and place on table > move bottle to upward
   rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(OPEN_FRIDGEINTERMEDIATE, SPEED, ACCEL)
   rtde_c.moveL(INTERMEDIATE_TOGETBOTTLE, SPEED, ACCEL)
   rtde_c.moveL(GET_MEDIABOTTLE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(LIFT_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(BRINGOUT_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(ONTABLE_MEDIABOTTLE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(MOVE_UP_FROM_TABLE, SPEED, ACCEL)
   rtde_c.moveL(REGRIP_POSITION_Z, SPEED, ACCEL)
   rtde_c.moveL(REGRIP_MEDIABOTTLE_Z, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(REGRIP_ROTATING_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(REGRIP_PLACE_ON_TABLE_INTERMEDIATE, SPEED, ACCEL)
   rtde_c.moveL(REGRIP_PLACE_ON_TABLE, SPEED, ACCEL)
   gripper.open()



#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE, SPEED, ACCEL)
#    rtde_c.moveL(BRINGOUT_MEDIABOTTLE, SPEED, ACCEL)
#    rtde_c.moveL(OPEN_FRIDGEINTERMEDIATE, SPEED, ACCEL)
#    rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)
#    gripper.open()
#    rtde_c.moveL(HOME, SPEED, ACCEL)

   #Up Position the media bottle
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)

#    rtde_c.moveL(OPENLID_MEDIABOTTLE, SPEED, ACCEL)
#    rtde_c.moveL(LID_ON_THE_TABLE_MEDIABOTTLE, SPEED, ACCEL)
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)

#    #Pour flaks 
#    rtde_c.moveL(HOLD_FLASK_FROM_TOP, SPEED, ACCEL)
#    #INCREASE Z XIS
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)
#    #ROTATION UPWARD
   #GO TO CAP STATION 
   #OPEN CAP
   #COMEBACK TO    #ROTATION UPWARD
   #POUR
   # RETURN BACK TO #ROTATION UPWARD
   #DEREASE Y  AND MOVE DOWN 
   #GO BACK TO LID POSITION AND CAP AND TURN 
   # REPOSTION CELL FLASK 





   # Take out the flask from incubator and place on table
#    rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
#    rtde_c.moveL(INCUBATOR_HANDLE, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(OPEN_INCUBATOR, SPEED, ACCEL)
#    gripper.open()
#    rtde_c.moveL(OPEN_INCUBATORINTERMEDIATE, SPEED, ACCEL)
#    rtde_c.moveL(INTERMEDIATE_TOGETFLASK, SPEED, ACCEL)
#    rtde_c.moveL(GRIP_FLASK_POSE, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(LIFTED_FLASK_POSE, SPEED, ACCEL)
#    rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_FLASK, SPEED, ACCEL)
#    rtde_c.moveL(ON_TABLE_FLASK_POSE, SPEED, ACCEL)
#    gripper.open()
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_FLASK, SPEED, ACCEL)
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_FLASK, SPEED, ACCEL)
#    rtde_c.moveL(OPEN_INCUBATOR, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(INCUBATOR_HANDLE, SPEED, ACCEL)
#    gripper.open()

#    rtde_c.moveL(HOME, SPEED, ACCEL)

#    rtde_c.moveL(INCUBATOR_HANDLE, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(OPEN_INCUBATOR, SPEED, ACCEL)
#    gripper.open()

#    rtde_c.moveL(ON_TABLE_FLASK_POSE, SPEED, ACCEL)
#    rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_FLASK, SPEED, ACCEL)
#    rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
#    rtde_c.moveL(INTERMEDIATE_TOGETFLASK, SPEED, ACCEL)
#    rtde_c.moveL(OPEN_INCUBATORINTERMEDIATE, SPEED, ACCEL)
#    rtde_c.moveL(GRIP_FLASK_POSE, SPEED, ACCEL)



#    rtde_c.move(OPEN_FRIDGEINTERMEDIATE, SPEED, ACCEL)
#    rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
#    gripper.close()
#    rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)


#    rtde_c.stopScript()
#    rtde_c.disconnect()
   # print("Control session ended.")




main()