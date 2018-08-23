import RPi.GPIO  as GPIO
import time
 
# mapping LED to GPIO
LED_A = 26 # 11
LED_B = 19 # 7
LED_C = 22 # 4
LED_D = 6 # 2
LED_E = 17 # 1
LED_F = 11 # 10
LED_G = 9 # 5
LED_DP = 10 # 3

# mapping public GPIO
DIGIT1 = 12 # 12
DIGIT2 = 16 # 9
DIGIT3 = 20 # 8
DIGIT4 = 21 # 6

#初始化
def init():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED_A, GPIO.OUT)
    GPIO.setup(LED_B, GPIO.OUT)
    GPIO.setup(LED_C, GPIO.OUT)
    GPIO.setup(LED_D, GPIO.OUT)
    GPIO.setup(LED_E, GPIO.OUT)
    GPIO.setup(LED_F, GPIO.OUT)
    GPIO.setup(LED_G, GPIO.OUT)
    GPIO.setup(LED_DP, GPIO.OUT)
    GPIO.setup(DIGIT1, GPIO.OUT)
    GPIO.setup(DIGIT2, GPIO.OUT)
    GPIO.setup(DIGIT3, GPIO.OUT)
    GPIO.setup(DIGIT4, GPIO.OUT)

def reset():
    GPIO.output(DIGIT1, False)
    GPIO.output(DIGIT2, False)
    GPIO.output(DIGIT3, False)
    GPIO.output(DIGIT4, False)

    GPIO.output(LED_A,True)
    GPIO.output(LED_B,True)
    GPIO.output(LED_C,True)
    GPIO.output(LED_D,True)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,False)

def setCount(num):
    if(num==1):
        GPIO.output(DIGIT1, True)
        # GPIO.output(DIGIT2, False)
        # GPIO.output(DIGIT3, False)
        # GPIO.output(DIGIT4, False)
    elif(num==2):
        # GPIO.output(DIGIT1, False)
        GPIO.output(DIGIT2, True)
        # GPIO.output(DIGIT3, False)
        # GPIO.output(DIGIT4, False)
    elif(num==3):
        # GPIO.output(DIGIT1, False)
        # GPIO.output(DIGIT2, False)
        GPIO.output(DIGIT3, True)
        # GPIO.output(DIGIT4, False)
    elif(num==4):
        # GPIO.output(DIGIT1, False)
        # GPIO.output(DIGIT2, False)
        # GPIO.output(DIGIT3, False)
        GPIO.output(DIGIT4, True)
    else:
        print("Set Count ERROR!")

def show_0():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,False)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,True)
    GPIO.output(LED_DP,True)

def show_1():
    GPIO.output(LED_A,True)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,True)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,True)
    GPIO.output(LED_DP,True)

def show_2():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,True)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,False)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_3():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_4():
    GPIO.output(LED_A,True)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,True)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_5():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,True)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_6():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,True)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,False)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_7():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,True)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,True)
    GPIO.output(LED_DP,True)

def show_8():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,False)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_9():
    GPIO.output(LED_A,False)
    GPIO.output(LED_B,False)
    GPIO.output(LED_C,False)
    GPIO.output(LED_D,False)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,False)
    GPIO.output(LED_G,False)
    GPIO.output(LED_DP,True)

def show_dot(num1):
    GPIO.output(LED_A,True)
    GPIO.output(LED_B,True)
    GPIO.output(LED_C,True)
    GPIO.output(LED_D,True)
    GPIO.output(LED_E,True)
    GPIO.output(LED_F,True)
    GPIO.output(LED_G,True)
    GPIO.output(LED_DP,False)

def showSingleDigit(num):
    if(num == 0):
        show_0()
    elif(num == 1):
        show_1()
    elif(num == 2):
        show_2()
    elif(num == 3):
        show_3()
    elif(num == 4):
        show_4()
    elif(num == 5):
        show_5()
    elif(num == 6):
        show_6()
    elif(num == 7):
        show_7()
    elif (num == 8):
        show_8()
    elif (num == 9):
        show_9()
    else:
        print("error")

def showonenum(wei,num):
    setCount(wei)
    showSingleDigit(num)

#開始執行
init()

#初始化
reset()

count=0
while(count<10):
    timestr = time.strftime("%M%S", time.localtime())#获取当前时间字符串
    led1=int(timestr[0])
    led2=int(timestr[1])
    led3=int(timestr[2])
    led4=int(timestr[3])
    showonenum(1,led1)
    showonenum(2,led2)
    showonenum(3,led3)
    showonenum(4,led4)
    count=count+1
    time.sleep(1)

#
# while True:
#     print(time.strftime("%H:%M:%S", time.localtime()))
#     timestr = time.strftime("%M%S", time.localtime())#获取当前时间字符串
#     led1=int(timestr[0])
#     led2=int(timestr[1])
#     led3=int(timestr[2])
#     led4=int(timestr[3])
#     print(led1,led2,led3,led4)
#
#     GPIO.output(DIGIT1,True)
#     # GPIO.output(DIGIT2,False)
#     # GPIO.output(DIGIT3,False)
#     # GPIO.output(DIGIT4,False)
#     showSingleDigit(led1) #数码管第1位显示
#
#     # GPIO.output(DIGIT1,False)
#     GPIO.output(DIGIT2,True)
#     # GPIO.output(DIGIT3,False)
#     # GPIO.output(DIGIT4,False)
#     showSingleDigit(led2) #数码管第2位显示
#
#     # GPIO.output(DIGIT1,False)
#     # GPIO.output(DIGIT2,False)
#     GPIO.output(DIGIT3,True)
#     # GPIO.output(DIGIT4,False)
#     showSingleDigit(led3) #数码管第3位显示
#
#     # GPIO.output(DIGIT1,False)
#     # GPIO.output(DIGIT2,False)
#     # GPIO.output(DIGIT3,False)
#     GPIO.output(DIGIT4,True)
#     showSingleDigit(led4) #数码管第4位显示
#     #showCurrentTime(list)
#     time.sleep(1)

GPIO.cleanup()
