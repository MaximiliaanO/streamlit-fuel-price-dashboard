import streamlit as st
from content_text.text import STREAMLITTEXT
from pathlib import Path

BASE_DIR = Path(__file__).parent
with st.container(horizontal_alignment="center"):
    bits = 8
    st.image(BASE_DIR / f"content_text/{bits}-bitme.png", width=200, caption=f"Maximiliaan Oorschot ({bits}-bit versie)")

st.markdown(STREAMLITTEXT.HOMEPAGETEXT)
