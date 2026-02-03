import streamlit as st
import streamlit.components.v1
from pong.pong_js import Pong

pong = Pong.game()

st.title("PLAY PONG", text_alignment="center")
st.subheader("Just because it's fun!", text_alignment="center")
streamlit.components.v1.html(html=pong, width=650, height=650)