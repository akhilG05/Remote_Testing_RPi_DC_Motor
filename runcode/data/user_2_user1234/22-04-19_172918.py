import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep # import function sleep for delay

GPIO.setmode(GPIO.BCM) # GPIO numbering
GPIO.setwarnings(False) # enable warning from GPIO

AN1 = 24 # set pwm1 pin on MDDS10 to GPIO 24
DIG1 = 18 # set dir1 pin on MDDS10 to GPIO 18

GPIO.setup(AN1, GPIO.OUT) # set pin as output
GPIO.setup(DIG1, GPIO.OUT) # set pin as output

sleep(1) # delay for 1 seconds
p1 = GPIO.PWM(AN1, 100) # set pwm for M1

GPIO.output(DIG1, GPIO.HIGH) # set DIG1 as high, dir2 = forward
p1.start(50) # set speed for M1, speed=0 - 100
sleep(5)	 # delay for 1 seconds
GPIO.output(DIG1, GPIO.LOW) # set DIG1 as low, DIR = backward
p1.start(50) # set speed for M1, speed=0 - 100
sleep(5) # delay for 1 seconds