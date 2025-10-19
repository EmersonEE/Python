import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("Interfaz con Botones")

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

    # Función para actualizar el texto mostrado
    def update_status():
        if left_selected and right_selected:
            status_label.config(text=f"Combinación: {left_selected} + {right_selected}")
        elif left_selected:
            status_label.config(text=f"Seleccionado: {left_selected}")
        elif right_selected:
            status_label.config(text=f"Seleccionado: {right_selected}")
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
        update_status()

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
        update_status()

    # Función para reiniciar todo
    def reset_buttons():
        nonlocal first_side_clicked, left_selected, right_selected
        first_side_clicked = None
        left_selected = None
        right_selected = None
        for btn in left_buttons + right_buttons:
            btn.config(bg="#d9d9d9", state="normal")
        status_label.config(text="Presiona un botón...")

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
    reset_button = tk.Button(root, text="Reiniciar", width=20, height=2, command=reset_buttons, bg="#d9d9d9")
    reset_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
