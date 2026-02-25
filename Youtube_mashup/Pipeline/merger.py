from pydub import AudioSegment
import os
from config.settings import CLIPS_DIR, OUTPUT_FILE

def merge_audios():

    combined = AudioSegment.empty()

    for file in os.listdir(CLIPS_DIR):
        if file.endswith(".mp3"):

            clip_path = os.path.join(CLIPS_DIR, file)
            audio = AudioSegment.from_mp3(clip_path)

            combined += audio

    combined.export(OUTPUT_FILE, format="mp3")
