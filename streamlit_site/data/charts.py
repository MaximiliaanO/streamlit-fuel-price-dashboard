import streamlit as st
import pandas as pd
import altair as alt
from data.db_queries import DB_QUERIES
from data.db_queries import DB_QUERIES
from data.database import PostgresHandler

class StreamlitCharts():
    def __init__(self):
        #init db connection
        self.db = PostgresHandler()
        self.db.initialize_conn()
    
    def min_max_avg_chart(self, f_type: str, p_type: str, min_scale:float, max_scale:float):
        # Budget branstofpompen dataframe & chart benzine
        dta = self.db.database_query(DB_QUERIES.price_query(fuel_type=f"{f_type}", pump_type=f"{p_type}"))
        df = pd.DataFrame(dta, columns=("Datum", "minimum price", "average price", "maximum price"))
        price_cols = ["minimum price", "average price", "maximum price"]
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
    
    def type_chart(self):
        dta = self.db.database_query(DB_QUERIES.PUMP_TYPE_QUERY)
        clean = [data for tpl in dta for data in tpl if data != None]
        df = pd.DataFrame(data=clean)
        df.index = ["budget", "premium"]
        chart = st.bar_chart(df, x_label="Station type")
        return chart