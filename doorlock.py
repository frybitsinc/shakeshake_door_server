import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

msg_wrong = "Wrong authentication. Door Unlock failed. "
msg_right = "Door Unlocked!\nWelcome home!"

# red light
GPIO.setup(23,GPIO.OUT)
# green light
GPIO.setup(24, GPIO.OUT)
# servo motor
servo_pin = 18
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)

def unlock(right):
    # led
    led_num = 24
    # sound
    sound_file = 'sound_button_right.mp3'
    # motor
    pwm_srt = 7.5
    pwm_dc = 12.5
    # msg
    msg = msg_right
    if not right:
        # led
        led_num = 23
        # sound
        sound_file = 'sound_button_wrong.mp3'
        # msg
        msg = msg_wrong
    print(msg)
    try:
        # led on
        GPIO.output(led_num, True)
        # sound control
        os.system("omxplayer -o hdmi {}".format(sound_file))
        # led off
        GPIO.output(led_num, False)
        if right:
            # servo motor control
            pwm.start(pwm_srt)
            pwm.ChangeDutyCycle(pwm_dc+0.5)
            time.sleep(1)
            pwm.ChangeDutyCycle(pwm_dc-1)
            pwm.ChangeDutyCycle(pwm_srt)
            time.sleep(1)
            pwm.stop()
    except KeyboardInterrupt:
        GPIO.cleanup()

