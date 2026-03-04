import math 
import scipy.stats as ss

def binom(n: int, p: float, k: int):
    n_su_k = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    p_k = p**k
    insuccesso = (1 - p) ** (n - k)
    return n_su_k * p_k * (insuccesso)

print(binom(10, 0.5, 3))


def binomiale(n: int, p: float, k: int):
    return ss.binom.pmf(k, n, p)

print(binomiale(5, 0.6, 3))

