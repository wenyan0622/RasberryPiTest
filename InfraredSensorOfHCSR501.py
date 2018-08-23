import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.IN)
    pass

def detct():
    for i in range(1, 31):
        if GPIO.input(7) == True:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!")
         else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Noanybody!")
        time.sleep(6)  # 每6秒检查一次

time.sleep(2)
init()
detct()
