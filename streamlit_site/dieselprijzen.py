import streamlit as st
import os
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env/.env"))

min_s = os.getenv("MIN_SCALE_D")
max_s = os.getenv("MAX_SCALE_D")

# Chart instance
charts = StreamlitCharts()

# Webapp - Benzineprijzen
st.title("Ontwikkeling van diesel prijzen in Nederland.")
st.divider()

st.header("Gemiddelde, minimale en maximale diesel prijs per soort tankstation", divider=None)

with st.container(border=True):

    st.subheader("Diesel prijzen bij budget tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="diesel", p_type="budget", min_scale=min_s, max_scale=max_s), use_container_width=True)

with st.container(border=True):
    st.subheader("Diesel prijzen bij premium tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="diesel", p_type="budget", min_scale=min_s, max_scale=max_s), use_container_width=True) # To change to premium gasstations.

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)
