import zipfile
from config.settings import OUTPUT_FILE, ZIP_FILE

def zip_output():

    with zipfile.ZipFile(ZIP_FILE, "w") as zipf:
        zipf.write(OUTPUT_FILE, arcname="mashup.mp3")
