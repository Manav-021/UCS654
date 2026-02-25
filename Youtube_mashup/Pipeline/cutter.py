from pydub import AudioSegment
import os
from config.settings import AUDIOS_DIR, CLIPS_DIR

def cut_first_30_sec():

    for file in os.listdir(AUDIOS_DIR):
        if file.endswith(".mp3"):

            input_path = os.path.join(AUDIOS_DIR, file)
            output_path = os.path.join(CLIPS_DIR, file)

            audio = AudioSegment.from_mp3(input_path)

            clip = audio[:30000] 
            clip.export(output_path, format="mp3")
