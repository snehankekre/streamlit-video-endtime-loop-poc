import numpy as np
import streamlit as st

st.subheader("🔁🔚 Specify end time and looping behavior for media")

st.markdown("For more information, see the [end_time](https://www.notion.so/snowflake-corp/end_time-for-st-video-and-st-audio-b0addaf6d5fa4863bcb194081a23669a) and [loop](https://www.notion.so/snowflake-corp/Loop-st-video-and-st-audio-fea53f2e434e44619060d2fb9818b525) for st.audio and st.video Notion pages. Get the wheel file [here](https://github.com/snehankekre/streamlit-video-endtime-loop-poc/raw/main/streamlit-1.27.2-py2.py3-none-any.whl).")
st.write("""
1. Just as st.video and st.audio have a `start_time` parameter, we will support `end_time` — the time at which this element should stop playing.
2. st.video and st.audio will optionally accept a boolean `loop` parameter to automatically seek back to the start upon reaching the end of the media.
""")


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