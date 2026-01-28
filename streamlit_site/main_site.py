import streamlit as st
from charts import StreamlitCharts
from text import STREAMLITTEXT

# Chart instance
charts = StreamlitCharts()

# Webapp
st.title("Ontwikkeling van brandstof prijzen in Nederland.")
st.markdown(body=STREAMLITTEXT.INTRO)
st.divider()

st.header("Gemiddelde, minimale en maximale benzine prijs per soort tankstation", divider=None)

with st.container(border=True):

    st.subheader("Benzine prijzen bij budget tankstations:")
    st.altair_chart(charts.bgt_gas_chart(), use_container_width=True)

with st.container(border=True):
    st.subheader("Benzine prijzen bij premium tankstations:")
    st.altair_chart(charts.prem_gas_chart(), use_container_width=True) # To change to premium gasstations.

st.markdown(body=STREAMLITTEXT.GAS_COMMENT)
