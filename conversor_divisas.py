import customtkinter as ctk
import tkinter as tk
import yfinance as yf
import os
import threading

# 1. Creamos el diccionario con las divisas.
import csv

from ruamel.yaml import anchor

divisas = {}

with open('divisas.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    for fila in lector:
        clave, valor = fila
        divisas[clave] = valor
lista_divisas = sorted(divisas.keys())

# 2. Nos anticiparemos a los errores si el otro usuario no tiene tkinter.


# 3. Definimos la Función XXXXXXXXXXXXXXXXXXXXXXXX

# 4. Configuramos la ventana principal.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Conversor de Divisas")
app.geometry('500x250')
app.resizable(width=False, height=False)

# Adición de labels
label_titulo = ctk.CTkLabel(master=app, text="Conversor de Divisas", font=("Segoe UI", 20))
label_titulo.place(relx=0.5, rely=0.1, anchor="center")
label_desde = ctk.CTkLabel(master=app, text="Desde", font=("Segoe UI", 15))
label_desde.place(relx=0.2, rely=0.3, anchor="center")
label_hasta = ctk.CTkLabel(master=app, text="Hasta", font=("Segoe UI", 15))
label_hasta.place(relx=0.8, rely=0.3, anchor="center")

# Adición Combobox
combobox_divisas_desde = ctk.CTkOptionMenu(master=app, values=lista_divisas, font=("Segoe UI", 15))
combobox_divisas_desde.place(relx=0.2, rely=0.4, anchor="center")
combobox_divisas_hasta = ctk.CTkOptionMenu(master=app, values=lista_divisas, font=("Segoe UI", 15))
combobox_divisas_hasta.place(relx=0.8, rely=0.4, anchor="center")

# Adición de la entrada y etiqueta de resultado

entry_divisa_computar = ctk.CTkEntry(master=app, placeholder_text="Ingresa el valor", font=("Segoe UI", 15))
entry_divisa_computar.place(relx=0.2, rely=0.6, anchor="center")
label_resultado = ctk.CTkEntry(master=app, state='readonly', font=("Segoe UI", 15))
label_resultado.place(relx=0.8, rely=0.6, anchor="center")

#Adición botón de convertir

def button_clicked():
    print("Button clicked")

button_convertir = ctk.CTkButton(master=app, text="Convertir", command=button_clicked)
button_convertir.place(relx=0.5, rely=0.5, anchor="center")
app.mainloop()
