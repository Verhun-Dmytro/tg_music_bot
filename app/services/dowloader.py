from yt_dlp import YoutubeDL
import os


def dowload_music(music):

    url_tube = f"https://www.youtube.com/watch?v={music}"
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio/%(music)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }     

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url_tube, download=True)

        return f"audio/{music}.mp3"
        
    except:
        print("Not dowload music")
        return ""    


def delete_music(music):

    try:
        os.remove(music)
    except FileExistsError as e:
        print(f"{e}")