import math 

'''Esercizio 11: Distribuzione di Poisson (Arrivi in un negozio)
Testo: In un negozio entrano in media 3 clienti ogni 10 minuti. 
Qual è la probabilità che in 10 minuti entrino esattamente 5 clienti?'''

'''
k = 5 
lambda = 3 

P(x = k) = (lambda ** 5 * esponenziale ** (-lambda)) / k! 

P(x = 5) = ((3**5) * (esponenziale**(-3))) / 5! = 12.098/120 = 0.1008 = 10.08 
'''

k = 5 
lambda_val = 3

probabilita = ((lambda_val ** k) * math.exp(-lambda_val)) / math.factorial(k)
print(f"{probabilita:2f}")

