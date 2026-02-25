import yt_dlp
import os
from config.settings import VIDEOS_DIR

def download_videos(query, max_videos=10):

    ydl_opts = {
        "format": "mp4",
        "outtmpl": os.path.join(VIDEOS_DIR, "%(title)s.%(ext)s"),
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{max_videos}:{query}"])
