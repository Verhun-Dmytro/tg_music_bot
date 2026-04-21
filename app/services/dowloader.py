from yt_dlp import YoutubeDL
import moviepy
import os
from pathlib import Path

def dowload_music(music):

    url_tube = f"https://www.youtube.com/watch?v={music}"
    base_dir = Path(__file__).parent
    base_dir_output = base_dir / "audio"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{base_dir_output}/%(title)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        # "postprocessors": [{
        #     "key": "FFmpegExtractAudio",
        #     "preferredcodec": "mp3",
        #     "preferredquality": "192",
        # }],
    }     

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url_tube, download=True)
            audioext = info["ext"]
            music_name = info["title"]

            music = {"output" : f"{base_dir_output}/{music_name}.{audioext}", "filename" : f"{music_name}"}
        return music
    #f"{base_dir_output}/{music}.{audioext}"
        
    except Exception as e:
        print("Not dowload music! {e}")
        return ""    


def delete_music(music):

    try:
        os.remove(music)
    except Exception as e:
        print(f"Error deleting file: {e}")


def convert_video_to_audio(music):
    try:

        base_dir = Path(__file__).parent
        file_dir_name = base_dir / f'audio/{music["filename"]}.mp3'

        audio = moviepy.AudioFileClip(music["output"])
        audio.write_audiofile(f"{file_dir_name}")

        return file_dir_name
    except (FileNotFoundError, OSError) as e:
        print(f"Error convert audio {e}")



if __name__ == "__main__":
   audio = convert_video_to_audio("audio/NA.webm")
   a = 0