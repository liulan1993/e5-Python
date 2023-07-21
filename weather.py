import requests
import json

def get_weather(city_name):
    api_key = 'YOUR_API_KEY'  # 请在OpenWeatherMap官网注册获取API密钥，并替换为您的密钥

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)
    data = json.loads(response.text)

    if data['cod'] == 200:
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f'天气情况：{main_weather} ({description})')
        print(f'温度：{temperature} K')
        print(f'湿度：{humidity} %')
        print(f'风速：{wind_speed} m/s')
    else:
        print('获取天气信息失败')

city = input('请输入城市名称：')
get_weather(city)
