import RPi.GPIO as GPIO
import time
servoPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7.5)
try:
    while True:
        pwm.ChangeDutyCycle(12.5)
        time.sleep(2)
        pwm.ChangeDutyCycle(7.5)
        time.sleep(2)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
