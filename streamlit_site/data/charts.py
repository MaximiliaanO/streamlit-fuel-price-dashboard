import streamlit as st
import altair as alt
from data.fetchdata import fetch_min_max_avg_data, fetch_avg_median_data, fetch_pump_types

class StreamlitCharts():
    def __init__(self):
        pass
    
    def min_max_avg_chart(self, f_type: str, p_type: str, min_scale:float, max_scale:float):
        df = fetch_min_max_avg_data(fuel_type=f_type, pump_type=p_type)
        if type(df) == Exception:
            return st.write("An error has ocurred")
        else:
            price_cols = ["Minimum", "Gemiddelde", "Maximum"]
            scale = [min_scale, max_scale]

            # Chart
            chart = (
                alt.Chart(df)
                .transform_fold(
                    price_cols,
                    as_=["type", "price"]
                )
                .mark_line(point=True)
                .encode(
                    x=alt.X("Datum:T", title="Datum"),
                    y=alt.Y(
                        "price:Q",
                        title="Prijs (€)",
                        scale=alt.Scale(domain=scale),
                        axis=alt.Axis(format=".3f")
                    ),
                    color=alt.Color("type:N", title="Prijssoort"),
                    tooltip=[
                        alt.Tooltip("Datum:T", title="Datum"),
                        alt.Tooltip("type:N", title="Type"),
                        alt.Tooltip("price:Q", title="Prijs (€)", format=".3f")
                    ]
                )
            )
            return chart

    
    def avg_median(self, f_type: str, min_scale:float, max_scale:float):
        df = fetch_avg_median_data(fuel_type=f_type)
        scale = [min_scale, max_scale]

        df_long = df.melt(
            id_vars=["Datum", "Pomp type"],
            value_vars=["Gemiddelde", "Mediaan"],
            var_name="Statistiek",
            value_name="Prijs"
        )

        chart = alt.Chart(df_long).mark_line().encode(
            x=alt.X("Datum:T", title="Datum"),
            y=alt.Y(
                "Prijs:Q",
                title="Prijs (€)",
                axis=alt.Axis(format=".3f"),
                scale=alt.Scale(domain=scale)
            ),
            color=alt.Color(
                "Pomp type:N",
                title="Pomp type",
                scale=alt.Scale(
                    domain=["premium", "budget"],
                    range=["#8ecae6", "#219ebc"]
                )
            ),
            strokeDash=alt.StrokeDash(
                "Statistiek:N",
                title="Statistiek",
                scale=alt.Scale(
                    domain=["Gemiddelde", "Mediaan"],
                    range=[[1, 0], [4, 4]]  # solid vs dashed
                )
            ),
            tooltip=[
                alt.Tooltip("Datum:T", title="Datum"),
                alt.Tooltip("Pomp type:N", title="Pomp type"),
                alt.Tooltip("Statistiek:N", title="Statistiek"),
                alt.Tooltip("Prijs:Q", title="Prijs (€)", format=".3f")
            ]
        )
        return st.altair_chart(chart, use_container_width=True)

    def type_chart(self):

        df = fetch_pump_types()
        chart = st.bar_chart(df, x_label="Station type")
        return chart