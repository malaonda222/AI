# Spazio campionario 
S = {1, 2, 3, 4, 5, 6}

# Definizione degli eventi 
A = {1, 2, 3} #evento A: ottenere 1, 2 o 3
B = {4, 5, 6} #evento B: ottenere 4, 5 o 6
C = {3, 6} #evento C: ottenere 3 o 6 

print("Spazio campionario S =", S)
print("\nEventi definiti:")
print(f"A = {A} (numeri <= 3)")
print(f"B = {B} (numeri >= 4)")
print(f"C = {C} (numeri multipli di 3 - 3 compreso)")


def probabilita(evento, spazio_campionario):
    '''Calcola P(evento) = |evento| / |spazio_campionario'''
    return len(evento)/len(spazio_campionario)

P_A = probabilita(A, S)
P_B = probabilita(B, S)
P_C = probabilita(C, S)
P_S = probabilita(S, S)
P_vuoto = probabilita(set(), S)

print("=" * 60)
print("VERIFICA DEGLI ASSIOMI DELLA PROBABILITÀ")
print("=" * 60)


#ASSIOMA 1: non negatività
print("\n[Assioma 1] Non-Negatività: P(E) >= 0")
print(f"P(A) = {P_A:.3f} >= 0 ✓")
print(f"P(B) = {P_B:.3f} >= 0 ✓")
print(f"P(C) = {P_C:.3f} >= 0 ✓")


#ASSIOMA 2: normalizzazione
print(f"\n[Assioma 2] Normalizzazione: P(S) = 1")
print(f"P(S) = {P_S:.3f} = 1 ✓")


#ASSIOMA 3: 

# Caso 1: additività per eventi disgiunti 
print(f"\n[Assioma 3] Additività per eventi disgiunti")
print(f"A e B sono disgiunti: A ∩ B = {A.intersection(B)}")
P_A_union_B = probabilita(A.union(B), S)
print(f"P(A u B) = {P_A_union_B:.3f}")
print(f"P(A) + P(B) = {P_A:.3f} + {P_B:.3f} = {P_A + P_B:.3f}")
print(f"--> P(A u B) = P(A) + P(B) (A e B sono disgiunti)")

#Caso 2: additività per eventi non disgiunti (A e C)
print(f"\nA e C non sono disgiunti: A ∩ C = {A.intersection(C)}")
P_A_union_C = probabilita(A.union(C), S)
P_A_inter_C = probabilita(A.intersection(C), S)
print(f"P(A u C) = {P_A_union_C:.3f}")
print(f"P(A) + P(C) - P(A ∩ C) = {P_A:.3f} + {P_C:.3f} - {P_A_inter_C:.3f} = {P_A + P_C + P_A_inter_C:.3f}")
print("--> P(A u C) = P(A) + P(C) - P(A ∩ C) (a e B non disgiunti)")
