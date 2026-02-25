import os
import shutil
from config.settings import VIDEOS_DIR, AUDIOS_DIR, CLIPS_DIR, OUTPUT_DIR, ZIP_DIR

def create_folders():
    for folder in [VIDEOS_DIR, AUDIOS_DIR, CLIPS_DIR, OUTPUT_DIR, ZIP_DIR]:
        os.makedirs(folder, exist_ok=True)

def clean_folders():
    for folder in [VIDEOS_DIR, AUDIOS_DIR, CLIPS_DIR, OUTPUT_DIR, ZIP_DIR]:
        if os.path.exists(folder):
            shutil.rmtree(folder)
        os.makedirs(folder)
