'''Esercizio 4: Probabilità Totale e Condizionata (Urne)
Testo: Ci sono due urne. L'urna A contiene 3 palline rosse e 2 blu. L'urna B contiene 1 pallina rossa e 4 blu. 
Si sceglie un'urna a caso e si estrae una pallina. Qual è la probabilità che la pallina estratta sia rossa?'''

urna_a = ["r", "r", "r", "b", "b"] #3/5
urna_b = ["r", "b", "b", "b", "b"] #1/5

# P(rossa) = P(rossa|urna_a) * P(urna_a) + P(rossa|urna_b) * P(urna_b)
# P(rossa) = 3/5 * 1/2 + 1/5 * 1/2 = 0.4 


'''
Risultato:
P(rossa) = P(rossa|urna_a) * P(urna_a) + P(rossa|urna_b) * P(urna_b)
'''
