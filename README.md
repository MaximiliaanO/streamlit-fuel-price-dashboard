# Fuel Prices Dashboard

This project contains the source code for a personal website with a data analysis about fuel prices in the Netherlands.
The project visualises the data from the data pipeline I created earlier in December 2025.

The website consists of an introduction page about myself and several project pages presenting interactive data visualisations.


---

## Project: Fuel Prices

The project consists of two parts.
First, a data pipeline that collects and processes fuel rpcie data (available [here](https://github.com/MaximiliaanO/Data-Pipeline---Fuel-Prices)). 
Second, a set of interactive visualisations built with Streamlit.

The project page contains:

- An introduction to the dataset and an overview of the number of *budget* versus *premium* fuel stations.
- A summary page showing average and median prices, split by fuel type and station type.
- Time series visualisations of minimum, average, and maximum prices per station type (budget or premium), split by fuel type.

---

## Architecture:

```
    Streamlit website (VPS)
    |
    |HTTP (private)
    |
    v
    FastAPI backend (home server)
    |
    |
    v
    PostgreSQL database (home server)
```

## Tech stack

- Python
- PostgreSQL
- FastAPI
- Streamlit
- Pandas
- Altair
- SQL
- Docker
- Wireguard

---

## Status

This project is being actively developed. Future versions will focus on further optimisations, such as introducing asynchronous I/O.