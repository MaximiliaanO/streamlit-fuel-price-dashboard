import requests
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(".env/.env"))

def fetch_min_max_avg_data(fuel_type :str, pump_type: str):
    try:
        base_url = os.getenv("API_LOC")
        endpoint = f"price-query?fuel_type={fuel_type.lower()}&pump_type={pump_type.lower()}"
        url = base_url + endpoint
        res = requests.get(url=url)
        res.raise_for_status()
        dta = res.json()
        df = pd.DataFrame(dta, columns=("Datum", "Minimum", "Gemiddelde", "Maximum"))
        return df
    except Exception as e:
        if e == requests.HTTPError:
            #To add logger to log connection errors
            print(f'An HTTP error has ocurred: {e}')
            return e
        else:
            print(f'An error has ocurred {e}')
            return e
        
def fetch_avg_median_data(fuel_type : str):
    try:
        base_url = os.getenv("API_LOC")
        endpoint= f"median-average?fuel_type={fuel_type.lower()}"
        url = base_url + endpoint
        res = requests.get(url=url)
        res.raise_for_status()
        dta = res.json()
        df = pd.DataFrame(dta, columns=['Datum', 'Pomp type', 'Gemiddelde', 'Mediaan'])
        return df
    except Exception as e:
        if e == requests.HTTPError:
            #To add logger to log connection errors
            print(f'An HTTP error has ocurred: {e}')
            return e
        else:
            print(f'An error has ocurred {e}')
            return e
        
def fetch_pump_types():
    try:
        base_url = os.getenv("API_LOC")
        endpoint = "pumps-by-types"
        url = base_url + endpoint
        res = requests.get(url=url)
        res.raise_for_status()
        dta = res.json()
        clean = [data for tpl in dta for data in tpl if data != None]
        df = pd.DataFrame(data=clean)
        df.index = ["budget", "premium"]
        return df
    except Exception as e:
        if e == requests.HTTPError:
            #To add logger to log connection errors
            print(f'An HTTP error has ocurred: {e}')
            return e
        else:
            print(f'An error has ocurred {e}')
            return e