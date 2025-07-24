import os

# Ruta de la carpeta donde están los archivos
carpeta = "/mnt/DiscoPrincipal/perez/Documentos/Cursos/Ingles/Nivel Avanzado/"  # <-- CAMBIA ESTO

# Recorremos todos los archivos en la carpeta
for nombre in os.listdir(carpeta):
    # Verificamos si el archivo comienza con 'AI_2_' y termina en '.mp4'
    if nombre.startswith("AI_3_") and ".mp4" in nombre:
        nuevo_nombre = nombre.split(" ")[0]  # Eliminamos todo después del espacio
        ruta_original = os.path.join(carpeta, nombre)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        
        # Renombramos solo si el nuevo nombre es diferente
        if ruta_original != ruta_nueva:
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrado: {nombre} → {nuevo_nombre}")
