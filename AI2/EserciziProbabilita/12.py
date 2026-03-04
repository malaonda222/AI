import math

'''Esercizio 12: Valore Atteso (Gioco a premi)
Testo: Un gioco consiste nel lanciare un dado a 6 facce. Se esce 6, vinci 10€. 
Se esce 4 o 5, vinci 1€. Se esce 1, 2 o 3, perdi 4€. 
Qual è il valore atteso di questo gioco? Conviene giocare?'''


'''6 -> 10 euro 
4 o 5 -> 1 euro 
1, 2, 3 -> perdi 4 euro

Formula valore atteso = Sommatoria x i p(x i)'''
''' P(6) = 1/6 
    P(4, 5) = 2/6
    P(1, 2, 3) = 1/2
    
10 * 1/6 + 1 * 2/6 + ((-4) * 3/6) = 10/6 + 2/6 - 12/6 = 0 (probabilità equa)

Se la probabilità fosse stata positiva -> conviene
Se la probabilità fosse stata negativa -> non conviene 

''' 

p_6 = 1/6 #+10
p_4_5 = 2/6 #+1
p_1_2_3 = 3/6 #-4

# valore_atteso = 1/6 * 10 + 2/6 * 1 + (-4) * 3/6
valore_atteso = 10/6 + 2/6 - 12/6
print(valore_atteso)




def valore_att(p_a: float, p_b:float, p_c:float, vincita_a: int, vincita_b: int, perdita_c:int):
    valore_atteso = (p_a * vincita_a) + (p_b * vincita_b) + ((perdita_c)* p_c)
    if math.isclose(valore_atteso, 0.0, abs_tol=1e-9):
        return "Equo"
    elif valore_atteso > 0:
        return "Conviene giocare"
    elif valore_atteso < 0:
        return "Non conviene giocare"


print(valore_att(1/6, 2/6, 3/6, 10, 1, -4))