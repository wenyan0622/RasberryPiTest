import RPi.GPIO as GPIO
import time
#程序目的：检测光敏传感器的输入信号，检测到光则小灯亮，否则灯灭

#分别指定传感器接口和LED灯接口
LightSensor_PIN=7
LED_PIN=12

#初始化
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LightSensor_PIN,GPIO.IN)
    GPIO.setup(LED_PIN,GPIO.OUT)
    pass

#循环检测100次
def detect():
    count=1
    for count in range(1,100):
        if GPIO.input(LightSensor_PIN) == True:
            GPIO.output(LED_PIN,True) #检测到灯光则灯亮
            print("light on ...",count)
        else:
            GPIO.output(LED_PIN,False) #没有检测到光则灯灭
            print("light off ...",count)
        count=count+1
        time.sleep(1)#1秒循环

try:
    init()
    detect()
except KeyboardInterrupt:
    pass

#清理工作
GPIO.cleanup()