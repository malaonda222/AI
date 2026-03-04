'''Esercizio 5: Teorema di Bayes (Produzione industriale)
Testo: Tre macchine, M1, M2 e M3, producono rispettivamente il 50%, 30% e 20% dei pezzi totali di una fabbrica. 
Le percentuali di pezzi difettosi sono del 2% per M1, 3% for M2 e 4% for M3. Scegliendo un pezzo a caso, questo risulta difettoso. 
Qual è la probabilità che sia stato prodotto dalla macchina M1?'''

M1 = 0.50 #P(D|M1) = 0.02 
M2 = 0.30 #P(D|M2) = 0.03
M3 = 0.20 #P(D|M3) = 0.04

# P(B|A) = P(A|B) * P(B) / P(A)
# P(M1|D) = P(D|M1) * P(M1) / P(D)

#P(D) = P(D|M1) * P(M1) + P(D|M2) * P(M2) + P(D|M3) * P(M3)
#P(D) = 0.02 * 0.50 + 0.03 * 0.30 + 0.04 * 0.20 = 0.01 + 0.009 + 0.008 = 0.027 

#P(M1|D) = 0.02 * 0.50 / 0.027 = 0.3704 


