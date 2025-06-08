import tkinter as tk
from tkinter import ttk, scrolledtext
import os
import subprocess

class ESP32Uploader:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 ESP32 Project Uploader")
        self.root.geometry("600x400")
        self.root.configure(bg="#f4f4f4")

        # Diccionario de proyectos
        self.projects = {
            "Proyecto LED": "/home/emerson/Documentos/PlatformIO/Projects/Blink/.pio/build/esp32doit-devkit-v1/firmware.bin",
            # Puedes añadir más proyectos aquí
        }

        # Encabezado
        header = tk.Label(root, text="ESP32 Project Uploader", font=("Segoe UI", 16, "bold"), bg="#f4f4f4", fg="#333")
        header.pack(pady=10)

        # Frame para selección de proyecto
        frame = tk.Frame(root, bg="#f4f4f4")
        frame.pack(pady=10)

        label = tk.Label(frame, text="Selecciona un proyecto:", font=("Segoe UI", 12), bg="#f4f4f4")
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.project_var = tk.StringVar(root)
        self.project_var.set(list(self.projects.keys())[0])

        self.option_menu = ttk.Combobox(frame, textvariable=self.project_var, values=list(self.projects.keys()), state="readonly", width=40)
        self.option_menu.grid(row=0, column=1, padx=10, pady=5)

        # Botón de subida
        self.upload_btn = tk.Button(root, text="Subir al ESP32", command=self.upload,
                                    bg="#4CAF50", fg="white", font=("Segoe UI", 11, "bold"),
                                    relief="flat", padx=10, pady=5)
        self.upload_btn.pack(pady=10)

        # Consola de salida con scroll
        console_label = tk.Label(root, text="Consola:", font=("Segoe UI", 11), bg="#f4f4f4", anchor="w")
        console_label.pack(padx=10, anchor="w")

        self.console = scrolledtext.ScrolledText(root, height=10, font=("Courier", 10), bg="#ffffff", relief="solid", bd=1)
        self.console.pack(fill="both", expand=True, padx=10, pady=5)

    def upload(self):
        selected_project = self.project_var.get()
        project_path = os.path.dirname(self.projects[selected_project])
        port = "/dev/ttyUSB0"  # Ajusta según tu puerto

        try:
            bootloader_bin = os.path.join(project_path, "bootloader.bin")
            partitions_bin = os.path.join(project_path, "partitions.bin")
            firmware_bin = self.projects[selected_project]

            self.console.delete(1.0, tk.END)
            self.console.insert(tk.END, f"🔧 Subiendo {selected_project}...\n")
            self.root.update()

            cmd = [
                "python", "-m", "esptool",
                "--chip", "esp32",
                "--port", port,
                "--baud", "460800",
                "--before", "default_reset",
                "--after", "hard_reset",
                "write_flash", "-z",
                "--flash_mode", "dio",
                "--flash_freq", "40m",
                "--flash_size", "4MB",
                "0x1000", bootloader_bin,
                "0x8000", partitions_bin,
                "0x10000", firmware_bin
            ]

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            self.console.insert(tk.END, stdout.decode())
            if stderr:
                self.console.insert(tk.END, f"\n⚠️ Error:\n{stderr.decode()}")

            if process.returncode == 0:
                self.console.insert(tk.END, "\n✅ ¡Subida completada correctamente!\n")
            else:
                self.console.insert(tk.END, "\n❌ ¡Error en la subida!\n")

        except Exception as e:
            self.console.insert(tk.END, f"⚠️ Error: {str(e)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ESP32Uploader(root)
    root.mainloop()
