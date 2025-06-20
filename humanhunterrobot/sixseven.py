# RoboMaster S1 Auto-Targeting System
# Run this in the RoboMaster app

pid_x = rm_ctrl.PIDCtrl()
pid_y = rm_ctrl.PIDCtrl()
pid_Pitch = rm_ctrl.PIDCtrl()
pid_Yaw = rm_ctrl.PIDCtrl()

variable_X = 0
variable_Y = 0
variable_Post = 0.01  # Accu
#cy threshold - how close to center before firing
list_MarkerList = RmList()

def start():
    #global variable_X, f modules)
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    
    # HUMAN HUNTER MODE - Detects and targets people!
    vision_ctrl.enable_detection( rm_define.vision_detection_people)
    
    # Set PID parameters (Proportional, Integral, Derivative)
    # Higher P = more aggressive tracking, D = dampening to reduce oscillation
    pid_Yaw.set_ctrl_params(115, 0, 5)      # Controls left/right gimbal movement
    pid_Pitch.set_ctrl_params(85, 0, 3)     # Controls up/down gimbal movement
    
    print("🤖 HUMAN HUNTER MODE ACTIVATED! 🎯")
    print("Looking for humans to target...")
    
    while True:
        if vision_ctrl.check_condition(rm_define.cond_recognized_people):
            print("I found someone!!!")
        else:
            print("I DIDNT find someone")
        time.sleep(1)

# Start the auto-targeting system
start()
