import streamlit as st
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT

# Chart instance
charts = StreamlitCharts()

# Webapp - Benzineprijzen
st.title("Ontwikkeling van diesel prijzen in Nederland.")
st.divider()

st.header("Gemiddelde, minimale en maximale diesel prijs per soort tankstation", divider=None)

with st.container(border=True):

    st.subheader("Diesel prijzen bij budget tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="diesel", p_type="budget", min_scale=1.40, max_scale=2.10), use_container_width=True)

with st.container(border=True):
    st.subheader("Diesel prijzen bij premium tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="diesel", p_type="budget", min_scale=1.40, max_scale=2.10), use_container_width=True) # To change to premium gasstations.

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)
