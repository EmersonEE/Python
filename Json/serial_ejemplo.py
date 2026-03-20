import serial
import time
import json

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
ser.dtr = False
time.sleep(2)
ser.reset_input_buffer()


def leer_trama():
    buffer = ""

    while True:
        if ser.in_waiting:
            c = ser.read().decode("utf-8", errors="ignore")

            if c == "$":
                buffer = ""
            elif c == "#":
                return buffer
            else:
                buffer += c


print("Solicitando datos...")
ser.write(b"x")

trama = leer_trama()

try:
    data = json.loads(trama)
    print("Datos recibidos:", data)

    with open("secuencia_serial.json", "w") as f:
        json.dump(data, f, indent=4)

except:
    print("Error decodificando JSON")
    print(trama)

ser.close()
