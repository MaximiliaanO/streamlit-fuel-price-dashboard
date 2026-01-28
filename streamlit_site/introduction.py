import streamlit as st
from content_text.text import STREAMLITTEXT
from data.charts import StreamlitCharts

st.title("Brandstofprijzen in Nederland: inzicht over tijd en type pomp")

st.markdown(STREAMLITTEXT.INTRODUCTIEPAGE_INTRO)
st.space()

with st.container(border=True):
    st.header("Aantal pompstations per type:", text_alignment="center")
    st.space(size="medium")
    charts = StreamlitCharts()
    charts.type_chart()