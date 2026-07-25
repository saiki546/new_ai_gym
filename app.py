import streamlit as st
from streamlit_webrtc import webrtc_streamer

st.title("Test")

ctx = webrtc_streamer(key="test")

st.write(ctx.state.playing)
