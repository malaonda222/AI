'''Simula il lancio di due dadi D6 e restituisci in output una lista 
con n = 100 risultati della somma dei due dadi'''

import random 

n: int = int(input("Inserisci il numero di lanci: "))

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

lista_somma = []

for _ in range(n):
    d1 = random.choice(dado1)
    d2 = random.choice(dado2)
    lista_somma.append(d1 + d2)

print(len(lista_somma))
print(lista_somma)
print(min(lista_somma))
print(max(lista_somma))

# oppure 

somma = []

for _ in range(n):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    somma.append(d1 + d2)

print(somma)


