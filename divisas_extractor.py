import csv

divisas = {}

with open('divisas.csv', newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        clave, valor = fila
        divisas[clave] = valor


print(divisas)