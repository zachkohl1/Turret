from rpi_hardware_pwm import HardwarePWM
from time import sleep

GPIO12_PWM_CHNL = 0
GPIO13_PWM_CHNL = 1
CHIP = 2
PWM_FREQ_HZ = 50

tilt_servo = HardwarePWM(GPIO12_PWM_CHNL, hz=PWM_FREQ_HZ, chip=CHIP)
base_servo = HardwarePWM(GPIO13_PWM_CHNL, hz=PWM_FREQ_HZ, chip=CHIP)
tilt_servo.start(100)
base_servo.start(100)

def set_servo_angle(servo, angle):
    duty_cycle = angle / 18 + 2  # Convert angle to duty cycle
    servo.change_duty_cycle(duty_cycle)  # Set duty cycle

def test_base():
    for angle in [0, 90, 180]:
        print("Base angle: ", angle)
        set_servo_angle(base_servo, angle)
        sleep(2)

def test_tilt():
    for angle in [0, 90, 180]:
        print("Tilt angle: ", angle)
        set_servo_angle(tilt_servo, angle)
        sleep(2)

# Run the servo tests
test_base()
test_tilt()

# Clean up
tilt_servo.stop()
print("Tilt servo stopped")
sleep(.5)
base_servo.stop()
print("Base servo stopped")
