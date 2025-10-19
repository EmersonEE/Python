import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

BROKER = "192.168.1.136"
PORT = 1883

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

def send_command(topic, message):
    client.publish(topic, message)
    print(f"Enviado → {topic}: {message}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("🤖 Control de 4 Motores NEMA - MQTT")
root.configure(bg='#2b2b2b')
root.resizable(True, True)

# Estilo moderno
style = ttk.Style()
style.theme_use('clam')

# Configurar colores y fuentes
bg_color = '#2b2b2b'
card_bg = '#3c3c3c'
accent_color = '#4a9cff'
text_color = '#ffffff'
button_bg = '#5a5a5a'

style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=text_color, font=('SF Pro Display', 10))
style.configure('Title.TLabel', background=bg_color, foreground=text_color, font=('SF Pro Display', 14, 'bold'))
style.configure('Card.TFrame', background=card_bg)
style.configure('Control.TButton', background=button_bg, foreground=text_color, 
                font=('SF Pro Display', 11), borderwidth=0, focuscolor='none')
style.map('Control.TButton', 
          background=[('active', accent_color), ('pressed', '#3a7cff')])

# Función para crear tarjetas de control
def create_motor_card(parent, title, row, left_cmd, right_cmd=None, up_cmd=None, down_cmd=None):
    # Marco de la tarjeta
    card = ttk.Frame(parent, style='Card.TFrame', padding=15, relief='raised', borderwidth=1)
    card.grid(row=row, column=0, columnspan=3, padx=10, pady=8, sticky='ew')
    
    # Título del motor
    title_label = ttk.Label(card, text=title, style='Title.TLabel')
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
    
    if up_cmd and down_cmd:  # Control vertical (Motor 3)
        up_btn = ttk.Button(card, text="⬆ SUBIR", style='Control.TButton', 
                           command=up_cmd, width=12)
        up_btn.grid(row=1, column=1, padx=5, pady=2)
        
        down_btn = ttk.Button(card, text="⬇ BAJAR", style='Control.TButton', 
                             command=down_cmd, width=12)
        down_btn.grid(row=2, column=1, padx=5, pady=2)
        
    else:  # Control horizontal
        left_btn = ttk.Button(card, text="⟵ IZQUIERDA", style='Control.TButton', 
                             command=left_cmd, width=12)
        left_btn.grid(row=1, column=0, padx=5, pady=5)
        
        right_btn = ttk.Button(card, text="⟶ DERECHA", style='Control.TButton', 
                              command=right_cmd, width=12)
        right_btn.grid(row=1, column=2, padx=5, pady=5)
    
    return card

# Contenedor principal
main_frame = ttk.Frame(root, padding=20)
main_frame.grid(row=0, column=0, sticky='nsew')

# Configurar grid responsivo
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

# Título principal
header_label = ttk.Label(main_frame, text="CONTROL DE BRAZO ROBÓTICO", style='Title.TLabel')
header_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Crear tarjetas de control para cada motor
create_motor_card(main_frame, "🔄 MOTOR 1 - BASE", 1,
                 lambda: send_command("control/motor1", "LEFT"),
                 lambda: send_command("control/motor1", "RIGHT"))

create_motor_card(main_frame, "📏 MOTOR 3 - ALTURA", 2,
                 lambda: send_command("control/motor3", "UP"),
                 None,
                 lambda: send_command("control/motor3", "UP"),
                 lambda: send_command("control/motor3", "DOWN"))

create_motor_card(main_frame, "🔗 MOTOR 2 - ESLABÓN 1", 3,
                 lambda: send_command("control/motor2", "LEFT"),
                 lambda: send_command("control/motor2", "RIGHT"))

create_motor_card(main_frame, "🦾 MOTOR 4 - ESLABÓN 2", 4,
                 lambda: send_command("control/motor4", "LEFT"),
                 lambda: send_command("control/motor4", "RIGHT"))

# Estado de conexión
status_frame = ttk.Frame(main_frame, style='Card.TFrame', padding=10)
status_frame.grid(row=5, column=0, columnspan=3, pady=20, sticky='ew')

status_label = ttk.Label(status_frame, text="✅ Conectado al broker MQTT", 
                        font=('SF Pro Display', 9), background=card_bg, foreground='#90EE90')
status_label.pack()

# Footer
footer_label = ttk.Label(main_frame, text="Arch Linux + Hyprland 🐧", 
                        font=('SF Pro Display', 8), foreground='#888888')
footer_label.grid(row=6, column=0, columnspan=3, pady=(10, 0))

# Ajustar tamaño inicial de la ventana
root.update_idletasks()
root.minsize(400, 600)
root.geometry("450x650")

# Centrar la ventana
root.eval('tk::PlaceWindow . center')

root.mainloop()