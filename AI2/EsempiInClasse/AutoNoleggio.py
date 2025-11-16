def probabilita_suv_audi(p_suv_inter_aud, p_audi):
    if p_audi == 0:
        raise ValueError("P(Audi) non può essere 0")
    return p_suv_inter_aud / p_audi 


print("Calcolo probabilità condizionata P(suv|audi):")
p_suv_inter_audi = float(input("Inserisci P(suv ∩ audi): "))
p_audi = float(input("Inserisci P(audi): "))

p_suv_dato_audi = probabilita_suv_audi(p_suv_inter_audi, p_audi)

print("\nRisultato: ")
print(f"P(suv|audi) = {p_suv_dato_audi * 100 :.2f}")
print(f"Interpretazione: sapendo che audi è avvenuto, la probabilità che si verifichi anche suv è: {p_suv_dato_audi * 100:.2f} %")


#oppure 

def probabilita_condizionata(p_suv_inter_audi, p_audi):
    if p_audi == 0:
        raise ValueError("La probabilità dell'evento condizionante non può essere 0")
    return p_suv_inter_audi / p_audi


auto = {
    "citycar": {
        "toyota": 50,
        "audi": 20
    },
    "suv": {
        "toyota": 25, 
        "audi": 5
    }
}


#calcolo del numero totale di auto
totale = sum(auto["citycar"].values()) + sum(auto["suv"].values())

#P(suv|audi) = numero suv audi / totale 
p_suv_inter_audi = auto["suv"]["audi"] / totale 

#P(audi) = numero audi / totale 
p_audi = (auto["citycar"]["audi"] + ["suv"]["audi"]) / totale 

#Probabilità condizionata
p_suv_dato_audi = probabilita_condizionata(p_suv_inter_audi, p_audi)

print(f"P(suv|audi) = {p_suv_dato_audi * 100:.2f}%")

