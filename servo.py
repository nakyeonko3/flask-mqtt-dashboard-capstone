import RPi.GPIO as GPIO
import time
from dynamikontrol import Timer
# import multiprocessing

auto_motor = Timer()

def servo_motor_control():
    servo_pin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)
    pwm = GPIO.PWM(servo_pin, 50)  # 50Hz (서보모터 PWM 동작을 위한 주파수)
    pwm.start(3.0) #서보의 0도 위치(0.6ms)이동:값 3.0은 pwm주기인 20ms의 3%를 의미하므로,0.6ms됨.
    pwm.ChangeDutyCycle(3.0)   # 서보모터를 0도로 회전(이동)
    time.sleep(1.0)            # 서보 모터가 이동할 시간을 줌
    pwm.ChangeDutyCycle(9.5)  # 서보 모터를 135도로 회전(이동)
    time.sleep(1.0)            # 서보 모터가 이동할 시간을 줌
    pwm.ChangeDutyCycle(0.0)
    pwm.stop()
    GPIO.cleanup()

def servo_motor_auto_mode_on():
    auto_motor.callback_after(func=servo_motor_control,interval=20)

# pro = multiprocessing.Process(target=servo_motor_auto_mode)

count = 0

if __name__ == "__main__":
    # servo_motor_control()
    servo_motor_auto_mode_on()


