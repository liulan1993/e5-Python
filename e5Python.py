import time

def focus_timer(minutes):
    seconds = minutes * 60
    print(f"专注倒计时开始：{minutes} 分钟")

    time.sleep(seconds)
    print("时间到！专注时间结束。")

# 设置专注时间为 25 分钟
focus_timer(25)
