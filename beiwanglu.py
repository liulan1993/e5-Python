import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# 备忘录数据结构示例
memo_data = {
    "天气": "",
    "时间": "",
    "星期": "",
    "阴历": "",
    "阳历": "",
    "待办事项": [],
    "完成进度": {},
    "定时提醒": []
}

# 获取天气信息的函数
def get_weather():
    # 这里使用了一个天气API的例子，你需要自行申请一个API并替换下面的URL
    api_key = "YOUR_WEATHER_API_KEY"
    city = "YOUR_CITY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    weather_description = data["weather"][0]["description"]
    return weather_description

# 更新备忘录信息的函数
def update_memo_data():
    now = datetime.now()
    memo_data["天气"] = get_weather()
    memo_data["时间"] = now.strftime("%H:%M:%S")
    memo_data["星期"] = now.strftime("%A")
    # 在这里你可以调用其他方法获取阴历、阳历等信息，这里不再展示具体实现
    # ...
    print("备忘录已更新：", memo_data)

# 添加待办事项的函数
def add_todo_item(item):
    memo_data["待办事项"].append(item)
    memo_data["完成进度"][item] = False
    print("待办事项已添加：", item)

# 更新待办事项完成状态的函数
def update_todo_item_status(item, status):
    if item in memo_data["完成进度"]:
        memo_data["完成进度"][item] = status
        print("待办事项更新完成状态：", item, status)

# 添加定时提醒的函数
def add_reminder(reminder_time, reminder_text):
    memo_data["定时提醒"].append((reminder_time, reminder_text))
    print("定时提醒已添加：", reminder_time, reminder_text)

# 在命令行中查看备忘录信息的函数
def view_memo():
    print("\n===== 备忘录 =====")
    for key, value in memo_data.items():
        if key == "待办事项":
            print("\n", key, ":")
            for item, status in value.items():
                print(f" - {item} [{status}]")
        elif key == "定时提醒":
            print("\n", key, ":")
            for reminder in value:
                print(f" - 时间：{reminder[0]}, 内容：{reminder[1]}")
        else:
            print(key, ":", value)
    print("==================\n")

# 初始化备忘录数据
update_memo_data()

# 使用定时任务定期更新备忘录信息（每隔5分钟）
scheduler = BackgroundScheduler()
scheduler.add_job(update_memo_data, trigger="interval", minutes=5)
scheduler.start()

# 主程序循环
while True:
    print("\n===== 备忘录功能菜单 =====")
    print("1. 添加待办事项")
    print("2. 更新待办事项完成状态")
    print("3. 添加定时提醒")
    print("4. 查看备忘录")
    print("5. 退出")
    choice = input("请输入功能对应的序号：")

    if choice == "1":
        item = input("请输入待办事项：")
        add_todo_item(item)
    elif choice == "2":
        item = input("请输入待办事项：")
        status = input("请输入完成状态（True/False）：").lower() == "true"
        update_todo_item_status(item, status)
    elif choice == "3":
        reminder_time = input("请输入定时提醒时间（格式：YYYY-MM-DD HH:MM:SS）：")
        reminder_text = input("请输入定时提醒内容：")
        add_reminder(reminder_time, reminder_text)
    elif choice == "4":
        view_memo()
    elif choice == "5":
        scheduler.shutdown()
        break
    else:
        print("无效的选择，请重新输入。")
