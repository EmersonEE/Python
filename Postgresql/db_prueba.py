import psycopg2

# Datos de conexión
host = "localhost"
dbname = "postgres"       # Cambia esto si ya tienes otra base de datos
user = "emerson"
password = "kuto123"
port = 5432

try:
    # Establecer conexión
    conexion = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )

    print("✅ Conexión exitosa a PostgreSQL")

    # Crear cursor
    cursor = conexion.cursor()

    # Ejecutar una consulta de prueba
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Versión de PostgreSQL:", version[0])

    # Cerrar cursor y conexión
    cursor.close()
    conexion.close()

except Exception as e:
    print("❌ Error al conectar con PostgreSQL:")
    print(e)
