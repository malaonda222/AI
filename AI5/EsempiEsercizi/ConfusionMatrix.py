# '''Scrivere il codice Python '''

import numpy as np 

# confusion_matrix = np.zeros([2, 2]) #crea una matrice di zeri

# # print(confusion_matrix)

# # print(confusion_matrix[0][0])


# #input due liste

# #opzione uno
# y_pred = [1, 0, 1, 1]
# y_real = [1, 0, 0, 1]
# for i in range(len(y_pred)): #faccio un ciclo su tutti gli indici del campione
#     reale = y_real[i] #estrai il valore reale al ciclo corrispondente
#     predetto = y_pred[i] #estrai il valore predetto al ciclo corrispondente
#     confusion_matrix[reale][predetto] += 1 #si aggiorna la confusion matrix, si aggiunge 1 alla cella corrispondente alla coppia (predittivo, real)
# print(confusion_matrix) #stampo la matrice di confusione 


# #opzione manuale (quando conosciamo la grandezza della matrice)
# def confusion(l_real: list, l_pred: list):
#     if len(l_pred) != len(l_real):
#         return "Errore, le liste devono avere la stessa lunghezza"
    
#     confusion_matrix = np.zeros([2, 2])

#     for x in range(len(l_real)):
#         if l_real[x] == 0 and l_pred[x] == 0:
#             confusion_matrix[0][0] += 1
#         elif l_real[x] == 0 and l_pred[x] == 1:
#             confusion_matrix[0][1] += 1
#         elif l_real[x] == 1 and l_pred[x] == 0:
#             confusion_matrix[1][0] += 1
#         else:
#             confusion_matrix[1][1]+=1
#     return confusion_matrix 


#opzione generalizzata 
y_real = [1, 0, 1, 1, 2, 2]
y_pred = [1, 0, 0, 1, 2, 0]

valori_unici = list(set(y_real))
n_classi = len(valori_unici)

confusion_matrix = np.zeros([n_classi, n_classi])
for i in range(len(y_real)): #faccio un ciclo su tutti gli indici del campione
    reale = y_real[i] #estrai il valore reale al ciclo corrispondente
    predetto = y_pred[i] #estrai il valore predetto al ciclo corrispondente
    confusion_matrix[reale][predetto] += 1 #si aggiorna la confusion matrix, si aggiunge 1 alla cella corrispondente alla coppia (predittivo, real)
print(confusion_matrix)


#data la confusion matrix, calcola l'Accuracy 

somma_totale = 0
diagonale = 0
for i in range(len(confusion_matrix)):
    for j in range(len(confusion_matrix)):
        if i == j:
            diagonale += confusion_matrix[i][j]
        somma_totale += confusion_matrix[i][j]

accuracy = diagonale/somma_totale 
print(f"Accuracy: {accuracy}")