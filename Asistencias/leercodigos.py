import cv2
from pyzbar.pyzbar import decode
import numpy as np
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



def leer_qr_camara():
    cap = cv2.VideoCapture(0)  # Usar cámara 0 (predeterminada)

    print("Escanea el código QR con la cámara... Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo acceder a la cámara.")
            break

        # Decodificar los códigos QR en la imagen
        codigos = decode(frame)
        if codigos:
            for codigo in codigos:
                data = codigo.data.decode('utf-8')
                print("Código QR detectado:", data)
                ser.write(b'1')

                # Dibujar un rectángulo y mostrar el contenido
                puntos = codigo.polygon
                pts = [(p.x, p.y) for p in puntos]
                cv2.polylines(frame, [np.array(pts, np.int32)], True, (0,255,0), 3)
                x, y, w, h = codigo.rect
                cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        else:
            print("No se detectó ningún código QR.")
            ser.write(b'0')
        # Mostrar el video
        cv2.imshow("Lector de QR", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    ser.close()

# Llamar la función
leer_qr_camara()
