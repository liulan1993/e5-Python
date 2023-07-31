from djitellopy import Tello
import time

# 连接无人机
tello = Tello()
tello.connect()

# 启动无人机
tello.takeoff()

# 发送指令：向前飞行
tello.send_rc_control(0, 20, 0, 0)
time.sleep(2)  # 等待2秒

# 发送指令：悬停
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)  # 等待1秒

# 发送指令：旋转
tello.send_rc_control(0, 0, 0, 30)
time.sleep(3)  # 等待3秒

# 发送指令：悬停
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)  # 等待1秒

# 发送指令：向前飞行
tello.send_rc_control(0, 20, 0, 0)
time.sleep(2)  # 等待2秒

# 发送指令：悬停
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)  # 等待1秒

# 发送指令：旋转
tello.send_rc_control(0, 0, 0, -30)
time.sleep(3)  # 等待3秒

# 发送指令：悬停
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)  # 等待1秒

# 发送指令：向后飞行
tello.send_rc_control(0, -20, 0, 0)
time.sleep(2)  # 等待2秒

# 发送指令：悬停
tello.send_rc_control(0, 0, 0, 0)
time.sleep(1)  # 等待1秒

# 发送指令：降落
tello.land()

# 断开连接
tello.disconnect()
