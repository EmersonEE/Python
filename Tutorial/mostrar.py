import os

# Ruta a la carpeta con los archivos .step
ruta_base = "/mnt/DiscoPrincipal/perez/Documentos/Altium Designer/3D Models/Resistencias 0.25W"

# Lista para almacenar las variantes
variantes = []

# Recorremos los archivos en la carpeta
for archivo in os.listdir(ruta_base):
    if archivo.endswith(".step"):
        # Extraer nombre de resistencia: elimina "R" al inicio y "_L..." al final
        nombre_resistencia = archivo.replace("R", "").split("_")[0]
        
        # Agrega una tupla con el nombre y la ruta completa
        ruta_completa = os.path.join(ruta_base, archivo)
        variantes.append((nombre_resistencia, ruta_completa))

# Mostrar resultado
for v in sorted(variantes):
    print(v)
