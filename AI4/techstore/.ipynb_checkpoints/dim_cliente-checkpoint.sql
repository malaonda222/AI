CREATE TABLE dim_cliente (
  cliente_sk SERIAL PRIMARY KEY,
  cliente_id INT UNIQUE,
  nome TEXT,
  cognome TEXT,
  citta TEXT,
  regione TEXT,
  data_nascita DATE,
  eta INT,
  fascia_eta TEXT
); 

INSERT INTO dim_cliente 
(cliente_id, nome, cognome, 
 citta, regione)
SELECT *
FROM dblink(
  'dbname=techstore 
   user=postgres 
   password=postgres',
  'SELECT cliente_id, nome, 
          cognome, citta, regione 
   FROM clienti'
) AS t(cliente_id INT, 
       nome TEXT, 
       cognome TEXT, 
       citta TEXT, 
       regione TEXT); 