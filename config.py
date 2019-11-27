import RPi.GPIO as GPIO

DEBUG_MODE = True

########################### pin config GPIO.BOARD
GPIO_MODE           =       GPIO.BOARD

# RGB led
STATUS_LED_PIN      =       (11, 13, 15)           # R , G , B pins

MTR_R_PIN           =       (35, 37)            # (direction, PWM)
MTR_L_PIN           =       (36, 38)

US_TRIG_PIN         =       31                  # ultrasonic
US_ECHO_PIN         =       32


########################### const
# ports
CTRL_PORT           =       "5555"
MEDIA_PORT          =       "4456"
AUTO_PORT           =       "5453"

# tolerances
DIST_TOLERANCE      =       1                  # in meters
ANGLE_TOLERANCE     =       5                  # in degrees
US_BLOCKED_THRESH   =       100                # in cm

# delays
TURN_DELAY          =       3.75               # in seconds
STEP_DELAY          =       1.5                # in seconds

# motors
MTR_PWM_FREQ        =       10000              # user manual says 20KHz is max
MTR_FRWRD_SPD       =       80                 # motor forward speed [PWM duty cycle 0~100]
MTR_BKWRD_SPD       =       80                 # motor backward speed [PWM duty cycle 0~100]
MTR_DIR_FORWARD     =       1
MTR_DIR_BACKWARD    =       0
MTR_RL_DIFF         =       17                  # added to left side

# RGB led colors
FREE_STATUS_COLOR   =       (0, 1, 0)           # green color to indicate car is free and waiting for tasks
BUSY_STATUS_COLOR   =       (1, 1, 0)           # Yellow color to indicate car is busy
DONE_STATUS_COLOR   =       (0, 0, 1)           # Blue color to indicate success
ERR_STATUS_COLOR    =       (1, 0, 0)           # Red color to indicate error

# media commands
MEDIA_CMD_PLAY      =       b'play'
MEDIA_CMD_STOP      =       b'stop'
MEDIA_CMD_TERMINATE =       b'terminate'

# control commands
TASK_CMD_FRWRD      =       b'f'
TASK_CMD_BKWRD      =       b'b'
TASK_CMD_TRN_R      =       b'r'
TASK_CMD_TRN_L      =       b'l'
TASK_CMD_STOP       =       b's'
TASK_CMD_AUTO       =       b'a'
