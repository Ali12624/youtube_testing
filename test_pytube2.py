from pytube import YouTube
import requests
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Change to DEBUG for more detailed logs
)

logger = logging.getLogger(__name__)

url = 'https://www.youtube.com/watch?v=PpOKVm4Vjzc'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    try:
        res = requests.get(url ,headers)
        logger.debug(res)
    except Exception:
        print(Exception)
    yt = YouTube(url)
    logger.debug(yt)
    try:
        stream = yt.streams.get_highest_resolution()
        download_url = stream.url

        print(url)

    except Exception:
        print(Exception)    

except Exception:
    print(Exception)