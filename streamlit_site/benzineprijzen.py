import streamlit as st
from data.charts import StreamlitCharts
from text_pages.text import STREAMLITTEXT

# Chart instance
charts = StreamlitCharts()

# Webapp - Benzineprijzen
st.title("Ontwikkeling van benzine prijzen in Nederland.")
st.markdown(body=STREAMLITTEXT.INTRO)
st.divider()

st.header("Gemiddelde, minimale en maximale benzine prijs per soort tankstation", divider=None)

with st.container(border=True):

    st.subheader("Benzine prijzen bij budget tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="budget", min_scale=1.70, max_scale=2.40), use_container_width=True)

with st.container(border=True):
    st.subheader("Benzine prijzen bij premium tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="premium", min_scale=1.70, max_scale=2.40), use_container_width=True)

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)
