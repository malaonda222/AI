# def probabilità_condizionata(p_veg_inter_ta, p_ta):
#     if p_ta == 0:
#         raise ValueError("Errore, P(ta) non può essere negativa")
#     return p_veg_inter_ta / p_ta 

# ristorante = {
#         "vegetariano": {
#             "tot_veg": 90,
#             "takeaway": 54
#         },
#         "carne": {
#             "tot_carne": 160,
#             "takeaway": 56
#         },
#         "pesce": {
#             "tot_pesce": 50,
#             "takeaway": 20
#         },
#         "totale": {
#             "tot_totale": 300,
#             "tot_ta": 130
#         }
# }

# # P(Intersezione vegetariani e takeaway) / totale ordini
# p_veg_inter_ta = ristorante["vegetariano"]["takeaway"] / ristorante["totale"]["tot_totale"]

# # P(Takeaway totali) / totale ordini 
# p_ta = ristorante["totale"]["tot_ta"] / ristorante["totale"]["tot_totale"]

# # P(veg|takeaway)
# p_veg_dato_ta = probabilità_condizionata(p_veg_inter_ta, p_ta)

# print(f"P(veg|ta) = {p_veg_dato_ta * 100 :.2f}%")
# print(f"Interpretazione: sapendo che takeaway è avvenuto, la probabilità che si verifichi anche veg è: {p_veg_dato_ta:.2f}")


#oppure 
def prob_con(p_veg_inter_ta, p_ta):
    if p_ta == 0:
        raise ValueError("Errore. La probabilità di takeaway non può essere negativa")
    return p_veg_inter_ta / p_ta 

print("Calcolo probabilità condizionata P(veg|takeaway):")
p_veg_inter_ta = float(input("Inserisci intersezione di veg con takeaway: "))
p_takeaway = float(input("Inserisci P(ta): "))

p_veg_dato_ta = prob_con(p_veg_inter_ta, p_takeaway)

print("\nRisultato: ")
print(f"Probabilità che vegetariano si verifichi dato takeaway avvenuto: {p_veg_dato_ta:.2f}%")

