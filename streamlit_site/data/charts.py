import pandas as pd
import altair as alt
from data.db_queries import DB_QUERIES
from data.database import PostgresHandler

class StreamlitCharts():
    def __init__(self):
        #init db connection
        self.db = PostgresHandler()
        self.db.initialize_conn()
    
    def bgt_gas_chart(self):
        # Budget branstofpompen dataframe & chart benzine
        bgt_dta = self.db.get_price_data_gas(DB_QUERIES.GAS_QUERY_BUDGET)
        bdt_g_df = pd.DataFrame(bgt_dta, columns=("Datum", "minimum price", "average price", "maximum price"))
        bgt_g_price_cols = ["minimum price", "average price", "maximum price"]

        # Chart
        bgt_g_chart = (
            alt.Chart(bdt_g_df)
            .transform_fold(
                bgt_g_price_cols,
                as_=["type", "price"]
            )
            .mark_line(point=True)
            .encode(
                x=alt.X("Datum:T", title="Datum"),
                y=alt.Y(
                    "price:Q",
                    title="Prijs (€)",
                    scale=alt.Scale(domain=[1.65, 2.4]),
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
        return bgt_g_chart

    def prem_gas_chart(self):
        # Premium brandstofpompen dataframe & chart benzine
        prem_g_dta = self.db.get_price_data_gas(DB_QUERIES.GAS_QUERY_PREMIUM)
        prem_g_df = pd.DataFrame(prem_g_dta, columns=("Datum", "minimum price", "average price", "maximum price"))
        prem_g_price_cols = ["minimum price", "average price", "maximum price"]

        # Chart
        prem_g_chart = (
            alt.Chart(prem_g_df)
            .transform_fold(
                prem_g_price_cols,
                as_=["type", "price"]
            )
            .mark_line(point=True)
            .encode(
                x=alt.X("Datum:T", title="Datum"),
                y=alt.Y(
                    "price:Q",
                    title="Prijs (€)",
                    scale=alt.Scale(domain=[1.65, 2.4]),
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
        return prem_g_chart
