#Se importan las librerias necesarias para realizar el trabajo. Con Customtkinter y tkinter se desarrolla la interfaz gráfica y con requests se logra realizar las peticiones a la API para obtener los datos divisas
import customtkinter as ctk
import tkinter as tk
import requests

# 1. Creamos el diccionario con las divisas. Para este caso, se utilizarán estas como ejemplo
monedas = {
    "Dólar estadounidense": "USD",
    "Euro": "EUR",
    "Libra esterlina": "GBP",
    "Yen japonés": "JPY",
    "Franco suizo": "CHF",
    "Dólar canadiense": "CAD",
    "Dólar australiano": "AUD",
    "Peso mexicano": "MXN",
    "Peso argentino": "ARS",
    "Real brasileño": "BRL",
    "Peso chileno": "CLP",
    "Peso colombiano": "COP",
    "Sol peruano": "PEN",
    "Boliviano": "BOB",
    "Guaraní paraguayo": "PYG",
    "Uruguayo peso": "UYU",
    "Rublo ruso": "RUB",
    "Yuan chino": "CNY",
    "Rupia india": "INR",
    "Won surcoreano": "KRW",
    "Rand sudafricano": "ZAR",
    "Lira turca": "TRY",
    "Dólar neozelandés": "NZD",
    "Dólar de Singapur": "SGD",
    "Dirham de Emiratos Árabes Unidos": "AED"
}

lista_monedas = list(monedas.keys()) #Se extrae solo las Key del diccionario, lo que corresponde al nombre de la divisa para ser utilizado en los combobox.

# 3. Definimos la Función tasa_cambio la cual permitirá obtener la tasa de cambio de las divisas que el usuario escoja solicitandolas a la API.

#Creamos la variable API_KEY y asignamos la Key que solicité en la API Exchangerate Host la cual es necesaria para el correcto funcionamiento de la API y de la App.
API_KEY = "2c127d63a66edb2ee384bb6e25d03584"

#Definimos la función con 3 argumentos: base es la moneda inicial, hacia es la moneda que el usuario espera obtener y cantidad=1 es el valor fijado por defecto (1 unidad monetaria) para obtener el valor de cambio entre ambas divisas.
def tasa_cambio(base, hacia, cantidad=1):
    
    #Definimos la función con 3 argumentos: base es la moneda inicial, hacia es la moneda que el usuario espera obtener y cantidad=1 es el valor fijado por defecto (1 unidad monetaria) para obtener el valor de cambio entre ambas divisas.

    url = f"https://api.exchangerate.host/convert?access_key={API_KEY}&from={base}&to={hacia}&amount={cantidad}"
    #Usamos el Manejo de Excepciones con Try Except.
    try:
        #Enviamos petición HTTP a la URL de la API.
        peticion = requests.get(url) 
        #Obtenemos en formato JSON los datos generados de la petición a la API.
        datos = peticion.json()
        #Hacemos un print en consola para ver la información que nos arroja al hacer la petición a la API.
        print("Respuesta API:", datos)
        #Utilizamos un condicional para obtener el resultado de la cantidad (1) monetaria convertida en caso que el campo del diccionario llamado Succes sea True.
        if datos.get("success", False):
            return datos.get("result")
        #De lo contrario, devolverá el error ya que no hay valores para trabajar con la función convertir.
        else:   
            error_info = datos.get("error", {}).get("info", "Error desconocido")
            raise Exception(f"La API devolvió un error: {error_info}")
    #Si hay algún error distinto al propio de la API, como puede ser de conexión, Firewall, etc, dirá que hay un error de conexión. En este caso, se llaman a todos los errores y se ingresa en "tipo_error" para luego ser mostrado.
    except requests.exceptions.RequestException as tipo_error:
        raise Exception(f"Error de conexión: {tipo_error}")


# 4. Configuramos la ventana principal.

#Establecemos la apareciencia que tendrá la ventana principal de la aplicación eligiendo el modo dark y color blue con los atributos set_appearance_mode y set_default_color_theme.
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Creamos la ventana principal y asignamos título, dimensiones e impedimos que el tamaño pueda ser modificado por el usuario con el atributo resizable.
app = ctk.CTk()
app.title("Conversor de Divisas")
app.geometry('600x250')
app.resizable(width=False, height=False)

# Adición de labels
label_titulo = ctk.CTkLabel(master=app, text="Conversor de Divisas", font=("Segoe UI", 20))
label_titulo.place(relx=0.5, rely=0.1, anchor="center")
label_desde = ctk.CTkLabel(master=app, text="Desde", font=("Segoe UI", 15))
label_desde.place(relx=0.2, rely=0.2, anchor="center")
label_hasta = ctk.CTkLabel(master=app, text="Hacia", font=("Segoe UI", 15))
label_hasta.place(relx=0.8, rely=0.2, anchor="center")

# Adición de los Combobox
combobox_divisas_desde = ctk.CTkOptionMenu(master=app, values=lista_monedas, font=("Segoe UI", 15))
combobox_divisas_desde.place(relx=0.2, rely=0.3, anchor="center")
combobox_divisas_hacia = ctk.CTkOptionMenu(master=app, values=lista_monedas, font=("Segoe UI", 15))
combobox_divisas_hacia.place(relx=0.8, rely=0.3, anchor="center")

# Adición de la entrada del valor a convertir y etiqueta de resultado

entry_divisa_computar = ctk.CTkEntry(master=app, placeholder_text="Ingresa el valor", font=("Segoe UI", 15))
entry_divisa_computar.place(relx=0.5, rely=0.5, anchor="center")
label_resultado = ctk.CTkEntry(master=app, state='readonly', font=("Segoe UI", 15), width=400)
label_resultado.place(relx=0.5, rely=0.9, anchor="center")

#Definición de la función con la que convertiremos los y daremos funcionamiento a la aplicación.
def convertir():

    #Con XXX TRY - EXCEPT haremos que la aplicación realice una operación de conversión de monedas según los datos obtenidos de la API. En caso de que haya algún error, esta pasará al EXCEPT -  y mostrará un mensaje según el tipo de error o problema.

    try:
        valor_ingreso = float(entry_divisa_computar.get())
        desde = combobox_divisas_desde.get()
        hacia = combobox_divisas_hacia.get()

        # Validar selección
        codigo_moneda_desde = monedas[desde]
        codigo_moneda_hacia = monedas[hacia]

        cambio_entre_monedas = tasa_cambio(codigo_moneda_desde, codigo_moneda_hacia)
        resultado = cambio_entre_monedas * valor_ingreso

        label_resultado.configure(state="normal")
        label_resultado.delete(0, ctk.END)
        label_resultado.insert(0, f"{valor_ingreso} {codigo_moneda_desde} equivalen a {resultado:.2f} {codigo_moneda_hacia}")
        label_resultado.configure(state="readonly")

    except ValueError as ve:
        label_resultado.configure(state="normal")
        label_resultado.delete(0, ctk.END)
        label_resultado.insert(0, f"Error: {ve}")
        label_resultado.configure(state="readonly")
    except Exception as e:
        label_resultado.configure(state="normal")
        label_resultado.delete(0, ctk.END)
        label_resultado.insert(0, f"Error: {e}")
        label_resultado.configure(state="readonly")

#Adición botón de convertir
button_convertir = ctk.CTkButton(master=app, text="Convertir", command=convertir)
button_convertir.place(relx=0.5, rely=0.7, anchor="center")

app.mainloop()
