f1 = open("result-pass-fail-1.csv").read() #Reads a file informing if the student passed in a exercise
f2 = open("result-count-1.csv").read() #Reads a file with the number of tries for each exercise
if f1[-1] != "\n":
    f1 += "\n"
if f2[-1] != "\n":
    f2 += "\n"

lista1 = []
nova_lista1 = []

palavra = "" #Creates a matrice with the data
for i in f1:
    if i != ";" and i != "\n":
        palavra += i
    elif i == ";":
        nova_lista1.append(palavra)
        palavra = ""
    elif i == "\n":
        nova_lista1.append(palavra)
        lista1.append(nova_lista1)
        nova_lista1 = []
        palavra = ""
lista1.append(nova_lista1)
lista1.remove(lista1[-1])

lista2 = []
nova_lista2 = []

palavra = "" #Creates a matrice with the data
for i in f2:
    if i != ";" and i != "\n":
        palavra += i
    elif i == ";":
        nova_lista2.append(palavra)
        palavra = ""
    elif i == "\n":
        nova_lista2.append(palavra)
        lista2.append(nova_lista2)
        nova_lista2 = []
        palavra = ""
lista2.append(nova_lista2)
if lista2[-1] == []:
    lista2.remove(lista2[-1])

matriz1 = []
nova_matriz1 = []

for i in range(len(lista1[0])):
    for j in lista1:
        nova_matriz1.append(j[i])
    matriz1.append(nova_matriz1)
    nova_matriz1 = []

matriz2 = []
nova_matriz2 = []

for i in range(len(lista2[0])):
    for j in lista2:
        nova_matriz2.append(j[i])
    matriz2.append(nova_matriz2)
    nova_matriz2 = []

for i in matriz2: #Changes the empty spaces with a 0
    for k in range(1, len(i)):
        if i[k] == "":
            i[k] = "0"

for i in matriz2: #Transforms the data into integers
    for k in range(1, len(i)):
        i[k] = int(i[k])

dicionario = []
for i in range(len(matriz2)): #Creates a list with the students that didn't reach the criteria and its location in the matrice
    for j in range(1, len(matriz2[i])):
        if matriz2[i][j] > 10:
            dicionario.append((i, j))

deletar = 0
for i in dicionario: #Changes the data that shall be deleted
    for j in range(len(matriz1)):
        matriz1[j][i[1]] = "del"
        matriz2[j][i[1]] = "del"
        deletar += 1

andre1 = []
andre_aux1 = []
for i in matriz1: #Creates a new matrice without the deleted data
    for j in range(len(i)):
        if i[j] != "del":
            andre_aux1.append(i[j])
    andre1.append(andre_aux1)
    andre_aux1 = []

andre2 = []
andre_aux2 = []
for i in matriz2: #Creates a new matrice without the deleted data
    for j in range(len(i)):
        if i[j] != "del":
            andre_aux2.append(i[j])
    andre2.append(andre_aux2)
    andre_aux2 = []

contador = 0
final = {}
for i in andre1: #Creates a dictionarie with the Exercise title and the number of tries
    for j in i:
        if j == "VRAI":
            contador += 1
    final.update({i[0]: contador})
    contador = 0 

final_sorted = {k: v for k, v in sorted(final.items(), key=lambda item: item[1])} #Sorts the dictionarie
chaves = list(final_sorted.keys())
chaves.reverse()
for i in chaves:
    print(i)