import os

# === Configuración del usuario ===
plantilla_path = "/home/emerson/Documentos/My_KiCad/MyLibreriaKiCad/Resistencias_0.25W.pretty/2.2K.kicad_mod"  # Ruta al archivo base
salida_dir = "./footprints_generados"  # Carpeta de salida
hole = 1.9
variantes = [
    ('1', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1_L8mm_0.25watts.step'),
    ('1.2K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.2K_L8mm_0.25watts.step'),
    ('1.2M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.2M_L8mm_0.25watts.step'),
    ('1.5', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.5_L8mm_0.25watts.step'),
    ('1.5K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.5K_L8mm_0.25watts.step'),
    ('1.5M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.5M_L8mm_0.25watts.step'),
    ('1.8', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.8_L8mm_0.25watts.step'),
    ('1.8K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.8K_L8mm_0.25watts.step'),
    ('1.8M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1.8M_L8mm_0.25watts.step'),
    ('10', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R10_L8mm_0.25watts.step'),
    ('100', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R100_L8mm_0.25watts.step'),
    ('100K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R100K_L8mm_0.25watts.step'),
    ('10K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R10K_L8mm_0.25watts.step'),
    ('10M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R10M_L8mm_0.25watts.step'),
    ('12', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R12_L8mm_0.25watts.step'),
    ('120', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R120_L8mm_0.25watts.step'),
    ('120K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R120K_L8mm_0.25watts.step'),
    ('12K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R12K_L8mm_0.25watts.step'),
    ('15', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R15_L8mm_0.25watts.step'),
    ('150', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R150_L8mm_0.25watts.step'),
    ('150K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R150K_L8mm_0.25watts.step'),
    ('15K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R15K_L8mm_0.25watts.step'),
    ('18', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R18_L8mm_0.25watts.step'),
    ('180', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R180_L8mm_0.25watts.step'),
    ('180K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R180K_L8mm_0.25watts.step'),
    ('18K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R18K_L8mm_0.25watts.step'),
    ('1K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1K_L8mm_0.25watts.step'),
    ('1M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R1M_L8mm_0.25watts.step'),
    ('2.2', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.2_L8mm_0.25watts.step'),
    ('2.2K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.2K_L8mm_0.25watts.step'),
    ('2.2M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.2M_L8mm_0.25watts.step'),
    ('2.7', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.7_L8mm_0.25watts.step'),
    ('2.7K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.7K_L8mm_0.25watts.step'),
    ('2.7M', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2.7M_L8mm_0.25watts.step'),
    ('200', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R200_L8mm_0.25watts.step'),
    ('20K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R20K_L8mm_0.25watts.step'),
    ('22', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R22_L8mm_0.25watts.step'),
    ('220', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R220_L8mm_0.25watts.step'),
    ('220K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R220K_L8mm_0.25watts.step'),
    ('22K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R22K_L8mm_0.25watts.step'),
    ('27', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R27_L8mm_0.25watts.step'),
    ('270', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R270_L8mm_0.25watts.step'),
    ('270K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R270K_L8mm_0.25watts.step'),
    ('27K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R27K_L8mm_0.25watts.step'),
    ('2K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R2K_L8mm_0.25watts.step'),
    ('3.3', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R3.3_L8mm_0.25watts.step'),
    ('3.3K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R3.3K_L8mm_0.25watts.step'),
    ('300K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R300K_L8mm_0.25watts.step'),
    ('33', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R33_L8mm_0.25watts.step'),
    ('33K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R33K_L8mm_0.25watts.step'),
    ('4.7K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R4.7K_L8mm_0.25watts.step'),
    ('47', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R47_L8mm_0.25watts.step'),
    ('470', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R470_L8mm_0.25watts.step'),
    ('470K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R470K_L8mm_0.25watts.step'),
    ('47K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R47K_L8mm_0.25watts.step'),
    ('5.1K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R5.1K_L8mm_0.25watts.step'),
    ('510', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R510_L8mm_0.25watts.step'),
    ('51K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R51K_L8mm_0.25watts.step'),
    ('56', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R56_L8mm_0.25watts.step'),
    ('6.8K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R6.8K_L8mm_0.25watts.step'),
    ('680', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R680_L8mm_0.25watts.step'),
    ('680K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R680K_L8mm_0.25watts.step'),
    ('68K', '/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W/R68K_L8mm_0.25watts.step'),
]


# Crear carpeta de salida si no existe
os.makedirs(salida_dir, exist_ok=True)

# Leer plantilla base
with open(plantilla_path, "r", encoding="utf-8") as f:
    base = f.read()

# Procesar cada variante
for nombre, ruta_3d in variantes:
    contenido = base

    # Cambiar nombre del footprint
    contenido = contenido.replace('(footprint "2.2K"', f'(footprint "{nombre}"')
    contenido = contenido.replace('(property "Value" "2.2K"', f'(property "Value" "{nombre}"')

    # Cambiar ruta del modelo 3D
    contenido = contenido.replace(
        "/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/R2.2K_L8mm_0.25watts.step",
        ruta_3d
    )

    # Guardar nuevo archivo
    nuevo_nombre = os.path.join(salida_dir, f"{nombre}.kicad_mod")
    with open(nuevo_nombre, "w", encoding="utf-8") as f_out:
        f_out.write(contenido)

    print(f"Generado: {nuevo_nombre}")
