import streamlit as st
import os
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env/.env"))

charts = StreamlitCharts()

bord = True
benzine_scale = [os.getenv("SUMM_MIN_B"), os.getenv("SUMM_MAX_B")] # minimum, maximum
diesel_scale = [os.getenv("SUMM_MIN_D"), os.getenv("SUMM_MAX_D")] # minimum, maximum

st.header("Gemiddelde en mediaan brandstofprijzen per soort tankstation:")
with st.container(border=bord):
    st.subheader("Benzine:")
    charts.avg_median(f_type='benzine', min_scale=benzine_scale[0], max_scale=benzine_scale[1])
    st.divider()
    st.subheader("Diesel:")
    charts.avg_median(f_type='diesel', min_scale=diesel_scale[0], max_scale=diesel_scale[1])

st.subheader("Analyse:")
st.markdown(STREAMLITTEXT.PRIJZEN_SAMENVATTING_COMMENT)