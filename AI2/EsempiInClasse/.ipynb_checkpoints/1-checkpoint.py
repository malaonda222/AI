from collections import Counter
import numpy as np

# Spazio campionario di due dati a sei facce
s_due_dadi = {[i, j] for i in range(1, 7) for j in range(1, 7)}

print("Spazio campionario per due dadi:")
print(f"Cardinalità di |S|: {len(s_due_dadi)}")
print(f"\nPrimi 10 elementi: {s_due_dadi[:10]}")
print(f"\nUltimi 10 elementi: {s_due_dadi[-10:]}")

# Spazio campionario per un dado 
s_dado = {1, 2, 3, 4, 5, 6}
print(f"Spazio campionario S = {s_dado}")
print(f"Cardinalità di S = {len(s_dado)}")

# Stabiliamo il numero di lanci 
n_lanci = 50
lanci = np.random.randint(1, 7, size=n_lanci)

# Stabiliamo le frequenze 
frequenze = Counter(lanci)
print(f"\nFrequenze assolute dopo {n_lanci} lanci:")
for faccia in sorted(frequenze.keys()):
    freq_rel = frequenze[faccia] / n_lanci
    print(f"Faccia {faccia}: {frequenze[faccia]} volte (frequenza relativa: {freq_rel:.3f})")

