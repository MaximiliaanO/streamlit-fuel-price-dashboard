import streamlit as st
from data.charts import StreamlitCharts
from text_pages.text import STREAMLITTEXT

# Chart instance
charts = StreamlitCharts()

# Webapp - Benzineprijzen
st.title("Ontwikkeling van diesl prijzen in Nederland.")
st.markdown(body=STREAMLITTEXT.INTRO)
st.divider()

st.header("Gemiddelde, minimale en maximale diesel prijs per soort tankstation", divider=None)

with st.container(border=True):

    st.subheader("Diesel prijzen bij budget tankstations:")
    st.altair_chart(charts.bgt_diesel_chart(), use_container_width=True)

with st.container(border=True):
    st.subheader("Diesel prijzen bij premium tankstations:")
    st.altair_chart(charts.prem_diesel_chart(), use_container_width=True) # To change to premium gasstations.

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)
