from yt_dlp import YoutubeDL

# search music in youtube.
def search_music_ytdlp(name_music):
    option_dlp = {
        "quiet": True,
        "format": "bestaudio/best",
        "extract_flat": "in_playlist",
        "noplaylist": True,
        "no_warnings": True,
    }

    with YoutubeDL(option_dlp) as ydl:
        data = ydl.extract_info(f"ytsearch10:music {name_music}", download=False)

    return data


# Trim music to between 360 seconds and 40 seconds.
def clip_music(date_music):
    music_list = {}

    try:
        num = 1
        for i in date_music["entries"]:
            id = i.get("id")
            title = i.get("title")
            duration = i.get("duration")
            if duration < 360 and duration >= 40 and num <= 5:
                music_list[title] = id
                num += 1
                # print(f"{duration},  {title},{url}")
        
        # print(f"{music_list}")
        # print(f"{len(music_list)}")
        return music_list
    except:
        print("Do not added music for playlist")
        music_list = {}
        


if __name__ == "__main__":
    clip_music(search_music_ytdlp("Зібров"))
