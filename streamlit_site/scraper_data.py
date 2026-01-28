import streamlit as st
from text_pages.text import STREAMLITTEXT
from data.charts import StreamlitCharts

st.title("Brandstofprijzen in Nederland: inzicht over tijd en type pomp")

st.markdown(STREAMLITTEXT.MAIN_INTRO)
st.space()

with st.container(border=True):
    st.header("Types pompstations", text_alignment="center")
    st.space(size="medium")
    charts = StreamlitCharts()
    charts.type_chart()