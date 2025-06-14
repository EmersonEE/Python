import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
load_dotenv()

password = os.getenv("PASSWORD")
email_sender = os.getenv("EMAIL")

email_reciver = "perezemerson85@gmail.com"

fecha = "2025-06-13"
nombre = "Juan Pérez"
carnet = "202512345"

body = f"""
Estimado/a Encargado,

Le saludamos cordialmente del sistema de control de asistencias. Le informamos que el estudiante asociado a su contacto no ha registrado su asistencia el día de hoy.

Es importante que esté al tanto de esta situación y, si considera necesario, se comunique con el estudiante para conocer el motivo de su ausencia.

Detalles:
📅 Fecha de inasistencia: {fecha}
👤 Estudiante: {nombre}
🆔 Carnet: {carnet}

Si tiene alguna duda o necesita más información, no dude en contactarnos.

Atentamente,

Sistema de Gestión de Asistencias
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = "Asistencia"
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
    print("Correo enviado exitosamente.")
