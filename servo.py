import RPi.GPIO as GPIO
import time
servoPin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
pwm = GPIO.PWM(servoPin, 50)
pwm.start(7.5)
try:
    while True:
        doorlock = input("Activate doorlock...? (0 = Unlocked, 1 = Locked)")
        if doorlock == 0:
            pwm.start(7.5)
            pwm.ChangeDutyCycle(12.5)
            time.sleep(1)
            #pwm.stop()
        else:
            pwm.start(12.5)
            pwm.ChangeDutyCycle(7.5)
            time.sleep(1)
            #pwm.stop()
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
