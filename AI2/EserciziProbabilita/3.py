'''Esercizio 3: Teorema di Bayes (Test diagnostico)
Testo: Un test per una malattia ha un'accuratezza del 99% (identifica 
correttamente sia i malati che i sani). La malattia colpisce lo 0.5% della 
popolazione. Se una persona risulta positiva al test, qual è la probabilità 
che sia effettivamente malata?'''

'''P(Malato) = 0.005
    P(Sano) = 0.995
    P(Positivo|Malato) = 0.99
    P(Positivo|Sano) = 0.01
    
    P(Malato|Positivo) = P(Positivo|Malato) * P(Malato) / P(Positivo)

    P(Positivo) = P(Positivo|Malato) * P(Malato) + P(Positivo|Sano) * P(Sano) = 0.0149

    P(Malato|Positivo) = 0.99 * 0.005 / 0.0149 = 0.3322 '''

#P(Malato|Positivo) = P(Positivo|Malato) * P(Malato) / P(Positivo)

#P(Positivo) = P(Positivo|Malato) * P(Malato) + P(Positivo|Sano) * P(Sano)

# P(Malato) = 0.005
# P(Positivo | Malato) = 0.99 
# P(Sano) = 0.995
# P(Positivo | Sano) = 0.01

# P(Positivo) = 0.99 * 0.005 + 0.01 * 0.995 = 0.00495 + 0.00995 = 0.0149

# P(Malato|Positivo) = (0.99 * 0.005) / 0.0149 = 0.00495 / 0.0149 = 0.3322
