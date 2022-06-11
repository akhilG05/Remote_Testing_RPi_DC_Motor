import RPi.GPIO as GPIO # using RPi.GPIO module
from time import sleep # import function sleep for delay

GPIO.setmode(GPIO.BCM) # GPIO numbering
GPIO.setwarnings(False) # enable warning from GPIO

AN = 23 # set pwm2 pin on MDDS10 to GPIO 25
DIG = 24 # set dir2 pin on MDDS10 to GPIO 23

GPIO.setup(AN, GPIO.OUT) # set pin as output
GPIO.setup(DIG, GPIO.OUT) # set pin as output

sleep(1) # delay for 1 seconds
p = GPIO.PWM(AN, 100) # set pwm for M1

print("Anti-clockwise") # display "Forward" when program executed
GPIO.output(DIG, GPIO.HIGH) # set DIG1 as high, dir2 = forward
p.start(50) # set speed for M1, speed=0 – 100
sleep(5) # delay for 1 seconds
        
print("Clockwise") # display "Backward" when program executed
GPIO.output(DIG, GPIO.LOW) # set DIG2 as low, DIR = backward
p.start(50) # set speed for M2, speed=0 – 100
sleep(5) # delay for 1 seconds

p.start(0)