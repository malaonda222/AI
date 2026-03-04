import matplotlib.pyplot as plt 
from scipy.stats import bernoulli, binom 
import numpy as np 

'''Distribuzione di Bernoulli'''

p = 0.3 #probabilità di successo 
x_bern = [0, 1]
y_bern = bernoulli.pmf(x_bern, p)

plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.stem(x_bern, y_bern)
plt.xticks([0, 1])
plt.xlabel('x')
plt.ylabel('P(X=x)')
plt.title('Distribuzione di Bernoulli (p=0.3)')
plt.ylim(0, 1)


'''Distribuzione binomiale'''
n = 10

x_binom = np.arange(0, n + 1)
y_binom = binom.pmf(x_binom, n, p)
plt.subplot(1, 2, 2)
plt.stem(x_binom, y_binom)
plt.xtick(range(0, n+1))
plt.xlabel('Numero di successi')
plt.ylbale('P(X=x)')
plt.title(f'Distribuzione Binomiale (n={n}, p={p})')
plt.ylim(0, max(y_binom)+0.05)
plt.tight_layout()
plt.show()


