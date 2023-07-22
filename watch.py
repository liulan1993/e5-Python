import datetime
import lunarcalendar
import requests
from astral import LocationInfo
import astral.sun
import astral.moon
import gpsd

# 获取当前日期和时间
def get_current_time():
    return datetime.datetime.now()

# 获取阳历日期
def get_gregorian_date():
    return datetime.date.today()

# 获取阴历日期
def get_lunar_date():
    lunar_date = lunarcalendar.Lunar(datetime.date.today())
    return f"{lunar_date.year}年{lunar_date.month}月{lunar_date.day}"

# 获取星期
def get_weekday():
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    return weekdays[datetime.datetime.today().weekday()]

# 获取天气信息（以北京为例）
def get_weather():
    api_key = "YOUR_WEATHER_API_KEY"
    city = "Beijing"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"{city}：{weather_description}，温度：{temperature}°C"
    else:
        return "获取天气信息失败"

# 获取月相信息
def get_moon_phase():
    location = LocationInfo("Beijing")
    today = datetime.date.today()
    moon_phase = astral.moon.phase(today, location.observer)
    return "满月" if moon_phase == 15 else "其他"

# 获取GPS信息（海拔和气压）
def get_gps_info():
    gpsd.connect()
    packet = gpsd.get_current()
    altitude = packet.altitude()
    pressure = packet.pressure()
    return f"海拔：{altitude}米，气压：{pressure}帕"

# 主程序
def main():
    print("欢迎使用手表指令集！")
    while True:
        print("\n请选择功能：")
        print("1. 显示时间")
        print("2. 显示阳历日期")
        print("3. 显示阴历日期")
        print("4. 显示星期")
        print("5. 显示天气信息")
        print("6. 显示月相")
        print("7. 显示GPS信息")
        print("0. 退出")
        choice = input("请输入选项：")

        if choice == "1":
            print("当前时间：", get_current_time())
        elif choice == "2":
            print("阳历日期：", get_gregorian_date())
        elif choice == "3":
            print("阴历日期：", get_lunar_date())
        elif choice == "4":
            print("星期：", get_weekday())
        elif choice == "5":
            print("天气信息：", get_weather())
        elif choice == "6":
            print("月相：", get_moon_phase())
        elif choice == "7":
            print("GPS信息：", get_gps_info())
        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效的选项，请重新输入！")

if __name__ == "__main__":
    main()
