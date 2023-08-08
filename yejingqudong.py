import RPi.GPIO as GPIO
import time

# 定义液晶面板的引脚
LCD_RS = 21
LCD_E = 20
LCD_D4 = 26
LCD_D5 = 19
LCD_D6 = 13
LCD_D7 = 6

# 定义液晶面板的行和列
LCD_WIDTH = 16   # 每行字符数
LCD_LINE_1 = 0x80  # LCD显示第一行的地址
LCD_LINE_2 = 0xC0  # LCD显示第二行的地址

# 定义液晶面板操作相关的常量
LCD_CHR = True
LCD_CMD = False
LCD_BACKLIGHT = 0x08  # 打开背光

# 定义液晶面板操作函数
def lcd_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)        # 设置GPIO引脚编号模式为BCM模式
    GPIO.setup(LCD_E, GPIO.OUT)   # 设置液晶面板E引脚为输出模式
    GPIO.setup(LCD_RS, GPIO.OUT)  # 设置液晶面板RS引脚为输出模式
    GPIO.setup(LCD_D4, GPIO.OUT)  # 设置液晶面板D4引脚为输出模式
    GPIO.setup(LCD_D5, GPIO.OUT)  # 设置液晶面板D5引脚为输出模式
    GPIO.setup(LCD_D6, GPIO.OUT)  # 设置液晶面板D6引脚为输出模式
    GPIO.setup(LCD_D7, GPIO.OUT)  # 设置液晶面板D7引脚为输出模式
    lcd_backlight(True)
    lcd_byte(0x33, LCD_CMD)      # 初始化液晶面板
    lcd_byte(0x32, LCD_CMD)      # 初始化液晶面板
    lcd_byte(0x06, LCD_CMD)      # 光标向右移动
    lcd_byte(0x0C, LCD_CMD)      # 显示开，光标不显示
    lcd_byte(0x28, LCD_CMD)      # 4位数据接口，两行显示，5x8点阵字符

def lcd_byte(bits, mode):
    GPIO.output(LCD_RS, mode)
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x10 == 0x10:
        GPIO.output(LCD_D4, True)
    if bits & 0x20 == 0x20:
        GPIO.output(LCD_D5, True)
    if bits & 0x40 == 0x40:
        GPIO.output(LCD_D6, True)
    if bits & 0x80 == 0x80:
        GPIO.output(LCD_D7, True)
    lcd_toggle_enable()
    GPIO.output(LCD_D4, False)
    GPIO.output(LCD_D5, False)
    GPIO.output(LCD_D6, False)
    GPIO.output(LCD_D7, False)
    if bits & 0x01 == 0x01:
        GPIO.output(LCD_D4, True)
    if bits & 0x02 == 0x02:
        GPIO.output(LCD_D5, True)
    if bits & 0x04 == 0x04:
        GPIO.output(LCD_D6, True)
    if bits & 0x08 == 0x08:
        GPIO.output(LCD_D7, True)
    lcd_toggle_enable()

def lcd_toggle_enable():
    time.sleep(0.0005)
    GPIO.output(LCD_E, True)
    time.sleep(0.0005)
    GPIO.output(LCD_E, False)
    time.sleep(0.0005)

def lcd_string(message, line):
    message = message.ljust(LCD_WIDTH, " ")
    lcd_byte(line, LCD_CMD)
    for i in range(LCD_WIDTH):
        lcd_byte(ord(message[i]), LCD_CHR)

def lcd_backlight(on):
    if on:
        GPIO.output(LCD_BACKLIGHT, True)
    else:
        GPIO.output(LCD_BACKLIGHT, False)

if __name__ == '__main__':
    lcd_init()
    lcd_string("Hello, LCD!", LCD_LINE_1)
    lcd_string("Welcome to", LCD_LINE_
