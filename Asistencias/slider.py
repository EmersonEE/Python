from tkinter import *




import time
import paho.mqtt.client as mqtt

BROKER = "192.168.1.136"  
PORT = 1883              
TOPIC = "/brillo"   

cliente = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código: {rc}")

cliente.on_connect = on_connect

cliente.connect(BROKER, PORT, 60)

cliente.loop_start()


def update_label(value):
    my_label.config(text=f"Current Value: {value}")
    print(value)
    cliente.publish(TOPIC, value)

root = Tk()
root.title("Tkinter Slider with Command")
root.geometry("300x200")

slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="Adjust Value", command=update_label)
slider.pack(pady=20)
my_label = Label(root, text="Current Value: 0")

my_label.pack()


def on_closing():
    print("Closing application...")
    cliente.loop_stop()
    cliente.disconnect()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()