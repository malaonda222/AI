import random 
from collections import Counter 

n_lanci = 100000
somma = []
for n in range(n_lanci):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    somma.append(d1 + d2)

# print(somma)

frequenza_7 = somma.count(7)
print(f"Simulazione", frequenza_7 / n_lanci)
print("Risultato probabilità classica", 6/36)





# d: dict = {}
# for num in somma:
#     if num not in d:
#         d[num] = 1
#     else:
#         d[num] += 1
# print(d)



