import requests
from bs4 import BeautifulSoup

def get_lyrics(artist, song):
    # 构建搜索URL
    url = f"https://www.azlyrics.com/lyrics/{artist}/{song}.html"
    
    try:
        # 发送HTTP GET请求并获取响应
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到歌词所在的标签
        lyrics_div = soup.find('div', class_='ringtone')

        # 提取歌词文本
        lyrics = lyrics_div.text.strip()

        return lyrics

    except requests.exceptions.RequestException as e:
        print("请求出错:", e)

# 示例用法
artist = "adele"
song = "someone-like-you"
lyrics = get_lyrics(artist, song)
if lyrics:
    print(lyrics)
else:
    print("未找到歌词。")
