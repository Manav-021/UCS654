from moviepy.editor import VideoFileClip
import os
from config.settings import VIDEOS_DIR, AUDIOS_DIR

def convert_to_audio():

    for file in os.listdir(VIDEOS_DIR):
        if file.endswith(".mp4"):

            video_path = os.path.join(VIDEOS_DIR, file)
            audio_path = os.path.join(AUDIOS_DIR, file.replace(".mp4", ".mp3"))

            clip = VideoFileClip(video_path)
            clip.audio.write_audiofile(audio_path)
            clip.close()
