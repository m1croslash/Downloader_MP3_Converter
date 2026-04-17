import yt_dlp
import os

def converter_mp3(url, save_path='./Downloads'): # Auto-Create folder with your name  
    os.makedirs(save_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': r'', # Location ffmpeg on OS
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    link = input('Link: ').strip()
    converter_mp3(link)
  
# So...first step you need download ffmpeg, recommending file example: ffmpeg-8.1-essentials_build
