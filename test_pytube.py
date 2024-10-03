import pytube
import requests
from pytube import YouTube
import logging
from time import sleep



url = 'https://www.youtube.com/watch?v=Jnl7rkz93MQ&t=1s'


res = requests.get(url)
print(res)
if res.status_code == 200:
    try:
        yt = YouTube(url)

        # yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        # yt.streams.filter(file_extension='mp4').first().download()


        try:
            streams = yt.streams.get_highest_resolution()

            down_url = streams.url

            print(down_url)
        except Exception as e:
            print(e)

    except Exception:
        print(Exception)