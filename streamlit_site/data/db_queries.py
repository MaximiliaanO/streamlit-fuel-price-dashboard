class DB_QUERIES:
    def price_query(fuel_type, pump_type):
        PRICE_QUERY = f"""
        WITH daily_prices AS(
            SELECT
                date_trunc('day', fp.date_time) AS price_date,
                fp.fuel_type,
                fp.price,
                ds.brand,
                    CASE
                        WHEN ds.brand = 'de-haan' OR ds.brand = 'esso-express' OR ds.brand = 'desimpel' THEN 'budget'
                        WHEN ds.brand = 'extern' THEN 'unknown'
                        ELSE 'premium'
                    END AS classification
            FROM 
                fact_prices AS fp
                LEFT JOIN dim_stations ds ON fp.id = ds.id
            ORDER BY 
                fp.date_time DESC
            )
        SELECT
            dp.price_date,
            ROUND(MIN(dp.price)::NUMERIC, 3)::FLOAT AS bgt_gas_daily_min,
            ROUND(AVG(dp.price)::NUMERIC, 3)::FLOAT AS bgt_gas_daily_avg,
            ROUND(MAX(dp.price)::NUMERIC, 3)::FLOAT AS bgt_gas_daily_max
        FROM daily_prices AS dp
        WHERE dp.classification = '{pump_type}' AND dp.fuel_type = '{fuel_type}'
        GROUP BY 
            dp.price_date,
            dp.classification,
            dp.fuel_type 
        ORDER BY 
            dp.price_date DESC
            """
        return PRICE_QUERY

    PUMP_TYPE_QUERY ="""
        WITH daily_prices AS(
            SELECT
                date_trunc('day', fp.date_time) AS price_date,
                fp.fuel_type,
                fp.price,
                fp.id,
                ds.brand,
                    CASE
                        WHEN ds.brand = 'de-haan' OR ds.brand = 'esso-express' OR ds.brand = 'desimpel' THEN 'budget'
                        WHEN ds.brand = 'extern' THEN 'unknown'
                        ELSE 'premium'
                    END AS classification
            FROM 
                fact_prices AS fp
                LEFT JOIN dim_stations ds ON fp.id = ds.id
            ORDER BY 
                fp.date_time DESC
        )
        SELECT
            CASE
                WHEN dp.classification = 'budget' THEN COUNT(DISTINCT dp.id)
                WHEN dp.classification = 'premium' THEN COUNT(DISTINCT dp.id)
            END
        FROM daily_prices AS dp
        GROUP BY
            dp.classification 
    """