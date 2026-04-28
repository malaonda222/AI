'''Esercizio 1: KPI Generali'''

--Numero totale dei noleggi
SELECT COUNT(*)
FROM dw.fact_noleggi 

--Durata media dei noleggi
SELECT round(avg(durata_minuti)::numeric, 2)
FROM dw.fact_noleggi 

--Distanza media percorsa
SELECT round(avg(distanza_km)::numeric, 2)
FROM dw.fact_noleggi


'''Esercizio 2: Analisi Temporale'''

--Numero di noleggi per anno
SELECT dt.anno, COUNT(*)
FROM dw.fact_noleggi fn
JOIN dw.dim_tempo dt ON fn.tempo_key = dt.tempo_key
GROUP BY dt.anno

--Numero di noleggi per giorno della settimana
SELECT dt.giorno_settimana, dt.nome_giorno, COUNT(*)
FROM dw.fact_noleggi fn
JOIN dw.dim_tempo dt on fn.tempo_key = dt.tempo_key
GROUP BY dt.giorno_settimana, dt.nome_giorno 
ORDER BY dt.giorno_settimana


'''Esercizio 3: Analisi Geografica'''

--Trova le 10 città con più noleggi
SELECT dc.nome_sistema, COUNT(*) as num_noleggi 
FROM dw.fact_noleggi fn
JOIN dw.dim_citta dc on fn.citta_key = dc.citta_key
GROUP BY dc.nome_sistema
ORDER BY num_noleggi 
LIMIT 10

--Trova le 10 stazioni di partenza più popolari
SELECT ds.id_stazione, COUNT(*) as stazione_partenza
FROM dw.fact_noleggi fn
JOIN dw.dim_stazione ds on fn.stazione_partenza_key = ds.stazione_key 
GROUP BY ds.id_stazione
ORDER BY stazione_partenza DESC
LIMIT 10


'''Esercizio 4: Analisi degli Utenti'''

--Numero di noleggi per tipo di abbonamento
SELECT du.tipo_abbonamento_corrente, count(*)
FROM dw.fact_noleggi fn
JOIN dw.dim_utente du ON fn.utente_key = du.utente_key 
GROUP BY du.tipo_abbonamento_corrente 

--Numero di noleggi per fascia d'età
SELECT du.fascia_eta, count(*)
FROM dw.fact_noleggi fn
JOIN dw.dim_utente du ON fn.utente_key = du.utente_key 
GROUP BY du.fascia_eta


'''Esercizio 5: Analisi delle Biciclette'''

--Analizza e numero di noleggi per tipo di propulsione
SELECT b.propulsione, COUNT(*)
FROM dw.fact_noleggi fn
JOIN dw.dim_bicicletta b ON fn.bicicletta_key = b.bicicletta_key 
GROUP BY b.propulsione 

--Durata e distanza media per tipo di propulsione
SELECT b.propulsione, AVG(fn.durata_minuti), AVG(fn.distanza_km)
FROM dw.fact_noleggi fn
JOIN dw.dim_bicicletta b ON fn.bicicletta_key = b.bicicletta_key 
GROUP BY b.propulsione