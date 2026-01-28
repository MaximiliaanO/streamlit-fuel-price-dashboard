import streamlit as st
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT

charts = StreamlitCharts()

bord = True
benzine_scale = [1.85, 2.10] # minimum, maximum
diesel_scale = [1.60, 1.90] # minimum, maximum

st.header("Gemiddelde en mediaan brandstofprijzen per soort tankstation:")
with st.container(border=bord):
    st.subheader("Benzine:")
    charts.avg_median(f_type='benzine', min_scale=benzine_scale[0], max_scale=benzine_scale[1])
    st.divider()
    st.subheader("Diesel:")
    charts.avg_median(f_type='diesel', min_scale=diesel_scale[0], max_scale=diesel_scale[1])

st.subheader("Analyse:")
st.markdown(STREAMLITTEXT.PRIJZEN_SAMENVATTING_COMMENT)