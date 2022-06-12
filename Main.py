#Main.py: lee una web y da la frecuencia de las palablas
#Estado:    - Finalizado
#           - 25/10/2021

from pandas import DataFrame
import numpy as np
from LectorWebV2 import url2text


url = 'https://www.boe.es/buscar/act.php?id=BOE-A-1978-31229'
lon_palabra_min = 3 #minimo de letras de una palabra para que se tenga en cuenta


file_web = url2text(url)
print(url)

with open("inutiles.txt" , "r" , encoding="utf8") as inu:
    inutiles = inu.read()
    inutiles = inutiles.split(sep=',')


file_web = file_web.lower() #convertir a minusculas
string_web = file_web.split() #separar por comas


frecuenciaPalab = []
count = []


ii = 0
for w in string_web:
    ii = ii + 1

    palabra = w
    count.append(w)
    frecuencia = string_web.count(w)

    suma = [palabra,frecuencia]
    a=0

    for n in count:
        #print(n)
        if w == n:
            a += 1
    if a == 1 and len(w) >= lon_palabra_min:
        frecuenciaPalab.append(suma)

#print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
#print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
#print(len(string_web))

archivo = []
archivo = frecuenciaPalab

for inutil in inutiles:
    for palabra in frecuenciaPalab:
        if inutil == palabra[0]:
            archivo.remove(palabra)


#print("palabra: ",frecuenciaPalab[2018][0])

#for indice in indices:
    #print(indice)
    #print(frecuenciaPalab[indice][0])
    #del frecuenciaPalab[indice]


df = DataFrame(archivo,columns=['Palabra','Repeticiones'])


df.sort_values(by ='Repeticiones', ascending=False , axis=0 , inplace=True)
print(df.head(20))
