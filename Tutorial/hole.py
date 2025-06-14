import os

carpeta_donde_estan = "/home/emerson/Documentos/Python/footprints_generados"
salida_dir = "./nuevas"

hole = 1.9

os.makedirs(salida_dir, exist_ok=True)

leer = os.listdir(carpeta_donde_estan)

for nombre_archivo in leer:
    print(nombre_archivo)
    ruta_original = os.path.join(carpeta_donde_estan, nombre_archivo)

    with open(ruta_original, "r", encoding="utf-8") as f:
        contenido = f.read()
        contenido_modificado = contenido.replace('(size 1.6 1.6)', '(size 1.9 1.9)')
    
    ruta_nueva = os.path.join(salida_dir, nombre_archivo)

    with open(ruta_nueva, "w", encoding="utf-8") as f_nuevo:
        f_nuevo.write(contenido_modificado)

print("Archivos modificados guardados correctamente en", salida_dir)
