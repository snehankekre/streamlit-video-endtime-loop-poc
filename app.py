import numpy as np
import streamlit as st

VIDEO_URL = "https://static.streamlit.io/examples/star.mp4"

col1, col2 = st.columns(2)
start_time = col1.slider("Start time", 0, 5, 0)
end_time = col2.slider("End time", 0, 5, 5)
loop = st.toggle("Loop media", True)

st.video(VIDEO_URL, start_time=start_time, end_time=end_time, loop=loop)


sample_rate = 44100
seconds = 5
frequency_la = 440
t = np.linspace(0, seconds, seconds * sample_rate, False)
AUDIO_URL = np.sin(frequency_la * t * 2 * np.pi)

st.audio(AUDIO_URL, sample_rate=sample_rate, start_time=start_time, end_time=end_time, loop=loop)