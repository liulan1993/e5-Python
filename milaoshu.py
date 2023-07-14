import time
import RPi.GPIO as GPIO

# LED引脚连接
RED_PIN = 17
GREEN_PIN = 18
BLUE_PIN = 27

# 初始化GPIO设置
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

# 定义米老鼠跳舞的动作
def mickey_dance():
    GPIO.output(RED_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(GREEN_PIN, GPIO.LOW)
    GPIO.output(BLUE_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(BLUE_PIN, GPIO.LOW)

# 执行米老鼠跳舞动作
try:
    while True:
        mickey_dance()
except KeyboardInterrupt:
    pass

# 清理GPIO设置
GPIO.cleanup()
