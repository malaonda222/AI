'''Esercizio 9 - Probabilità totale con più rami (canali marketing)
Testo
Un’azienda riceve richieste da tre canali:
    • Web: 50% delle richieste, tasso di conversione 4%
    • Telefono: 30% delle richieste, tasso di conversione 6%
    • Referral: 20% delle richieste, tasso di conversione 10%
Domande
    1. Qual è la probabilità complessiva che una richiesta diventi cliente?
    2. Dato che un nuovo cliente è stato acquisito, qual è la probabilità che provenga dal canale Referral?'''


''' P(Web) Web 0.5              P(C|Web) tc: 0.04 
    P(Telefono) Telefono 0.3    P(C|Telefono) tc: 0.06
    P(Referral) Referral 0.2    P(C|Referral) tc: 0.1
    
1. 
P(Totale) = P(C|Web) * P(Web) + P(C|Telefono) * P(Telefono) + P(C|Referral) * P(Referral) 
= 0.04 * 0.5 + 0.06 * 0.3 + 0.1 * 0.2 = 0.02 + 0.018 + 0.02 = 0.058 = 5,8%

2. 
P(Referral|C) = P(Referral|C) * P(C) / P(Totale) = 0.1 * 0.2 / 0.058 = 0.3448

'''