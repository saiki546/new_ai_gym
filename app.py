import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

ctx = webrtc_streamer(
    key="test",
    mode=WebRtcMode.RECVONLY,
)

st.write(ctx.state.playing)
