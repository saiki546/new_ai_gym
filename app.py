import streamlit as st
import streamlit_webrtc
import aiortc
import aioice
import av
import sys

st.write("Python:", sys.version)
st.write("streamlit:", st.__version__)
st.write("streamlit-webrtc:", streamlit_webrtc.__version__)
st.write("aiortc:", aiortc.__version__)
st.write("aioice:", aioice.__version__)
st.write("av:", av.__version__)
