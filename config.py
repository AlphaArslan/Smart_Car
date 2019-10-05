import RPi.GPIO as GPIO


########################### pin config GPIO.BOARD
GPIO_MODE           =       GPIO.BOARD
# RGB led
STATUS_LED_PIN      =       (3, 5, 7)           # R , G , B pins



########################### const
# ports
TASK_PORT           =       "5555"
MEDIA_PORT          =       "4456"

# motors
MTR_PWM_FREQ        =       10000              # user manual says 20KHz is max
MTR_FRWRD_SPD       =       80                 # motor forward speed [PWM duty cycle 0~100]
MTR_BKWRD_SPD       =       80                 # motor backward speed [PWM duty cycle 0~100]
MTR_DIR_FORWARD     =       1
MTR_DIR_BACKWARD    =       0
MTR_R_PIN           =       (11, 12)           # (direction, PWM)
MTR_L_PIN           =       (13, 15)

# RGB led colors
FREE_STATUS_COLOR   =       (0, 1, 0)           # green color to indicate car is free and waiting for tasks
BUSY_STATUS_COLOR   =       (1, 1, 0)           # Yellow color to indicate car is busy
DONE_STATUS_COLOR   =       (0, 0, 1)           # Blue color to indicate success
ERR_STATUS_COLOR    =       (1, 0, 0)           # Red color to indicate error

# media commands
MEDIA_CMD_PLAY      =       b'play'
MEDIA_CMD_STOP      =       b'stop'
MEDIA_CMD_TERMINATE =       b'terminate'
