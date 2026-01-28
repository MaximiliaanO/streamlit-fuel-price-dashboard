class DB_QUERIES:
    GAS_QUERY_BUDGET = """
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
        WHERE dp.classification = 'budget' AND dp.fuel_type = 'benzine'
        GROUP BY 
            dp.price_date,
            dp.classification,
            dp.fuel_type 
        ORDER BY 
            dp.price_date DESC
            """
    
    GAS_QUERY_PREMIUM = """
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
            WHERE dp.classification = 'premium' AND dp.fuel_type = 'benzine'
            GROUP BY 
                dp.price_date,
                dp.classification,
                dp.fuel_type 
            ORDER BY 
                dp.price_date DESC
            """