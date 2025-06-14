import serial
import time

esp32_port = '/dev/ttyUSB0'  # Cambia esto al puerto correcto de tu ESP32
baud_rate = 115200  # Asegúrate de que coincida con la configuración del ESP32  

time.sleep(2)  # Espera a que el puerto se inicialice
try:
    ser = serial.Serial(esp32_port, baud_rate, timeout=1)
    print(f"Conectado a {esp32_port} a {baud_rate} baudios.")
except serial.SerialException as e:
    print(f"Error al conectar al puerto {esp32_port}: {e}")
    exit()

while True:
    def toogle(key):
        if key == '1':
            ser.write(b'1')
        elif key == '0':
            ser.write(b'0')
        else:
            print("Tecla no válida. Usa '1' para encender o '0' para apagar.")
    key = input("Presiona '1' para encender el LED o '0' para apagarlo (q para salir): ")
    if key.lower() == 'q':
        print("Saliendo...")
        break
    toogle(key)

ser.close()