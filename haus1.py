from myservo import myServo
import time
from machine import Pin, PWM

led1 = 4
led2 = 5
led_pin1 = Pin(led1, Pin.OUT)
led_pin2 = Pin(led2, Pin.OUT)

servo = myServo(9) # Pinninn sem servo-inn er tengdur við
teljari = 0
check = True
while True:
    servo.myServoWriteAngle(teljari)
    time.sleep(1)
    led_pin2.value(1)
    led_pin1.value(1)
    teljari = teljari + 83
    servo.myServoWriteAngle(teljari)
    time.sleep(1)
    led_pin2.value(0)
    led_pin1.value(0)
    teljari = 0
