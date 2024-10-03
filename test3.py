import pytube
from pytube import YouTube

url = 'https://www.youtube.com/watch?v=Jnl7rkz93MQ&t=1s'


try:
    yt = YouTube(url)
    
    # Get the highest resolution stream
    streams = yt.streams.get_highest_resolution()
    
    # Print stream URL (if needed)
    print(f"Stream URL: {streams.url}")
    
    # Just check if the stream is available
    if streams:
        print("Stream is available!")
    else:
        print("No streams available.")

except Exception as e:
    print(f"An error occurred: {e}")
