import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent

benzineprijzen = st.Page(BASE_DIR / "benzineprijzen.py", title="Webscraper data - benzineprijzen")
dieselprijzen = st.Page(BASE_DIR / "dieselprijzen.py", title="Webscraper data - dieselprijzen")
scraper_landing = st.Page(BASE_DIR / "scraper_data.py", title="Webscraper data - brandstofprijzen in Nederland: inzicht over tijd en type pomp")
homepage = st.Page(BASE_DIR / "home.py", title="Oorschot.tech")

st_pages = {"Oorschot.tech" : [homepage], "Project: Fuel Prices": [scraper_landing, benzineprijzen, dieselprijzen]}

page = st.navigation(pages=st_pages, position="top")

page.run()

