import time

# --- Configuración del Footprint ---
MODULE_NAME = "ESP32_DevKit_38Pin"
PIN_COUNT_TOTAL = 38
PAD_WIDTH = 2.2  # Ancho del pad de cobre
PAD_HEIGHT = 1.9 # Alto del pad de cobre
DRILL_SIZE = 1.0   # Diámetro de la perforación

PIN_PITCH = 2.54       # Distancia vertical entre pines
ROW_SPACING = 25.4     # Distancia horizontal entre las dos filas de pines
# ------------------------------------

def generate_footprint():
    """
    Genera el contenido del archivo .kicad_mod para un ESP32 de 38 pines.
    """
    # --- Metadatos del archivo ---
    timestamp = int(time.time())
    file_content = [
        f"(module {MODULE_NAME} (layer F.Cu) (tedit {timestamp})",
        "  (fp_text reference REF** (at 0 -15) (layer F.SilkS) (effects (font (size 1 1) (thickness 0.15))))",
        "  (fp_text value ESP32_DevKit_38Pin (at 0 15) (layer F.Fab) (effects (font (size 1 1) (thickness 0.15))))",
        "  (descr \"Footprint for 38-pin ESP32 Development Board, 2.54mm pitch, 25.4mm row spacing\")",
        "  (tags \"ESP32 DevKit DOIT\")"
    ]

    # --- Gráficos (Contorno en Serigrafía y Fabricación) ---
    half_row_spacing = ROW_SPACING / 2
    board_height = (PIN_COUNT_TOTAL / 2 - 1) * PIN_PITCH + 4 # Altura estimada del PCB
    half_board_height = board_height / 2
    
    file_content.extend([
        f"  (fp_line (start {-half_row_spacing - 2} {-half_board_height}) (end {half_row_spacing + 2} {-half_board_height}) (layer F.SilkS) (width 0.15))",
        f"  (fp_line (start {half_row_spacing + 2} {-half_board_height}) (end {half_row_spacing + 2} {half_board_height}) (layer F.SilkS) (width 0.15))",
        f"  (fp_line (start {half_row_spacing + 2} {half_board_height}) (end {-half_row_spacing - 2} {half_board_height}) (layer F.SilkS) (width 0.15))",
        f"  (fp_line (start {-half_row_spacing - 2} {half_board_height}) (end {-half_row_spacing - 2} {-half_board_height}) (layer F.SilkS) (width 0.15))"
    ])
    
    # --- Generación de Pads ---
    pins_per_row = PIN_COUNT_TOTAL // 2
    y_start = -((pins_per_row - 1) * PIN_PITCH) / 2

    # Fila Izquierda (Pines 1 a 19)
    for i in range(pins_per_row):
        pin_num = i + 1
        x_pos = -half_row_spacing
        y_pos = y_start + (i * PIN_PITCH)
        pad_line = f"  (pad {pin_num} thru_hole rect (at {x_pos:.2f} {y_pos:.2f}) (size {PAD_WIDTH} {PAD_HEIGHT}) (drill {DRILL_SIZE}) (layers *.Cu *.Mask))"
        file_content.append(pad_line)

    # Fila Derecha (Pines 20 a 38)
    for i in range(pins_per_row):
        pin_num = i + pins_per_row + 1
        x_pos = half_row_spacing
        # La numeración en la fila derecha va en sentido contrario para que el pin 38 quede frente al 1
        y_pos = y_start + ((pins_per_row - 1 - i) * PIN_PITCH)
        pad_line = f"  (pad {pin_num} thru_hole rect (at {x_pos:.2f} {y_pos:.2f}) (size {PAD_WIDTH} {PAD_HEIGHT}) (drill {DRILL_SIZE}) (layers *.Cu *.Mask))"
        file_content.append(pad_line)
        
    # Pin 1 marcado con un rectángulo en la serigrafía
    pin1_marker_y = y_start
    file_content.append(f"  (fp_line (start {-half_row_spacing-1.5} {pin1_marker_y-1.5}) (end {-half_row_spacing+1.5} {pin1_marker_y-1.5}) (layer F.SilkS) (width 0.15))")
    file_content.append(f"  (fp_line (start {-half_row_spacing+1.5} {pin1_marker_y-1.5}) (end {-half_row_spacing+1.5} {pin1_marker_y+1.5}) (layer F.SilkS) (width 0.15))")
    file_content.append(f"  (fp_line (start {-half_row_spacing+1.5} {pin1_marker_y+1.5}) (end {-half_row_spacing-1.5} {pin1_marker_y+1.5}) (layer F.SilkS) (width 0.15))")
    file_content.append(f"  (fp_line (start {-half_row_spacing-1.5} {pin1_marker_y+1.5}) (end {-half_row_spacing-1.5} {pin1_marker_y-1.5}) (layer F.SilkS) (width 0.15))")


    # --- Cierre del archivo ---
    file_content.append(")")
    
    return "\n".join(file_content)

if __name__ == "__main__":
    footprint_data = generate_footprint()
    print(footprint_data)