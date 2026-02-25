import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

VIDEOS_DIR = os.path.join(DATA_DIR, "videos")
AUDIOS_DIR = os.path.join(DATA_DIR, "audios")
CLIPS_DIR = os.path.join(DATA_DIR, "clips")
OUTPUT_DIR = os.path.join(DATA_DIR, "output")
ZIP_DIR = os.path.join(DATA_DIR, "zip")

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mashup.mp3")
ZIP_FILE = os.path.join(ZIP_DIR, "mashup.zip")
