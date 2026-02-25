import streamlit as st
from utils.helpers import create_folders, clean_folders
from pipeline.downloader import download_videos
from pipeline.audio_converter import convert_to_audio
from pipeline.cutter import cut_first_30_sec
from pipeline.merger import merge_audios
from pipeline.zipper import zip_output
from pipeline.mailer import send_mail

st.title("🎵 YouTube Mashup Automation")

query = st.text_input("Enter YouTube Search Term", "sharry maan")
num_videos = st.slider("Number of Videos", 1, 30, 10)
email = st.text_input("Enter Email")

if st.button("Run Pipeline 🚀"):

    clean_folders()
    create_folders()

    with st.spinner("Downloading Videos..."):
        download_videos(query, max_videos=num_videos)

    with st.spinner("Converting to Audio..."):
        convert_to_audio()

    with st.spinner("Cutting First 30 Seconds..."):
        cut_first_30_sec()

    with st.spinner("Merging Audios..."):
        merge_audios()

    with st.spinner("Zipping File..."):
        zip_output()

    if email:
        with st.spinner("Sending Email..."):
            send_mail(email)

    st.success("Pipeline Completed Successfully ✅")
