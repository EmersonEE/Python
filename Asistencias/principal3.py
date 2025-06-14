import os
import cv2
import numpy as np
import time
from pyzbar.pyzbar import decode
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter
import qrcode
from PIL import Image, ImageTk
import math
import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
load_dotenv()

# Configuración de correo electrónico
password = os.getenv("PASSWORD")
email_sender = os.getenv("EMAIL")


NOMBRE_CARNET = 'nombre_carnet.xlsx'
DIR_ASISTENCIAS = 'Asistencias'
ARCHIVO_USUARIOS = 'usuarios_creados.xlsx'
DIR_QRS = os.path.join(DIR_ASISTENCIAS, "QRs")
ARCHIVO_ASISTENCIAS = os.path.join(DIR_ASISTENCIAS, 'asistencia.xlsx')
COLUMNAS_ASISTENCIAS = ["Nombre", "Carnet", "Fecha", "Hora"]
# COLUMNAS_USUARIO= ["Nombre","Carnet" "Edad","Telefono","Encargado","Telefono Encargado","Correo Encargado"]
COLUMNAS_USUARIO = [
    "Nombre", "Carnet", "Edad", "Telefono", 
    "Encargado", "Telefono Encargado", "Correo Encargado", 
    "Carrera", "Estado"  # Agregamos Carrera y Estado
]
COLUMNAS_NC = ["Carnet", "Nombre"]
class SistemaAsistenciasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Asistencias")
        self.root.geometry("1000x700")
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        
        # Variables para la cámara
        self.cap = None
        self.running = False
        
        # Crear el notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Crear las pestañas
        self.crear_pestana_registro()
        self.crear_pestana_asistencia()
        self.crear_pestana_reportes()
        self.crear_pestana_verificacion()
        
        # Inicializar directorios y archivos
        self.inicializar_directorios()
        self.inicializar_archivo_asistencias()
    
    def inicializar_directorios(self):
        os.makedirs(DIR_QRS, exist_ok=True)

    def generar_chivos(self, archivo, columnas):
        if not os.path.exists(archivo):
            print("El Archivo No Existe, Creando Uno Nuevo...")
            wb = Workbook()
            ws = wb.active
            ws.title = "Datos"
            for idx, columna in enumerate(columnas, start=1):
                letra = get_column_letter(idx)
                ws[f"{letra}1"] = columna
            wb.save(archivo)
        else:
            print("El Archivo ya existe, Agregando Datos..")
            wb = load_workbook(archivo)
            ws = wb.active
    def obtener_siguiente_carnet(self,NOMBRE_CARNET):
        try:
            wb = load_workbook(NOMBRE_CARNET)
            ws = wb.active
            carnets = []
            for row in ws.iter_rows(min_row=2, values_only=True):  
                if row[1] is not None:
                    carnets.append(int(row[1]))
            if carnets:
                return str(max(carnets) + 1)
            else:
                return "202500000"
        except FileNotFoundError:
            return "202500000"

    def agregar_datos_nqr(self, nombre, carnet):
        self.generar_chivos(NOMBRE_CARNET, COLUMNAS_NC)
        wb = load_workbook(NOMBRE_CARNET)
        ws = wb.active
        nueva_fila = [nombre, carnet]
        ws.append(nueva_fila)
        wb.save(NOMBRE_CARNET)
    

    def crear_qr(self,nombre, carnet):
        qr_data = f"Carnet: {carnet}\nNombre: {nombre}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        ruta = os.path.join(DIR_QRS, f"{carnet}.png")
        if not os.path.exists(DIR_QRS):
            os.makedirs(DIR_QRS)
        img.save(ruta)  

    def agregar_datos_usuario(self, nombre, carnet, edad, telefono, nombre_encargado, telefono_encargado, correo_encargado):
        self.generar_chivos(ARCHIVO_USUARIOS, COLUMNAS_USUARIO)
        wb = load_workbook(ARCHIVO_USUARIOS)
        ws = wb.active
        nueva_fila = [nombre, carnet, edad, telefono, nombre_encargado, telefono_encargado, correo_encargado]
        for row in ws.iter_rows(min_row=6, values_only=True):
            if row[0] == nombre and row[1] == carnet and row[2] == edad and row[3] == telefono and row[4] == nombre_encargado and row[5] == telefono_encargado and row[6] == correo_encargado:
                print("El Usuario ya existe")
                return
        ws.append(nueva_fila)
        wb.save(ARCHIVO_USUARIOS)
        self.agregar_datos_nqr(nombre, carnet)
        self.crear_qr(nombre, carnet)
        print("Usuario Agregado")
            
    def inicializar_archivo_asistencias(self):
        """Crea el archivo de asistencias con las columnas necesarias si no existe"""
        if not os.path.exists(ARCHIVO_ASISTENCIAS):
            wb = Workbook()
            ws = wb.active
            ws.title = "Datos"
            for idx, columna in enumerate(COLUMNAS_ASISTENCIAS, start=1):
                letra = get_column_letter(idx)
                ws[f"{letra}1"] = columna
            wb.save(ARCHIVO_ASISTENCIAS)
    
    def crear_pestana_registro(self):
        """Crea la pestaña de registro de usuarios"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Registro de Usuarios")
        
        # Encabezado
        ttk.Label(frame, text="Registro de Nuevo Usuario", style='Header.TLabel').grid(
            row=0, column=0, columnspan=2, pady=10)
        
        # Campos del formulario
        campos = [
            ("Nombre:", "nombre_entry"),
            ("Edad:", "edad_entry"),
            ("Teléfono (8 dígitos):", "telefono_entry"),
            ("Nombre del Encargado:", "encargado_entry"),
            ("Teléfono Encargado (8 dígitos):", "telefono_encargado_entry"),
            ("Correo del Encargado:", "correo_entry"),
            ("Carrera:", "carrera_entry")
        ]
        
        for i, (texto, nombre) in enumerate(campos, start=1):
            ttk.Label(frame, text=texto).grid(row=i, column=0, sticky=tk.W, padx=10, pady=5)
            entry = ttk.Entry(frame, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            setattr(self, nombre, entry)
        
        # Botón de registro
        ttk.Button(frame, text="Registrar Usuario", command=self.registrar_usuario).grid(
            row=len(campos)+1, column=0, columnspan=2, pady=20)
        
        # Área de mensajes
        self.registro_message = ttk.Label(frame, text="", foreground='green')
        self.registro_message.grid(row=len(campos)+2, column=0, columnspan=2)
    
    def crear_pestana_asistencia(self):
        """Crea la pestaña para tomar asistencia con QR"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Tomar Asistencia")
        
        # Encabezado
        ttk.Label(frame, text="Tomar Asistencia con Cámara QR", style='Header.TLabel').grid(
            row=0, column=0, columnspan=2, pady=10)
        
        # Canvas para mostrar la cámara
        self.canvas = tk.Canvas(frame, width=640, height=480)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Botones
        ttk.Button(frame, text="Iniciar Cámara", command=self.iniciar_camara).grid(
            row=2, column=0, pady=10, padx=5, sticky=tk.E)
        ttk.Button(frame, text="Detener Cámara", command=self.detener_camara).grid(
            row=2, column=1, pady=10, padx=5, sticky=tk.W)
        
        # Área de mensajes
        self.asistencia_message = ttk.Label(frame, text="", foreground='blue')
        self.asistencia_message.grid(row=3, column=0, columnspan=2)
    
    def crear_pestana_reportes(self):
        """Crea la pestaña para generar reportes"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Reportes")
        
        # Encabezado
        ttk.Label(frame, text="Generar Reporte de Asistencias", style='Header.TLabel').grid(
            row=0, column=0, columnspan=2, pady=10)
        
        # Fecha para el reporte
        ttk.Label(frame, text="Fecha del Reporte (YYYY-MM-DD):").grid(
            row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.fecha_reporte_entry = ttk.Entry(frame, width=20)
        self.fecha_reporte_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        self.fecha_reporte_entry.insert(0, time.strftime("%Y-%m-%d"))
        
        # Botón para generar reporte
        ttk.Button(frame, text="Generar Reporte", command=self.generar_reporte).grid(
            row=2, column=0, columnspan=2, pady=10)
        
        # Área para mostrar el reporte
        self.reporte_text = tk.Text(frame, height=20, width=80, wrap=tk.WORD)
        self.reporte_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, command=self.reporte_text.yview)
        scrollbar.grid(row=3, column=2, sticky='nsew')
        self.reporte_text['yscrollcommand'] = scrollbar.set
        
        # Botón para exportar reporte
        ttk.Button(frame, text="Exportar Reporte", command=self.exportar_reporte).grid(
            row=4, column=0, columnspan=2, pady=10)
    
    def crear_pestana_verificacion(self):
        """Crea la pestaña para verificar asistencias"""
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Verificación")
        
        # Encabezado
        ttk.Label(frame, text="Verificar Asistencias por Fecha", style='Header.TLabel').grid(
            row=0, column=0, columnspan=2, pady=10)
        
        # Fecha para verificación
        ttk.Label(frame, text="Fecha a Verificar (YYYY-MM-DD):").grid(
            row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.fecha_verificacion_entry = ttk.Entry(frame, width=20)
        self.fecha_verificacion_entry.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        self.fecha_verificacion_entry.insert(0, time.strftime("%Y-%m-%d"))
        
        # Botón para verificar
        ttk.Button(frame, text="Verificar Asistencias", command=self.verificar_asistencias).grid(
            row=2, column=0, columnspan=2, pady=10)
        
        # Treeview para mostrar resultados
        columns = ('nombre', 'carnet', 'estado', 'correo')
        self.tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)
        
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('carnet', text='Carnet')
        self.tree.heading('estado', text='Estado')
        self.tree.heading('correo', text='Correo Encargado')
        
        self.tree.column('nombre', width=200)
        self.tree.column('carnet', width=100)
        self.tree.column('estado', width=100)
        self.tree.column('correo', width=200)
        
        self.tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=3, column=2, sticky='ns')
        
        # Botón para enviar notificaciones
        ttk.Button(frame, text="Enviar Notificaciones a Ausentes", command=self.enviar_notificaciones).grid(
            row=4, column=0, columnspan=2, pady=10)
    
    # Funciones de la aplicación
    def registrar_usuario(self):
        """Registra un nuevo usuario en el sistema"""
        try:
            # Obtener datos del formulario
            nombre = self.nombre_entry.get().strip()
            edad = self.edad_entry.get().strip()
            telefono = self.telefono_entry.get().strip()
            encargado = self.encargado_entry.get().strip()
            telefono_encargado = self.telefono_encargado_entry.get().strip()
            correo = self.correo_entry.get().strip()
            carrera = self.carrera_entry.get().strip()
            
            # Validaciones básicas
            if not all([nombre, edad, telefono, encargado, telefono_encargado, correo, carrera]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
                
            if not edad.isdigit() or int(edad) <= 0:
                messagebox.showerror("Error", "La edad debe ser un número positivo")
                return
                
            if not telefono.isdigit() or len(telefono) != 8:
                messagebox.showerror("Error", "El teléfono debe tener 8 dígitos")
                return
                
            if not telefono_encargado.isdigit() or len(telefono_encargado) != 8:
                messagebox.showerror("Error", "El teléfono del encargado debe tener 8 dígitos")
                return
                
            # Obtener carnet automático
            carnet = self.obtener_siguiente_carnet(NOMBRE_CARNET)
            
            # Registrar usuario
            self.agregar_datos_usuario(nombre, carnet, edad, telefono, encargado, telefono_encargado, correo)
            
            # Mostrar mensaje de éxito
            self.registro_message.config(text=f"Usuario {nombre} registrado exitosamente con carnet {carnet}")
            
            # Limpiar campos
            for entry in [self.nombre_entry, self.edad_entry, self.telefono_entry, 
                          self.encargado_entry, self.telefono_encargado_entry, 
                          self.correo_entry, self.carrera_entry]:
                entry.delete(0, tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar el usuario: {str(e)}")
    
    def iniciar_camara(self):
        """Inicia la cámara para leer códigos QR"""
        if self.running:
            return
            
        self.running = True
        self.cap = cv2.VideoCapture(0)
        self.asistencia_message.config(text="Escanea el código QR... Presiona 'Detener Cámara' para salir.")
        self.leer_qr()
    
    def detener_camara(self):
        """Detiene la cámara"""
        self.running = False
        if self.cap:
            self.cap.release()
            self.cap = None
        self.asistencia_message.config(text="Cámara detenida")

    def verificar_carnet(self,carnet: str) -> bool:
        """Verifica si el carnet existe en la base de datos"""
        try:
            wb = load_workbook(NOMBRE_CARNET)
            ws = wb.active
            for row in ws.iter_rows(values_only=True):
                if row[1] == carnet:
                    print("Carnet Correcto")
                    return True
            print("Carnet Inválido")
            return False
        except Exception as e:
            print(f"Error al verificar carnet: {e}")
            return False
        
    
    def registrar_asistencia(self,nombre: str, carnet: str) -> bool:
        """Registra la asistencia en el archivo Excel si no está ya registrada"""
        try:
            wb = load_workbook(ARCHIVO_ASISTENCIAS)
            ws = wb.active
            
            fecha_actual = time.strftime("%Y-%m-%d")
            hora_actual = time.strftime("%H:%M:%S")
            
            for row in ws.iter_rows(min_row=2, values_only=True):
                if row[1] == carnet and row[2] == fecha_actual:
                    print("La asistencia ya fue registrada hoy.")
                    return False
            
            nueva_fila = [nombre, carnet, fecha_actual, hora_actual]
            ws.append(nueva_fila)
            wb.save(ARCHIVO_ASISTENCIAS)
            print("Asistencia registrada exitosamente.")
            return True
        except Exception as e:
            print(f"Error al registrar asistencia: {e}")
            return False
    def procesar_datos_qr(self,data: str) -> tuple:
        """Extrae y valida los datos del QR"""
        try:
            if "Carnet:" not in data or "Nombre:" not in data:
                print("Formato incorrecto: faltan 'Carnet:' o 'Nombre:' en la cadena.")
                return None, None
            
            carnet = data.split("Carnet:")[1].split("Nombre:")[0].strip()
            nombre = data.split("Nombre:")[1].strip()
            return nombre, carnet
        except Exception as e:
            print(f"Error al procesar QR: {e}")
            return None, None
    
        
    def leer_qr(self):
        """Lee códigos QR de la cámara"""
        if not self.running or not self.cap:
            return
            
        ret, frame = self.cap.read()
        if ret:
            # Convertir a formato que tkinter puede mostrar
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            
            # Mostrar en el canvas
            self.canvas.imgtk = imgtk
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            
            # Decodificar códigos QR
            codigos = decode(frame)
            if codigos:
                for codigo in codigos:
                    try:
                        data = codigo.data.decode('utf-8')
                        nombre, carnet = self.procesar_datos_qr(data)
                        
                        if nombre and carnet and self.verificar_carnet(carnet):
                            if self.registrar_asistencia(nombre, carnet):
                                self.asistencia_message.config(
                                    text=f"Asistencia registrada: {nombre} ({carnet})", 
                                    foreground='green')
                        else:
                            self.asistencia_message.config(
                                text="Código QR no válido", 
                                foreground='red')
                            
                    except Exception as e:
                        print(f"Error al procesar código QR: {e}")
        
        # Llamar de nuevo después de 10ms
        if self.running:
            self.root.after(10, self.leer_qr)

    def obtener_lista_usuarios(self):
        """Obtiene la lista completa de usuarios registrados"""
        try:
            wb = load_workbook(ARCHIVO_USUARIOS)
            ws = wb.active
            usuarios = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                if row[0]:  # Si tiene nombre
                    usuarios.append({
                        'Nombre': row[0],
                        'Carnet': row[1],
                        'Correo Encargado': row[6] if len(row) > 6 else 'No especificado',
                        'Carrera': row[7] if len(row) > 7 else 'No especificado'
                    })
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def obtener_asistencias_por_fecha(self,fecha):
        """Obtiene las asistencias de una fecha específica"""
        try:
            wb = load_workbook(ARCHIVO_ASISTENCIAS)
            ws = wb.active
            asistencias = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                if row[2] == fecha:
                    asistencias.append(row[1])  # Guardamos solo el carnet
            return asistencias
        except Exception as e:
            print(f"Error al obtener asistencias: {e}")
            return []
    
    def generar_reporte(self):
        """Genera un reporte de asistencias para la fecha especificada"""
        try:
            fecha = self.fecha_reporte_entry.get().strip()
            
            # Validar formato de fecha
            if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
                messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD")
                return
                
            # Obtener datos
            usuarios = self.obtener_lista_usuarios()
            asistencias = self.obtener_asistencias_por_fecha(fecha)
            
            presentes = []
            ausentes = []
            
            for usuario in usuarios:
                if usuario['Carnet'] in asistencias:
                    presentes.append(usuario)
                else:
                    ausentes.append(usuario)
            
            # Mostrar en el área de texto
            self.reporte_text.delete(1.0, tk.END)
            self.reporte_text.insert(tk.END, f"=== Reporte de Asistencias ===\n")
            self.reporte_text.insert(tk.END, f"Fecha: {fecha}\n\n")
            
            self.reporte_text.insert(tk.END, f"Presentes ({len(presentes)}):\n")
            for usuario in presentes:
                self.reporte_text.insert(tk.END, f"- {usuario['Nombre']} ({usuario['Carnet']}) - {usuario['Carrera']}\n")
            
            self.reporte_text.insert(tk.END, f"\nAusentes ({len(ausentes)}):\n")
            for usuario in ausentes:
                self.reporte_text.insert(tk.END, f"- {usuario['Nombre']} ({usuario['Carnet']}) - {usuario['Carrera']}\n")
            
            messagebox.showinfo("Éxito", "Reporte generado correctamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al generar el reporte: {str(e)}")
    
    def exportar_reporte(self):
        """Exporta el reporte a un archivo de texto"""
        try:
            # Obtener el texto del reporte
            reporte = self.reporte_text.get(1.0, tk.END)
            if not reporte.strip():
                messagebox.showwarning("Advertencia", "No hay reporte para exportar")
                return
                
            # Pedir ubicación para guardar
            fecha = self.fecha_reporte_entry.get().strip()
            default_filename = f"reporte_asistencia_{fecha}.txt"
            
            filepath = filedialog.asksaveasfilename(
                defaultextension=".txt",
                initialfile=default_filename,
                filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
                
            if filepath:
                with open(filepath, 'w') as f:
                    f.write(reporte)
                messagebox.showinfo("Éxito", f"Reporte exportado a:\n{filepath}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al exportar el reporte: {str(e)}")
    
    def verificar_asistencias(self):
        """Verifica las asistencias para una fecha específica"""
        try:
            fecha = self.fecha_verificacion_entry.get().strip()
            
            # Validar formato de fecha
            if len(fecha) != 10 or fecha[4] != '-' or fecha[7] != '-':
                messagebox.showerror("Error", "Formato de fecha inválido. Use YYYY-MM-DD")
                return
                
            # Limpiar treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
                
            # Obtener datos
            wb_usuarios = load_workbook(ARCHIVO_USUARIOS)
            ws_usuarios = wb_usuarios.active
            todos_usuarios = [
                (row[0], str(row[1]), row[6] ) # nombre, carnet, correo encargado
                for row in ws_usuarios.iter_rows(min_row=2, values_only=True)
            ]
            
            wb_asistencias = load_workbook(ARCHIVO_ASISTENCIAS)
            ws_asistencias = wb_asistencias.active
            asistencias_fecha = [
                (row[0], str(row[1])) 
                for row in ws_asistencias.iter_rows(min_row=2, values_only=True)
                if row[2] == fecha
            ]

            carnets_asistieron = set(c[1] for c in asistencias_fecha)
            
            # Mostrar en el treeview
            for nombre, carnet, correo_tutor in todos_usuarios:
                if carnet in carnets_asistieron:
                    estado = "PRESENTE"
                    tags = ('presente',)
                else:
                    estado = "AUSENTE"
                    tags = ('ausente',)
                
                self.tree.insert('', tk.END, values=(nombre, carnet, estado, correo_tutor), tags=tags)
            
            # Configurar colores
            self.tree.tag_configure('presente', foreground='green')
            self.tree.tag_configure('ausente', foreground='red')
            
            messagebox.showinfo("Éxito", "Verificación de asistencias completada")
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al verificar asistencias: {str(e)}")

    def enviar_correo(self,destinatario,fecha,nombre,carnet):
        """Envía un correo electrónico con el asunto y cuerpo especificados"""

        cuerpo = f"""
        Estimado/a Encargado,

        Le saludamos cordialmente del sistema de control de asistencias. Le informamos que el estudiante asociado a su contacto no ha registrado su asistencia el día de hoy.

        Es importante que esté al tanto de esta situación y, si considera necesario, se comunique con el estudiante para conocer el motivo de su ausencia.

        Detalles:
        📅 Fecha de inasistencia: {fecha}
        🆔 Carnet: {carnet}
        👤 Estudiante: {nombre}

        Si tiene alguna duda o necesita más información, no dude en contactarnos.

        Atentamente,

        Sistema de Gestión de Asistencias
        """

        em = EmailMessage()
        em["From"] = email_sender
        em["To"] = destinatario
        em["Subject"] = "Asistencia"
        em.set_content(cuerpo)
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.sendmail(email_sender, destinatario, em.as_string())
                print("Correo enviado exitosamente.")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
        
    def enviar_notificaciones(self):
        """Envía notificaciones por correo a los ausentes"""
        try:
            # Obtener ausentes del treeview
            ausentes = []
            for item in self.tree.get_children():
                values = self.tree.item(item, 'values')
                if values and values[2] == "AUSENTE":
                    ausentes.append({
                        'nombre': values[0],
                        'carnet': values[1],
                        'correo': values[3]
                    })
            
            if not ausentes:
                messagebox.showinfo("Información", "No hay ausentes para notificar")
                return
                
            # Confirmar envío
            confirmar = messagebox.askyesno(
                "Confirmar", 
                f"¿Desea enviar notificaciones a {len(ausentes)} ausentes?")
                
            if not confirmar:
                return
                
            # Enviar correos
            for ausente in ausentes:
                if ausente['correo'] and ausente['correo'].strip():
                    try:
                        self.enviar_correo(ausente['correo'].strip())
                        print(f"Notificación enviada a {ausente['nombre']} ({ausente['correo']})")
                    except Exception as e:
                        print(f"Error al enviar a {ausente['correo']}: {str(e)}")
            
            messagebox.showinfo("Éxito", "Proceso de notificación completado")
            
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al enviar notificaciones: {str(e)}")

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAsistenciasApp(root)
    root.mainloop()