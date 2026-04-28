CREATE TABLE dim_data (
    data_sk SERIAL PRIMARY KEY,
    data DATE UNIQUE,
    anno INT,
    mese INT,
    giorno INT,
    trimestre INT,
    mese_nome TEXT,
    giorno_settimana INT,
    giorno_nome TEXT
);

INSERT INTO dim_data (data, anno, mese, giorno, trimestre, 
mese_nome, giorno_settimana, giorno_nome)
SELECT
 d,
 EXTRACT(YEAR FROM d),
 EXTRACT(MONTH FROM d),
 EXTRACT(DAY FROM d),
 EXTRACT(QUARTER FROM d),
 TO_CHAR(d, 'Month'),
 EXTRACT(DOW FROM d),
 TO_CHAR(d, 'Day')
FROM generate_series('2020-01-01'::date, 
 '2026-12-31'::date, 
 '1 day'::interval) AS d; 

