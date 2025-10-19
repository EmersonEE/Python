import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

secuencias = {
    "BI_1_BD_1" : 0,
    "BI_1_BD_2" : 1,
    "BI_1_BD_3" : 2,
    "BI_2_BD_1" : 3,
    "BI_2_BD_2" : 4,
    "BI_2_BD_3" : 5,
    "BI_3_BD_1" : 6,
    "BI_3_BD_2" : 7,
    "BI_3_BD_3" : 8,
    "BD_1_BI_1" : 9,
    "BD_1_BI_2" : 10,
    "BD_1_BI_3" : 11,
    "BD_2_BI_1" : 12,
    "BD_2_BI_2" : 13,
    "BD_2_BI_3" : 14,
    "BD_3_BI_1" : 15,
    "BD_3_BI_2" : 16,
    "BD_3_BI_3" : 17,
    
}
for i in secuencias:
    print(i)
def create_gui():
    root = tk.Tk()
    root.title("Control MQTT - Secuencias")
    
    # Configuración de la ventana para Hyprland
    root.configure(bg='#1e1e2e')
    root.attributes('-alpha', 0.95)
    
    # Colores modernos para Hyprland (usados en ambas pestañas)
    COLORS = {
        'bg': '#1e1e2e',         # Fondo principal
        'card_bg': '#313244',    # Fondo de tarjetas y etiquetas
        'text': '#cdd6f4',       # Color de texto
        'accent': '#89b4fa',     # Color de énfasis (títulos, botones activos)
        'success': '#a6e3a1',    # Color para combinaciones exitosas
        'warning': '#f9e2af',    # Color para botones hover/activos
        'error': '#f38ba8',      # Color para botones izquierdos seleccionados
        'button_normal': '#45475a',  # Color de botones en reposo
        'button_hover': '#585b70'    # Color de botones en hover
    }

    # Estilo moderno para ttk widgets
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TNotebook', background=COLORS['bg'], borderwidth=0)
    style.configure('TNotebook.Tab', 
                    background=COLORS['card_bg'],
                    foreground=COLORS['text'],
                    font=('JetBrains Mono', 10, 'bold'),
                    padding=[10, 5],
                    borderwidth=0)
    style.map('TNotebook.Tab',
              background=[('selected', COLORS['accent']), ('active', COLORS['button_hover'])],
              foreground=[('selected', '#1e1e2e'), ('active', COLORS['text'])])
    style.configure('TFrame', background=COLORS['bg'])
    style.configure('TLabel', background=COLORS['bg'], foreground=COLORS['text'], font=('JetBrains Mono', 10))
    style.configure('Title.TLabel', background=COLORS['bg'], foreground=COLORS['accent'], font=('JetBrains Mono', 14, 'bold'))
    style.configure('Card.TFrame', background=COLORS['card_bg'], relief='flat')
    style.configure('Control.TButton', 
                    background=COLORS['button_normal'],
                    foreground=COLORS['text'],
                    font=('JetBrains Mono', 10, 'bold'),
                    borderwidth=0,
                    focuscolor='none')
    style.map('Control.TButton',
              background=[('active', COLORS['button_hover']), ('pressed', COLORS['accent'])],
              foreground=[('active', COLORS['text']), ('pressed', '#1e1e2e')])

    # Crear notebook (pestañas)
    notebook = ttk.Notebook(root, style='TNotebook')
    notebook.pack(fill='both', expand=True, padx=10, pady=10)
    
    # Frame para la pestaña original (Secuencias)
    tab_original = tk.Frame(notebook, bg=COLORS['bg'])
    notebook.add(tab_original, text="🎛️ Secuencias")
    
    # Frame para nueva pestaña
    tab_nueva = tk.Frame(notebook, bg=COLORS['bg'])
    notebook.add(tab_nueva, text="⚡ Control de Motores")
    
    # ========== PESTAÑA ORIGINAL ==========
    
    # Parámetros del broker MQTT
    BROKER = "192.168.1.136"
    PORT = 1883
    TOPIC = "ESP/Secuencias"

    # Conectar al broker MQTT
    client = mqtt.Client()
    try:
        client.connect(BROKER, PORT, 60)
        print("✅ Conectado al broker MQTT")
    except Exception as e:
        print(f"❌ Error al conectar al broker MQTT: {e}")

    def send_mqtt_message(message):
        try:
            client.publish(TOPIC, message)
            print(f"📤 Enviado por MQTT → {TOPIC}: {message}")
        except Exception as e:
            print(f"❌ Error al enviar MQTT: {e}")

    # Listas de botones
    left_buttons = []
    right_buttons = []

    # Variables de estado
    first_side_clicked = None
    left_selected = None
    right_selected = None

    # Función para efectos hover
    def on_enter(e):
        if e.widget['state'] == 'normal':
            e.widget['background'] = COLORS['button_hover']

    def on_leave(e):
        if e.widget['state'] == 'normal':
            e.widget['background'] = COLORS['button_normal']

    # Etiqueta para mostrar la combinación
    status_label = tk.Label(
        tab_original, 
        text="🎛️  Selecciona una secuencia...", 
        font=("JetBrains Mono", 12, "bold"), 
        bg=COLORS['card_bg'],
        fg=COLORS['text'],
        relief='flat',
        padx=20,
        pady=10
    )
    status_label.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=20, sticky='ew')

    # Frame para los botones izquierdos
    left_frame = tk.Frame(tab_original, bg=COLORS['bg'])
    left_frame.grid(row=1, column=0, padx=(20, 10), pady=10)

    # Frame para los botones derechos
    right_frame = tk.Frame(tab_original, bg=COLORS['bg'])
    right_frame.grid(row=1, column=1, padx=(10, 20), pady=10)

    # Títulos para las columnas
    left_title = tk.Label(
        left_frame, 
        text="SECUENCIAS IZQ", 
        font=("JetBrains Mono", 10, "bold"), 
        bg=COLORS['bg'],
        fg=COLORS['accent']
    )
    left_title.pack(pady=(0, 10))

    right_title = tk.Label(
        right_frame, 
        text="SECUENCIAS DER", 
        font=("JetBrains Mono", 10, "bold"), 
        bg=COLORS['bg'],
        fg=COLORS['accent']
    )
    right_title.pack(pady=(0, 10))

    # Función para actualizar el texto mostrado
    def update_status():
        nonlocal left_selected, right_selected
        if left_selected and right_selected:
            if first_side_clicked == "left":
                combination = f"{left_selected}_{right_selected}"
            else:  # first_side_clicked == "right"
                combination = f"{right_selected}_{left_selected}"
            status_label.config(
                text=f"🚀 Combinación: {combination}", 
                bg=COLORS['success'],
                fg='#1e1e2e'
            )
            for i in secuencias:
                if i == combination:
                    print(secuencias[i])
                    send_mqtt_message(secuencias[i])
        elif left_selected:
            status_label.config(
                text=f"⬅️  Seleccionado: {left_selected}",
                bg=COLORS['card_bg'],
                fg=COLORS['text']
            )
        elif right_selected:
            status_label.config(
                text=f"➡️  Seleccionado: {right_selected}",
                bg=COLORS['card_bg'],
                fg=COLORS['text']
            )
        else:
            status_label.config(
                text="🎛️  Selecciona una secuencia...",
                bg=COLORS['card_bg'],
                fg=COLORS['text']
            )

    # Función para manejar botón izquierdo
    def handle_left_click(button):
        nonlocal first_side_clicked, left_selected
        if first_side_clicked is None:
            first_side_clicked = "left"
        color = COLORS['error'] if first_side_clicked == "left" else COLORS['success']
        button.config(bg=color, fg='#1e1e2e')
        left_selected = button.cget("text")
        for btn in left_buttons:
            btn.config(state="disabled")
        # update_status()

    # Función para manejar botón derecho
    def handle_right_click(button):
        nonlocal first_side_clicked, right_selected
        if first_side_clicked is None:
            first_side_clicked = "right"
        color = COLORS['error'] if first_side_clicked == "left" else COLORS['success']
        button.config(bg=color, fg='#1e1e2e')
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
            btn.config(bg=COLORS['button_normal'], fg=COLORS['text'], state="normal")
        update_status()

    # Estilo común para botones
    button_style = {
        'width': 12,  # Ajustado para consistencia con la pestaña Nueva Funcionalidad
        'height': 2,
        'font': ("JetBrains Mono", 10, "bold"),
        'relief': 'flat',
        'borderwidth': 0,
        'cursor': 'hand2'
    }

    # Crear botones izquierdos
    for i in range(3):
        btn = tk.Button(
            left_frame, 
            text=f"BI_{i+1}", 
            bg=COLORS['button_normal'],
            fg=COLORS['text'],
            activebackground=COLORS['button_hover'],
            activeforeground=COLORS['text'],
            **button_style
        )
        btn.pack(pady=8)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.config(command=lambda b=btn: handle_left_click(b))
        left_buttons.append(btn)

    # Crear botones derechos
    for i in range(3):
        btn = tk.Button(
            right_frame, 
            text=f"BD_{i+1}", 
            bg=COLORS['button_normal'],
            fg=COLORS['text'],
            activebackground=COLORS['button_hover'],
            activeforeground=COLORS['text'],
            **button_style
        )
        btn.pack(pady=8)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.config(command=lambda b=btn: handle_right_click(b))
        right_buttons.append(btn)

    # Frame para botón de acción
    action_frame = tk.Frame(tab_original, bg=COLORS['bg'])
    action_frame.grid(row=2, column=0, columnspan=2, pady=20)

    # Botón de ejecutar
    execute_button = tk.Button(
        action_frame, 
        text="⚡ EJECUTAR SECUENCIA", 
        width=25,
        height=2,
        font=("JetBrains Mono", 10, "bold"),
        bg=COLORS['accent'],
        fg='#1e1e2e',
        activebackground=COLORS['warning'],
        activeforeground='#1e1e2e',
        relief='flat',
        borderwidth=0,
        cursor='hand2',
        command=lambda: [update_status(), reset_buttons()]
    )
    execute_button.pack(pady=10)
    execute_button.bind("<Enter>", on_enter)
    execute_button.bind("<Leave>", on_leave)

    # Configurar grid weights para centrado responsivo
    tab_original.grid_columnconfigure(0, weight=1)
    tab_original.grid_columnconfigure(1, weight=1)
    tab_original.grid_rowconfigure(1, weight=1)

    # ========== NUEVA PESTAÑA ==========

    # Título principal de la nueva pestaña
    nueva_title = tk.Label(
        tab_nueva,
        text="🔧 CONTROL DE BRAZO ROBÓTICO",
        font=("JetBrains Mono", 14, "bold"),
        bg=COLORS['bg'],
        fg=COLORS['accent'],
        pady=20
    )
    nueva_title.grid(row=0, column=0, columnspan=3, pady=(10, 20), sticky='ew')

    # Contenedor principal para la nueva pestaña
    main_frame = tk.Frame(tab_nueva, bg=COLORS['bg'])
    main_frame.grid(row=1, column=0, sticky='nsew')

    # Configurar grid responsivo
    tab_nueva.columnconfigure(0, weight=1)
    tab_nueva.rowconfigure(1, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)

    # Función para enviar comandos MQTT
    def send_command(topic, message):
        try:
            client.publish(topic, message)
            print(f"📤 Enviado por MQTT → {topic}: {message}")
        except Exception as e:
            print(f"❌ Error al enviar MQTT: {e}")

    # Función para crear tarjetas de control
    def create_motor_card(parent, title, row, left_cmd, right_cmd=None, up_cmd=None, down_cmd=None):
        # Marco de la tarjeta
        card = tk.Frame(parent, bg=COLORS['card_bg'], relief='flat', borderwidth=1)
        card.grid(row=row, column=0, columnspan=3, padx=10, pady=8, sticky='ew')
        
        # Título del motor
        title_label = tk.Label(
            card, 
            text=title, 
            font=('JetBrains Mono', 12, 'bold'),
            bg=COLORS['card_bg'],
            fg=COLORS['accent'],
            pady=10
        )
        title_label.grid(row=0, column=0, columnspan=3)
        
        if up_cmd and down_cmd:  # Control vertical (Motor 3)
            up_btn = tk.Button(
                card, 
                text="⬆ SUBIR", 
                bg=COLORS['button_normal'],
                fg=COLORS['text'],
                activebackground=COLORS['button_hover'],
                activeforeground=COLORS['text'],
                command=up_cmd, 
                **button_style
            )
            up_btn.grid(row=1, column=1, padx=5, pady=5)
            up_btn.bind("<Enter>", on_enter)
            up_btn.bind("<Leave>", on_leave)
            
            down_btn = tk.Button(
                card, 
                text="⬇ BAJAR", 
                bg=COLORS['button_normal'],
                fg=COLORS['text'],
                activebackground=COLORS['button_hover'],
                activeforeground=COLORS['text'],
                command=down_cmd, 
                **button_style
            )
            down_btn.grid(row=2, column=1, padx=5, pady=5)
            down_btn.bind("<Enter>", on_enter)
            down_btn.bind("<Leave>", on_leave)
            
        else:  # Control horizontal
            left_btn = tk.Button(
                card, 
                text="⟵ IZQUIERDA", 
                bg=COLORS['button_normal'],
                fg=COLORS['text'],
                activebackground=COLORS['button_hover'],
                activeforeground=COLORS['text'],
                command=left_cmd, 
                **button_style
            )
            left_btn.grid(row=1, column=0, padx=5, pady=5)
            left_btn.bind("<Enter>", on_enter)
            left_btn.bind("<Leave>", on_leave)
            
            right_btn = tk.Button(
                card, 
                text="⟶ DERECHA", 
                bg=COLORS['button_normal'],
                fg=COLORS['text'],
                activebackground=COLORS['button_hover'],
                activeforeground=COLORS['text'],
                command=right_cmd, 
                **button_style
            )
            right_btn.grid(row=1, column=2, padx=5, pady=5)
            right_btn.bind("<Enter>", on_enter)
            right_btn.bind("<Leave>", on_leave)
        
        return card

    # Crear tarjetas de control para cada motor
    create_motor_card(main_frame, "🔄 MOTOR 1 - BASE", 1,
                    lambda: send_command("control/motor1", "LEFT"),
                    lambda: send_command("control/motor1", "RIGHT"))

    create_motor_card(main_frame, "📏 MOTOR 3 - ALTURA", 2,
                    None,
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
    status_frame = tk.Frame(main_frame, bg=COLORS['card_bg'], relief='flat')
    status_frame.grid(row=5, column=0, columnspan=3, pady=20, sticky='ew')

    status_label_nueva = tk.Label(
        status_frame, 
        text="✅ Conectado al broker MQTT", 
        font=('JetBrains Mono', 9), 
        bg=COLORS['card_bg'], 
        fg=COLORS['success']
    )
    status_label_nueva.pack()

    # Footer
    footer_label = tk.Label(
        main_frame, 
        text="Arch Linux + Hyprland 🐧", 
        font=('JetBrains Mono', 8), 
        bg=COLORS['bg'], 
        fg='#888888'
    )
    footer_label.grid(row=6, column=0, columnspan=3, pady=(10, 0))

    # Configurar tamaño inicial de la ventana
    root.update_idletasks()
    root.minsize(450, 650)
    root.geometry("500x700")

    root.mainloop()

if __name__ == "__main__":
    create_gui()