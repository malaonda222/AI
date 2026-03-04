'''Esercizio 7 - Probabilità condizionata inversa
Testo
    • Il 60% degli studenti studia Informatica.
    • Il 40% studia Economia.
    • Il 70% degli studenti di Informatica ha superato l’esame di Statistica.
    • Il 50% degli studenti di Economia ha superato l’esame di Statistica.
Domande
    1. Qual è la probabilità che uno studente scelto a caso abbia superato Statistica?
    2. Se uno studente ha superato Statistica, qual è la probabilità che studi 
    Informatica?
'''


'''1. 
    P(EsameStat) = P(EsameStat|Informatica) * P(Informatica) + P(EsameStat|Economia) * P(Economia) 
    = 0.70 * 0.60 + 0.50 * 0.40 = 0.42 + 0.2 = 0.62 = 62%'''

'''2. 
    P(Informatica|EsameStat) = P(EsameStat|Informatica) * P(Informatica) / P(EsameStat)
    = 0.42 / 0.62 = 0.68 = 62%
    '''