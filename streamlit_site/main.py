import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).parent

benzineprijzen = st.Page(BASE_DIR / "benzineprijzen.py", title="Benzineprijzen")
dieselprijzen = st.Page(BASE_DIR / "dieselprijzen.py", title="Dieselprijzen")
scraper_landing = st.Page(BASE_DIR / "introduction.py", title="Introductie")
scraper_summary = st.Page(BASE_DIR / "prijzen_samenvatting.py", title="Samenvatting en analyse")
homepage = st.Page(BASE_DIR / "home.py", title="Over mij")

st_pages = {"Oorschot.tech" : [homepage], "Project: Fuel Prices": [scraper_landing, scraper_summary, benzineprijzen, dieselprijzen]}

page = st.navigation(pages=st_pages, position="top")

page.run()

