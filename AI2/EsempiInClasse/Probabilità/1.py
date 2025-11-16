import numpy as np
import matplotlib.pyplot as plt
from collections import Counter 

s_due_dadi = {[i, j] for i in range(1, 7) for j in range(1, 7)}

print(f"Spazio campionario per due dadi:")
print(f"Cardinalità |S| = {len(s_due_dadi)}")
print(f"\Primi 10 elementi: {s_due_dadi[:10]}")
print(f"\nUltimi 10 elementi: {s_due_dadi[-10:]}")

s_dado = {1, 2, 3, 4, 5, 6}
print(f"Spazio campionario S = {s_dado}")
print(f"Cardinalità |S| = {len(s_dado)}")

n_lanci = 1000
lanci = np.random.randint(1, 7, size=n_lanci)

frequenze = Counter(lanci)
print(f"\nFrequenze assolute dopo {n_lanci} lanci:")
for faccia in sorted(frequenze.keys()):
    freq_rel = frequenze[faccia] / n_lanci 
    print(f"    Faccia {faccia}: {frequenze[faccia]} volte (frequenza relativa: {freq_rel:.3f})")


# Visualizzazione delle frequenze 
plt.figure(figsize=(10,6))
facce = sorted(frequenze.keys())
conteggi = [frequenze[f] for f in facce]

plt.bar(facce, conteggi, color = 'steelblue')
plt.legend()
plt.grid(axis='y', aplha= 0.3)
plt.show()
