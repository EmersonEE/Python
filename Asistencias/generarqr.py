import os
import qrcode
from PIL import Image
import math
import time 

def solicitar_carnet():
    while True:
        try:
            numero = int(input("Ingrese Su Carnet "))
            if numero > 0:
                if len(str(numero)) == 9:
                    return numero
                else:
                    print("El número debe tener exactamente 9 dígitos.")
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def solicitar_string():
    while True:
        texto = input("Ingrese Su Nombre: ")
        if texto.strip():
            if any(char.isdigit() for char in texto):
                print("El nombre no debe contener números.")
            else:
                return texto
        else:
            print("El texto no puede estar vacío.")


nombre = solicitar_string()
carnet = solicitar_carnet()

if not os.path.exists("Asistencias"):
    os.makedirs("Asistencias")
if not os.path.exists(os.path.join("Asistencias", "QRs")):
    os.makedirs(os.path.join("Asistencias", "QRs")) 


# Crear el código QR
qr_data = f"Carnet: {carnet} Nombre: {nombre}"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(qr_data)
qr.make(fit=True)
# Generar la imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")
# Guardar la imagen del código QR
ruta = os.path.join(os.getcwd(), "Asistencias", "QRs")
if not os.path.exists(ruta):
    os.makedirs(ruta)
img_path = os.path.join(ruta, f"{carnet}.png")
img.save(img_path)
# Mostrar la imagen del código QR
img.show()
# Imprimir la ruta del archivo QR generado
print(f"Código QR generado y guardado en: {img_path}")
# Mostrar el contenido del código QR        

