import RPi.GPIO as GPIO


########################### pin config GPIO.BOARD
GPIO_MODE           =       GPIO.BOARD
# RGB led
STATUS_LED_PIN      =       (3, 5, 7)           # R , G , B pins



########################### const
# ports
TASK_PORT           =       "tcp://localhost:5555"

# motors
MTR_FRWRD_SPD       =       200                 # motor forward speed [PWM]
MTR_BKWRD_SPD       =       200                 # motor backward speed [PWM]

# RGB led colors
FREE_STATUS_COLOR   =       (0, 1, 0)           # green color to indicate car is free and waiting for tasks
BUSY_STATUS_COLOR   =       (1, 1, 0)           # Yellow color to indicate car is busy
DONE_STATUS_COLOR   =       (0, 0, 1)           # Blue color to indicate success
ERR_STATUS_COLOR    =       (1, 0, 0)           # Red color to indicate error
