import os
import threading
from gpiozero import AngularServo
from time import sleep

GPIO_TILT_SERVO = 12
GPIO_BASE_SERVO = 13
HIGHEST_PRIORITY = -20

def test_base():
    base_servo = AngularServo(GPIO_BASE_SERVO, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0020)

    base_servo.angle = 0
    sleep(2)
    base_servo.angle = 90
    sleep(2)
    base_servo.angle = 180
    sleep(2)

def test_tilt():
    tilt_servo = AngularServo(GPIO_TILT_SERVO, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0020)

    tilt_servo.angle = 0
    sleep(2)
    tilt_servo.angle = 90
    sleep(2)
    tilt_servo.angle = 180
    sleep(2)

niceValue = os.nice(HIGHEST_PRIORITY) 

# Run the servo tests
test_base()
test_tilt()

