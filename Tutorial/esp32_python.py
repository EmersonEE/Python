import serial
import time
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# CONFIGURACIÓN SERIAL
# -------------------------------
PUERTO = '/dev/ttyUSB0'  # Ajusta según tu sistema
BAUDRATE = 115200

try:
    ser = serial.Serial(PUERTO, BAUDRATE, timeout=1)
    time.sleep(2)  # Espera al ESP32
    print("✅ Conexión serial establecida con el ESP32.")
except Exception as e:
    messagebox.showerror("Error de conexión", f"No se pudo conectar al puerto {PUERTO}:\n{e}")
    exit()

# -------------------------------
# FUNCIONES DE CONTROL
# -------------------------------

def enviar_comando(cmd):
    """Envía texto por serial al ESP32"""
    try:
        ser.write((cmd + '\n').encode())  # Envía el comando
        print(f"📤 Enviado: {cmd}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar comando: {e}")

def giro_completo():
    enviar_comando('360')
    label_status.config(text="Motor: Giro completo →", fg="green")

def giro_inverso():
    enviar_comando('-360')
    label_status.config(text="Motor: Giro completo ←", fg="red")

def enviar_angulo():
    try:
        grados = float(entry_grados.get())
        # if grados < 0:
        #     messagebox.showwarning("Advertencia", "El ángulo debe ser positivo.")
        #     return
        enviar_comando(str(grados))
        label_status.config(text=f"Motor: {grados}° enviados", fg="blue")
    except ValueError:
        messagebox.showerror("Error", "Introduce un valor numérico válido para los grados.")

def cerrar_app():
    try:
        ser.close()
    except:
        pass
    root.quit()

# -------------------------------
# INTERFAZ GRÁFICA (Tkinter)
# -------------------------------
root = tk.Tk()
root.title("Control de Motor NEMA17 - ESP32")
root.geometry("350x300")
root.protocol("WM_DELETE_WINDOW", cerrar_app)

label_status = tk.Label(root, text="Motor detenido", fg="black", font=("Arial", 12))
label_status.pack(pady=15)

# Botones de control
btn_giro = tk.Button(root, text="Girar 360° →", command=giro_completo, bg="#4CAF50", fg="white", font=("Arial", 10))
btn_giro.pack(pady=10)

btn_giro_inv = tk.Button(root, text="Girar -360° ←", command=giro_inverso, bg="#E53935", fg="white", font=("Arial", 10))
btn_giro_inv.pack(pady=10)

# Campo para ángulo personalizado
frame_angulo = tk.Frame(root)
frame_angulo.pack(pady=10)

tk.Label(frame_angulo, text="Ángulo (°):", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
entry_grados = tk.Entry(frame_angulo, width=10)
entry_grados.pack(side=tk.LEFT, padx=5)
btn_enviar = tk.Button(frame_angulo, text="Enviar", command=enviar_angulo, bg="#2196F3", fg="white", font=("Arial", 10))
btn_enviar.pack(side=tk.LEFT, padx=5)

# -------------------------------
# LOOP DE LA INTERFAZ
# -------------------------------
root.mainloop()
