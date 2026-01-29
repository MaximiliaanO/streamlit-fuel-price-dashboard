from fastapi import FastAPI
from backend.rest_api.database.database import PostgresHandler
from backend.rest_api.database.db_queries import DB_QUERIES

db = PostgresHandler()
db.initialize_conn()

app = FastAPI(debug=True)

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/price-query")
def price_query(fuel_type : str, pump_type :str):
    dta = db.database_query(DB_QUERIES.price_query(fuel_type=fuel_type.lower(), pump_type=pump_type.lower()))
    return dta

@app.get("/median-average")
def median_average(fuel_type : str):
    dta = db.database_query(DB_QUERIES.MEDIAN_PRICE_QUERY(fuel_type=fuel_type))
    return dta

@app.get("/pumps-by-types")
def pumps_by_types():
    pumptypes = db.database_query(DB_QUERIES.PUMP_TYPE_QUERY)
    return pumptypes