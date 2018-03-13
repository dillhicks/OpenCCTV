import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

p = GPIO.PWM(12, 50)
l = GPIO.PWM(33, 50)

global xpos
global ypos
xpos = 7.5
ypos = 10.5 

p.start(xpos)
l.start(ypos)

def moveRight():
    global xpos
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(7.5)
    try:
        p.ChangeDutyCycle(xpos)
        xpos = xpos + 1
        p.ChangeDutyCycle(xpos)
        time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    print(xpos)
        
    
def moveLeft():
    global xpos
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(xpos)
    try:
        p.ChangeDutyCycle(xpos)
        xpos = xpos - 1
        p.ChangeDutyCycle(xpos)
        time.sleep(0.5)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    print(xpos)
def moveUp():
    global ypos
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(33, GPIO.OUT)
    l = GPIO.PWM(33, 50)
    l.start(ypos)
    try:
        ypos = ypos + 1
        l.ChangeDutyCycle(ypos)
        time.sleep(0.5)
    except KeyboardInterrupt:
        l.stop()
        GPIO.cleanup()
    print(ypos)
def moveDown():
    global ypos
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(33, GPIO.OUT)
    l = GPIO.PWM(33, 50)
    l.start(ypos)
    try:
        ypos = ypos - 1
        l.ChangeDutyCycle(ypos)
        time.sleep(0.5)
    except KeyboardInterrupt:
        l.stop()
        GPIO.cleanup()
    print(ypos)
def center():
    global ypos
    global xpos
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(33, GPIO.OUT)
    l = GPIO.PWM(33, 50)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(7.5)
    l.start(7.5)
    ypos = 10.5
    xpos = 7.5
    try:
        l.ChangeDutyCycle(10.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(0.5)
    except KeyboardInterrupt:
        l.stop()
        p.stop()
        GPIO.cleanup()
    print(ypos)
    print(xpos)
