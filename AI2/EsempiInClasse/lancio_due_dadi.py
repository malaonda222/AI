def probabilita_condizionale(p_a_inter_b, p_b):
    if p_b == 0:
        raise ValueError("P(B) non può essere zero")
    return p_a_inter_b / p_b

print("Calcolo della probabilità condionale P(A|B)")
p_a_inter_b = float(input("Inserisci P(A n B): "))
p_b = float(input("Inserisci P(B): "))

p_a_dato_b = probabilita_condizionale(p_a_inter_b, p_b)

print("\nRisultato: ")
print(f"P(A|B) = {p_a_dato_b:.4f} -> {p_a_dato_b:.2f}")
print(f"P(B) = {p_b:.3f} -> {p_b:.2f}")
print(f"Interpretazione: sapendo che B è avvenuto, la probabilità che si verifichi anche A è {p_a_dato_b:.2f}")
