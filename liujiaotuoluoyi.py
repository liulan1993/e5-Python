import time
import board
import busio
import adafruit_lsm6ds

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm6ds.LSM6DS33(i2c)

while True:
    acceleration = sensor.acceleration
    gyro = sensor.gyro

    print("加速度 (m/s^2): X=%0.2f Y=%0.2f Z=%0.2f" % (acceleration[0], acceleration[1], acceleration[2]))
    print("角速度 (rad/s): X=%0.2f Y=%0.2f Z=%0.2f" % (gyro[0], gyro[1], gyro[2]))

    time.sleep(0.5)
