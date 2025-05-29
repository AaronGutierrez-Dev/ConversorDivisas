from tkinter import ttk, Button
import tkinter as tk
import yfinance as yf
import os
import threading


#1. Creamos el diccionario con las divisas.
import csv

divisas = {}

with open('divisas.csv', newline='') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        clave, valor = fila
        divisas[clave] = valor
lista_divisas = sorted(divisas.keys())

#2. Nos anticiparemos a los errores si el otro usuario no tiene tkinter.
try:
    import tkinter as tk
except ImportError:
    import tkinter as tk

# 3. Definimos la Función XXXXXXXXXXXXXXXXXXXXXXXX

# 4. Configuramos la ventana principal.
root = tk.Tk()
root.title("Conversor de Divisas")
root.geometry("700x350")
root.resizable(False, False)

# 5. Asignación de cuadrículas para colocar los widgets.
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)


# 6. Inclusión de widgets.
label_titulo = tk.Label(root, text="Conversor de Divisas", bg="black", fg="white", font=("Arial", 12))
label_from_1 = tk.Label(root, text="Desde", bg="black", fg="white", font=("Arial", 12))
label_to_2 = tk.Label(root, text="A", bg="black", fg="white", font=("Arial", 12))
label_titulo.grid(row=0, column=2, columnspan=2, sticky=tk.NSEW)
label_from_1.grid(row=1, column=1, padx=20, pady=10)
label_to_2.grid(row=1, column=4, padx=20, pady=10)
combo_from = ttk.Combobox(root, values=lista_divisas, width=30)
combo_to = ttk.Combobox(root, values=lista_divisas, width=30)
combo_from.grid(row=2, column=1, padx=10, pady=10)
combo_to.grid(row=2, column=4, padx=10, pady=10)
entry_from = ttk.Entry(root, width=33)
entry_from.grid(row=3, column=1, padx=10, pady=10)
result_label = tk.Label(root, text="", bg="white", fg="black", width=22, font=("Arial", 12) )
result_label.grid(row=3, column=4, padx=10, pady=10)
button_convert = Button(root, text="Convertir")
button_convert.grid(row=3, column=2, padx=10, pady=10, columnspan=2, sticky=tk.NSEW)



root.mainloop()
