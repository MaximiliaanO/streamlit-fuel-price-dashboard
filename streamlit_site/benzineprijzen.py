import streamlit as st
from data.charts import StreamlitCharts
from content_text.text import STREAMLITTEXT

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
    st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="budget", min_scale=1.70, max_scale=2.30), use_container_width=True)
    #st.space(size='small')
    st.divider()
    st.subheader("Benzine prijzen bij premium tankstations:")
    st.altair_chart(charts.min_max_avg_chart(f_type="benzine", p_type="premium", min_scale=1.70, max_scale=2.30), use_container_width=True)

st.markdown(body=STREAMLITTEXT.FUEL_COMMENT)

st.divider()


