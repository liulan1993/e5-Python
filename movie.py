import vlc

def play_movie(movie_path):
    # 创建一个VLC播放器实例
    player = vlc.MediaPlayer()

    # 加载电影文件
    media = vlc.Media(movie_path)

    # 将电影文件设置为播放器的媒体
    player.set_media(media)

    # 播放电影
    player.play()

    # 等待电影播放完毕
    while player.is_playing():
        pass

    # 释放播放器资源
    player.release()

# 电影文件的路径
movie_path = "path/to/your/movie.mp4"

# 调用播放函数
play_movie(movie_path)
