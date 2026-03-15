import rtde_control


import time
import socket




from robotiq_gripper_control import RobotiqGripper
from rtde_control import RTDEControlInterface
from rtde_receive import RTDEReceiveInterface
from microscope import save_image


ROBOT_IP = "192.168.12.52"  # change to your robotâ€™s IP
PORT = 63352            # Robotiq URCap port


# NEUTRAL_POSE = [-0.368, 0.16622, 0.78466, 0.906, 2.629, -2.443]
# NEUTRAL_POSE2 = [0.3, 0.6, 0.5, 3.18, 0.47, -0.148]
# DROP_OFF_POSE = [0.710, -0.3876, -.145, 0, 3.14, 0.0]
# RETURN_POSE = [0.710, -0.3876, 0.08622, 0, 3.14, 0.0]




HOME = [-0.99853, 0.04105, -0.11891, 1.495, -0.221, 0.038]


# --- FRIDGE & MEDIA BOTTLE POSES ---
FRIDGE_HANDLE = [-0.71027, -0.32422, -0.33378, 0.144, -2.098, 2.062]
OPEN_FRIDGE = [-0.95014, -0.32422, -0.33378, 0.144, -2.098, 2.062]
OPEN_FRIDGEINTERMEDIATE = [-0.95014, -0.128, -0.33378, 0.144, -2.098, 2.062]
FRIDGE_HOME = [-0.71027, 0.077, -0.33378, 0.144, -2.098, 2.062]


# FRIDGE
INTERMEDIATE_TOGETBOTTLE = [-0.76926, -0.128, -0.15108, 0.0, 1.911, -2.493]
GET_MEDIABOTTLE = [-0.76926, -0.44112, -0.15108, 0.0, 1.911, -2.493]
LIFT_MEDIABOTTLE = [-0.76926, -0.44112, -0.13009, 0.0, 1.911, -2.493]
BRINGOUT_MEDIABOTTLE = [-0.76926, -0.11173, -0.13009, 0.0, 1.911, -2.493]
BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE = [
   -0.76926, -0.11173, 0.20159, 0.0, 1.911, -2.493]
BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE = [
   -0.69509, -0.42933, 0.20159, 0.0, 1.911, -2.493]
ONTABLE_MEDIABOTTLE = [-0.69509, -0.42933, 0.15159, 0.065, 2.256, -2.306]


MOVE_UP_FROM_TABLE = [-0.69509, -0.42933, 0.35130, 0.065, 2.256, -2.306]
REGRIP_POSITION_Z = [-0.69507, -0.42932, 0.35130, 0.000, 3.141, -0.013]
REGRIP_MEDIABOTTLE_Z = [-0.6959, -0.42932, 0.13045, 0.000, 3.141, -0.013]
REGRIP_ROTATING_MEDIABOTTLE = [-0.6959, -0.42932, 0.288, 0, 2.153, -2.287]


REGRIP_PLACE_ON_TABLE_INTERMEDIATE = [-0.507, -
                                     0.49413, 0.3573, 0, 2.153, -2.287]
REGRIP_PLACE_ON_TABLE = [-0.6959, -0.42932, 0.19468, 0, 2.153, -2.287]




# --- MICROSCOPE ---
MICROSCOPE_HOME = [0.19008, -0.5503, 0.69348, 0.137, -2.085, 2.484]
MICROSCOPE_APPROACH1 = [0.76932, 0.14060, 0.63912, 1.209, 1.209, 1.209]
MICROSCOPE_APPROACH2 = [0.76932, 0.14060, 0.00893, 1.209, 1.209, 1.209]
GRIP_FLASK_FROM_TABLE_MICROSCOPE = [
   0.81367, 0.14061, 0.00665, 1.209, 1.209, 1.209]
MICROSCOPE_APPROACH3 = [0.78085, 0.43842, 0.08476, 1.209, 1.209, 1.209]
PLACE_ON_MICROSCOPE = [0.84312, 0.44126, 0.0065, 1.216, 1.238, 1.215]
OUT_OF_MICROSCOPE = [0.76689, 0.44126, 0.0065, 1.216, 1.238, 1.215]




INTERMEIDATE1_MICROSCOPE_TO_FRIDGE = [-0.37291, -
                                     0.5447, 0.69348, 0.137, -2.085, 2.484]
INTERMEIDATE2_MICROSCOPE_TO_FRIDGE = [-0.37291, -
                                     0.17308, 0.69348, 0.137, -2.085, 2.484]


# INCUBABOR
INCUBATOR_HOME = [-0.84093, -0.30589, 0.76812, 0.103, -2.168, 2.249]
# INCUBATOR_HANDLE = [-0.84093, -0.44288, 0.76812, 0.103, -2.168, 2.249]
# INCUBATOR_OPEN = [0.19008, -0.5503, 0.69348, 0.137, -2.085, 2.484]
# INCUBATOR_OPEN_INTERMEIDATE = [0.19008, -0.5503, 0.69348, 0.137, -2.085, 2.484]
# INCUBATOR_INTERMEDIATE_TO_FLASK = [-1.04893, -0.44159, 0.46898, 0.103, -2.168, 2.249]


# INCUBATOR_GRIP_FLAKSK_FROM_INCUBATOR = [-1.08086, -0.31423, 0.49598, 0.014, 2.146, -2.855]
# INCUBATOR_GRIP_FLAKSK_LIFT_UP = [-1.08086, -0.31423, 0.49598, 0.014, 2.146, -2.855]
GRIP_FLASK_POSE = [-1.04735, -0.57252, 0.46834, 1.571, 0.0, 0.0]
# LIFTED_FLASK_POSE = [-1.04735, -0.57252, 0.49834, 1.571, 0.0, 0.0]
# OUT_FLASK_POSE = [-1.04735, -0.53252, 0.49834, 1.571, 0.0, 0.0]
AWAY_FLASK_POSE = [-1.04735, -0.128, 0.46821, 1.571, 0.0, 0.0]
INCUBATOR_INTERMEDIATE_MICROSCOPE = [-0.63532, -
                                    0.128, 0.71624, 1.571, 0.0, 0.0]




SPEED = 0.9      # m/s
ACCEL = 0.9       # m/s^2




def main():


   # Connect to robot
   rtde_c = RTDEControlInterface(ROBOT_IP)
   rtde_r = RTDEReceiveInterface(ROBOT_IP)
   gripper = RobotiqGripper(rtde_c)


   # Move to neutral/home
   print("Moving to neutral pose...")
   # rtde_c.moveL(HOME, SPEED, ACCEL)


   gripper.open()


   # ==========================================
   # 2. GET MEDIA BOTTLE FROM FRIDGE and Place on Table
   # ==========================================
   print("Retrieving media bottle from fridge...")


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


# --
   # rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE2_MEDIABOTTLE, SPEED, ACCEL)
   # rtde_c.moveL(MOVE_UP_FROM_TABLE, SPEED, ACCEL)
   # rtde_c.moveL(REGRIP_POSITION_Z, SPEED, ACCEL)
   # rtde_c.moveL(REGRIP_MEDIABOTTLE_Z, SPEED, ACCEL)
   # gripper.close()
   # rtde_c.moveL(REGRIP_ROTATING_MEDIABOTTLE, SPEED, ACCEL)
   # rtde_c.moveL(REGRIP_PLACE_ON_TABLE_INTERMEDIATE, SPEED, ACCEL)
   # rtde_c.moveL(REGRIP_PLACE_ON_TABLE, SPEED, ACCEL)
   # gripper.open()


   # ==========================================
   # 3. Go Back to Fridge and Close Door
   # ==========================================
   rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(OPEN_FRIDGEINTERMEDIATE, SPEED, ACCEL)
   rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(FRIDGE_HOME, SPEED, ACCEL)


   # ==========================================
   # 4. Open Incubator
   # ==========================================
   # rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
   # rtde_c.moveL(GRIP_FLASK_POSE, SPEED, ACCEL)
   # gripper.close()
   # rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
   # rtde_c.moveL(INCUBATOR_INTERMEDIATE_MICROSCOPE, SPEED, ACCEL)
   # rtde_c.moveL(MICROSCOPE_HOME, SPEED, ACCEL)


   # rtde_c.moveL(MICROSCOPE_APPROACH1, SPEED, ACCEL)
   # rtde_c.moveL(MICROSCOPE_APPROACH2, SPEED, ACCEL)
   # rtde_c.moveL(GRIP_FLASK_FROM_TABLE_MICROSCOPE, SPEED, ACCEL)
   # gripper.open()
   # ==========================================
   # 2. GO HOME POSITION FROM MICROSCOPE TO FRIDGE
   # ==========================================
   # rtde_c.moveL(INTERMEIDATE2_MICROSCOPE_TO_FRIDGE, SPEED, ACCEL)
   # rtde_c.moveL(INTERMEIDATE1_MICROSCOPE_TO_FRIDGE, SPEED, ACCEL)


   # ==========================================
   # 1. MICROSCOPE
   # ==========================================
   print("MICROSCOPE HOME POSITION...")
   rtde_c.moveL(MICROSCOPE_HOME, SPEED, ACCEL)
   rtde_c.moveL(MICROSCOPE_APPROACH1, SPEED, ACCEL)
   rtde_c.moveL(MICROSCOPE_APPROACH2, SPEED, ACCEL)
   rtde_c.moveL(GRIP_FLASK_FROM_TABLE_MICROSCOPE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(MICROSCOPE_APPROACH3, SPEED, ACCEL)
   rtde_c.moveL(PLACE_ON_MICROSCOPE, SPEED, ACCEL)
   gripper.open()
   save_image()
   rtde_c.moveL(OUT_OF_MICROSCOPE, SPEED, ACCEL)
   rtde_c.moveL(MICROSCOPE_HOME, SPEED, ACCEL)


   # ==========================================
   # 2. GO HOME POSITION FROM MICROSCOPE TO FRIDGE
   # ==========================================
   rtde_c.moveL(INTERMEIDATE1_MICROSCOPE_TO_FRIDGE, SPEED, ACCEL)
   rtde_c.moveL(INTERMEIDATE2_MICROSCOPE_TO_FRIDGE, SPEED, ACCEL)


   # ==========================================
   # 4. Go Back to Table and Move Bottle Back to Fridge
   # ==========================================
   rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(OPEN_FRIDGEINTERMEDIATE, SPEED, ACCEL)
   rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(ONTABLE_MEDIABOTTLE, SPEED, ACCEL)
   gripper.close()


   rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(INTERMEDIATE_TOGETBOTTLE, SPEED, ACCEL)
   rtde_c.moveL(GET_MEDIABOTTLE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(LIFT_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(BRINGOUT_MEDIABOTTLE, SPEED, ACCEL)
   rtde_c.moveL(OPEN_FRIDGE, SPEED, ACCEL)
   gripper.close()
   rtde_c.moveL(FRIDGE_HANDLE, SPEED, ACCEL)
   gripper.open()
   rtde_c.moveL(FRIDGE_HOME, SPEED, ACCEL)




# ...
   # ==========================================
   # 3. Take out the flask from incubator and place on table
   # ==========================================
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


# ==========================================
# 5. RETURN FLASK TO INCUBATOR
# ==========================================
   # print("Returning flask to incubator...")
   # rtde_c.moveL(INCUBATOR_HANDLE, SPEED, ACCEL)
   # gripper.close()
   # time.sleep(0.5)
   # rtde_c.moveL(OPEN_INCUBATOR, SPEED, ACCEL)
   # gripper.open()
   # time.sleep(0.5)


   # rtde_c.moveL(ON_TABLE_FLASK_POSE, SPEED, ACCEL)
   # gripper.close()
   # time.sleep(0.5)


   # rtde_c.moveL(BRING_OUT_TO_TABLE_INTERMEDIATE_FLASK, SPEED, ACCEL)
   # rtde_c.moveL(AWAY_FLASK_POSE, SPEED, ACCEL)
   # rtde_c.moveL(INTERMEDIATE_TOGETFLASK, SPEED, ACCEL)
   # rtde_c.moveL(GRIP_FLASK_POSE, SPEED, ACCEL)
   # gripper.open()
   # time.sleep(0.5)


   # rtde_c.moveL(OPEN_INCUBATORINTERMEDIATE, SPEED, ACCEL)
   # rtde_c.moveL(OPEN_INCUBATOR, SPEED, ACCEL)
   # gripper.close()
   # time.sleep(0.5)
   # rtde_c.moveL(INCUBATOR_HANDLE, SPEED, ACCEL)
   # gripper.open()
   # time.sleep(0.5)


   # # Return to home and disconnect
   # print("Workflow complete. Returning home.")
   # rtde_c.moveL(HOME, SPEED, ACCEL)
main()


# --- INCUBATOR & FLASK POSES ---
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



