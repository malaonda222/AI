# Spazio campionario
S = {1, 2, 3, 4, 5, 6}

# Definizione di eventi
A = {2, 4, 6} #numeri pari
B = {1, 2, 3} #numeri minori o uguali a 3
C = {5, 6} #numeri maggiori o uguali a 5

print(f"Spazio campionario: {S}")
print("\nEventi definiti:")
print(f"A -> {A} numeri pari")
print(f"B -> {B} numeri <= 3")
print(f"C -> {C} numeri >= 5")

# Unione (OR)
A_union_B = A.union(B)
print("\nUnione (A U B):")
print(f"A U B = {A_union_B}")
print(f"Significato: numeri pari o numeri <= 3")


# Intersezione (AND)
A_inter_B = A.intersection(B)
print("\nIntersezione (A ∩ B):")
print(f"A ∩ B = {A_inter_B}")
print("Significato: numeri pari e minori o uguali a 3")


# Complemento (NOT)
A_complement = S.difference(A)
print("\nComplemento di A:")
print(f"Aᶜ = {A_complement}")
print("Significato: numeri non pari (dispari)")


#Verifica che A e C siano disgiunti 
A_inter_C = A.intersection(C)
print("\nVerifica disgiunzione:")
print(f"A ∩ B = {A_inter_C}")
if len(A_inter_C) == 0:
    print("A e C sono disgiunti (non hanno elementi in comune)")
else:
    print("A e C non sono disgiunti")

