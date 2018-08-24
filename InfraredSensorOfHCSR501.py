import RPi.GPIO as GPIO
import time

#设定红外传感器和LED灯引脚
SENSOR_PIN=7
LED_PIN=12

#初始化
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SENSOR_PIN,GPIO.IN) # 红外传感器
    GPIO.setup(LED_PIN,GPIO.OUT) # LED二极管
    pass

#检测函数
def detct():
    for i in range(1, 31):
        if GPIO.input(SENSOR_PIN) == True:#检测到信号
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Someone is closing!") #打印语句
            GPIO.output(LED_PIN,True)#检测到信号灯亮
        else:
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "  Noanybody!")

        time.sleep(3)  # 每6秒检查一次

        if GPIO.input(LED_PIN) == True:
            GPIO.output(LED_PIN, False)
            print("led is off")

#执行
init()
detct()
GPIO.cleanup()
