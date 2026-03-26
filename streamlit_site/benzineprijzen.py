import streamlit as st
import os
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env/.env"))

min_s = os.getenv("MIN_SCALE_B")
max_s = os.getenv("MAX_SCALE_B")

#border
bord = True

# Chart instance
charts = StreamlitCharts()

# Webapp - Benzineprijzen
st.title("Ontwikkeling van benzine prijzen in Nederland.")
st.divider()



st.header("Gemiddelde, minimale en maximale benzine prijs per soort tankstation", divider=None)

with st.container(border=bord):

    st.subheader("Benzine prijzen bij budget tankstations:")
    try:
        st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="budget", min_scale=min_s, max_scale=max_s), use_container_width=True)
    except Exception as e:
        st.write(f"An error has ocurred!")
    #st.space(size='small')
    st.divider()
    st.subheader("Benzine prijzen bij premium tankstations:")
    try:
        st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="premium", min_scale=min_s, max_scale=max_s), use_container_width=True)
    except Exception as e:
        st.write(f"An error has ocurred!")

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)

st.divider()


