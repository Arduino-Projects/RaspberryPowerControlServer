import RPi.GPIO as GPIO

global SWITCH_STATUS

def toggle():
    # The script as below using BCM GPIO 00..nn numbers
    GPIO.setmode(GPIO.BCM)

    # Set relay pins as output
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    global SWITCH_STATUS

    if (SWITCH_STATUS == 0):
     print "Switch status ON"
     # Turn all relays ON
     GPIO.output(18, GPIO.HIGH)
     GPIO.output(23, GPIO.HIGH)
     GPIO.output(24, GPIO.HIGH)
     GPIO.output(25, GPIO.HIGH)
     SWITCH_STATUS = 1
    else:
     print "Switch status OFF"
     # Turn all relays OFF
     GPIO.output(18, GPIO.LOW)
     GPIO.output(23, GPIO.LOW)
     GPIO.output(24, GPIO.LOW)
     GPIO.output(25, GPIO.LOW)
     SWITCH_STATUS = 0

def setSwitchStatus():
    global SWITCH_STATUS
    SWITCH_STATUS = 0
