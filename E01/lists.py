Nomi_settimana=['Lunedì', 'Martedì',' Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
Nomi_settimana_iniz=Nomi_settimana[1:]
print(Nomi_settimana_iniz)
Nomi_settimana_prima_parte= Nomi_settimana[0:4]
Mese_ottobre= Nomi_settimana_iniz +(3* Nomi_settimana) + Nomi_settimana_prima_parte
print(Mese_ottobre)
#lavoro sul dizionario con il metodo update
dict={1: "Martedì"}
for i in range (2,32):
    dict.update({i: Mese_ottobre[i-1]})
print (dict)
#oppure vedi come farlo con list comprehension
