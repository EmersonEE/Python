import tkinter as tk
import paho.mqtt.client as mqtt

def create_gui():
    root = tk.Tk()
    root.title("Interfaz con Botones MQTT")

    # Parámetros del broker MQTT
    BROKER = "192.168.1.136"   # ← Cambia esta IP por la de tu broker o ESP32
    PORT = 1883
    TOPIC = "ESP/Secuencias"

    # Conectar al broker MQTT
    client = mqtt.Client()
    try:
        client.connect(BROKER, PORT, 60)
        print("✅ Conectado al broker MQTT")
    except Exception as e:
        print(f"❌ Error al conectar al broker MQTT: {e}")

    # Listas de botones
    left_buttons = []
    right_buttons = []

    # Variables de estado
    first_side_clicked = None
    left_selected = None
    right_selected = None

    # Etiqueta para mostrar la combinación
    status_label = tk.Label(root, text="Presiona un botón...", font=("Arial", 12))
    status_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Función para publicar por MQTT
    def send_mqtt_message(message):
        try:
            client.publish(TOPIC, message)
            print(f"📤 Enviado por MQTT → {TOPIC}: {message}")
        except Exception as e:
            print(f"❌ Error al enviar MQTT: {e}")

    # Función para actualizar el texto mostrado y enviar por MQTT
    def update_status():
        if left_selected and right_selected:
            if first_side_clicked == "left":
                combination = f"{left_selected}_{right_selected}"
            else:  # first_side_clicked == "right"
                combination = f"{right_selected}_{left_selected}"
            status_label.config(text=f"Combinación: {combination}")
            send_mqtt_message(combination)
        elif left_selected:
            status_label.config(text=f"Seleccionado: {left_selected}")
            # send_mqtt_message(left_selected)
        elif right_selected:
            status_label.config(text=f"Seleccionado: {right_selected}")
            # send_mqtt_message(right_selected)
        else:
            status_label.config(text="Presiona un botón...")

    # Función para manejar botón izquierdo
    def handle_left_click(button):
        nonlocal first_side_clicked, left_selected
        if first_side_clicked is None:
            first_side_clicked = "left"
        color = "red" if first_side_clicked == "left" else "green"
        button.config(bg=color)
        left_selected = button.cget("text")
        for btn in left_buttons:
            btn.config(state="disabled")
        # update_status()

    # Función para manejar botón derecho
    def handle_right_click(button):
        nonlocal first_side_clicked, right_selected
        if first_side_clicked is None:
            first_side_clicked = "right"
        color = "red" if first_side_clicked == "left" else "green"
        button.config(bg=color)
        right_selected = button.cget("text")
        for btn in right_buttons:
            btn.config(state="disabled")
        # update_status()

    # Función para reiniciar todo
    def reset_buttons():
        nonlocal first_side_clicked, left_selected, right_selected
        first_side_clicked = None
        left_selected = None
        right_selected = None
        for btn in left_buttons + right_buttons:
            btn.config(bg="#d9d9d9", state="normal")
        status_label.config(text="Presiona un botón...")        
        
        # send_mqtt_message("Reinicio de botones")

    # Crear botones izquierdos
    for i in range(3):
        btn = tk.Button(root, text=f"BI_{i+1}", width=20, height=2, bg="#d9d9d9")
        btn.grid(row=i, column=0, padx=10, pady=10)
        btn.config(command=lambda b=btn: handle_left_click(b))
        left_buttons.append(btn)

    # Crear botones derechos
    for i in range(3):
        btn = tk.Button(root, text=f"BD_{i+1}", width=20, height=2, bg="#d9d9d9")
        btn.grid(row=i, column=1, padx=10, pady=10)
        btn.config(command=lambda b=btn: handle_right_click(b))
        right_buttons.append(btn)

    # Botón de reinicio
    reset_button = tk.Button(root, text="Ejecutar", width=20, height=2, command=lambda:[ update_status(),reset_buttons()], bg="#d9d9d9")
    reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    
    # reset_button = tk.Button(root, text="Enviar", width=20, height=2, command=update_status, bg="#d9d9d9")
    # reset_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
