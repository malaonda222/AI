import math 
'''Esercizio 10: Distribuzione Binomiale (Lancio di una moneta)
Testo: Lanciando una moneta 10 volte, qual è la probabilità di ottenere esattamente 6 teste?'''

'''
n = 10 
k = 6 
p = 1/2 
'''

'''
P(X = k) = (n k) * p**k * (1 - p)**(n-k)

P(x = 6) = 10! / (6! * 4!) * (n - k)! * p**k * (1 - p)**(n-k)

210 * (0.5)**10 = 240 * 1/1024 = 0.205

P(x) = 20.5%
'''

def binom(n: int, p: float, k: int):
    n_su_k = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    p_k = p**k
    insuccesso = (1 - p) ** (n - k)
    return n_su_k * p_k * (insuccesso)

print(binom(10, 0.5, 6))


#oppure con comb

def binomiale(n, p, k):
    coeff_binom = math.comb(n, k)
    p_k = p**k 
    insuccesso = (1 - p)** (n - k)
    return coeff_binom * p_k * insuccesso

print(binomiale(10, 0.5, 6))



