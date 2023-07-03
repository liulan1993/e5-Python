import serial

def read_weight(ser):
    ser.write(b'W\r\n')
    response = ser.readline().strip().decode('utf-8')
    weight = float(response)
    return weight

def main():
    port = 'COM1'  # 替换成你的电子秤串口号
    baud_rate = 9600  # 波特率
    timeout = 1  # 超时时间（秒）

    ser = serial.Serial(port, baud_rate, timeout=timeout)

    try:
        ser.open()
        if ser.is_open:
            print('电子秤已连接')
            while True:
                weight = read_weight(ser)
                print(f'当前重量: {weight:.2f} 克')
    except serial.SerialException:
        print('无法打开电子秤串口')
    finally:
        if ser.is_open:
            ser.close()

if __name__ == '__main__':
    main()
