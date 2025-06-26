import psycopg2
from psycopg2 import sql

# Configuración de conexión
DB_USER = "emerson"
DB_PASSWORD = "kuto123"
DB_HOST = "localhost"
DB_PORT = "5432"

def crear_base_datos():
    try:
        # Conexión inicial para crear la base de datos
        conn = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True  # Necesario para crear una base de datos
        cursor = conn.cursor()

        # Nombre de la base de datos
        db_name = "sistema_asistencias"

        # Verificar si la base de datos ya existe
        cursor.execute("SELECT datname FROM pg_database WHERE datname = %s;", (db_name,))
        exists = cursor.fetchone()

        if not exists:
            # Crear la base de datos
            cursor.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier(db_name)))
            print(f"Base de datos '{db_name}' creada exitosamente.")
        else:
            print(f"La base de datos '{db_name}' ya existe.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear la base de datos: {e}")

def crear_tablas():
    try:
        # Conexión a la nueva base de datos
        conn = psycopg2.connect(
            dbname="sistema_asistencias",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Crear tabla de usuarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                carnet VARCHAR(20) UNIQUE NOT NULL,
                edad INTEGER NOT NULL CHECK (edad > 0),
                telefono VARCHAR(8) NOT NULL CHECK (LENGTH(telefono) = 8),
                encargado VARCHAR(100) NOT NULL,
                telefono_encargado VARCHAR(8) NOT NULL CHECK (LENGTH(telefono_encargado) = 8),
                correo_encargado VARCHAR(100) NOT NULL,
                carrera VARCHAR(100) NOT NULL,
                estado VARCHAR(20) DEFAULT 'Activo'
            );
        """)
        print("Tabla 'usuarios' creada o ya existente.")

        # Crear tabla de asistencias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS asistencias (
                id SERIAL PRIMARY KEY,
                carnet VARCHAR(20) REFERENCES usuarios(carnet) ON DELETE CASCADE,
                fecha DATE NOT NULL,
                hora TIME NOT NULL,
                UNIQUE(carnet, fecha)
            );
        """)
        print("Tabla 'asistencias' creada o ya existente.")

        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error al crear las tablas: {e}")

if __name__ == "__main__":
    crear_base_datos()
    crear_tablas()