from yt_dlp  import YoutubeDL

# آدرس ویدیو را وارد کنید
# video_url = 'https://www.youtube.com/watch?v=your_video_id'

# # تنظیمات دانلود
# ydl_opts = {
#     'format': 'best',  # بهترین کیفیت را دانلود کنید
#     'outtmpl': '/path/to/save/%(title)s.%(ext)s',  # محل ذخیره ویدیو
# }

# # دانلود ویدیو
# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([video_url])


url = 'https://www.youtube.com/watch?v=KLfkcSM4SrI'


with YoutubeDL() as ydl:
    info_dict = ydl.extract_info(url, download=False)  # Don't download, just get info
    formats = info_dict['formats']
    for fmt in formats:
        print(f"Format ID: {fmt['format_id']}, Extension: {fmt['ext']}, Quality: {fmt['height'] if 'height' in fmt else 'N/A'}")


