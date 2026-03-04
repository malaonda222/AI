semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
valori = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

mazzo = [(valore, seme) for valore in valori for seme in semi]
print(f"mazzo completo: {len(mazzo)} carte\n")

carte_re = [c for c in mazzo if c[0] == 'K']
carte_cuori = [c for c in mazzo if c[1] == 'Cuori']
carte_re_cuori = [c for c in mazzo if c[0] == 'K' and c[1] == 'Cuori']

print(f"Carte Re: {len(carte_re)}")
print(f"Carte di Cuori: {len(carte_cuori)}")
print(f"Carte Re di Cuori: {carte_re_cuori}\n")

#calcolo delle probabilità 
p_re = len(carte_re) / len(mazzo)
p_cuori = len(carte_cuori) / len(mazzo)
p_re_cuori = len(carte_re_cuori) / len(mazzo)

#probabilità condizionale
p_re_dato_cuori = p_re_cuori / p_cuori 

print("Probabilità\n")
print(f"P(Re) = {p_re:.2f}")
print(f"P(Cuori) = {p_cuori:.2f}")
print(f"P(Re di Cuori) = {p_re_cuori:.2f}")
print(f"\nP(Re|Fiori) = P(Re di Cuori) / P(Cuori) = {p_re_dato_cuori:.2f}")
print(f"\nInterpretazione: Sapendo che la carte è di cuori,")
print(f"La probabilità che sia un Re è del {p_re_dato_cuori:.2%}")
