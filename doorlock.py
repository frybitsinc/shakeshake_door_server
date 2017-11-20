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

def unlock(right):
    led_num = 24
    sound_file = 'sound_button_right.mp3'
    msg = msg_right
    if not right:
        led_num = 23
        sound_file = 'sound_button_wrong.mp3'
        msg = msg_wrong
    print(msg)
    try:
        GPIO.output(led_num, True)
        os.system("omxplayer -o hdmi {}".format(sound_file))
        GPIO.output(led_num, False)
    except KeyboardInterrupt:
        GPIO.cleanup()

