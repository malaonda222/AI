'''Uso la libreria scipy e stats e importo binom. Lo uso poi successivamente con i dati di riferimento.'''
from scipy.stats import binom

k = 3
n = 7
p = 1/6
risultato = binom.pmf(k, n, p)
print(f"{risultato:.3f}")


#oppure 
'''Uso la libreria scipy e uso sempre binom oppure uso comb dalla libreria math per calcola in modo manuale.'''
import scipy.stats as st 
import math 

p = st.binom.pmf(k=3, n=7, p=1/6)
print(f"{p:.3f}")

a = math.comb(7, 3) * ((1/6) **3) * ((5/6)**4)
print(f"{a:.3f}")


#oppure 
'''Uso la libreria scipy.special e in particolare mi prendo comb e dentro ci metto tutti i dati relativi.'''
from scipy.stats import binom
from scipy.special import comb

b = comb(7, 3) * ((1/6) **3) * ((5/6)**4)
print(f"{b:.3f}")