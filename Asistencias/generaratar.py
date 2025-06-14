from PIL import Image, ImageDraw, ImageFont, ImageOps
import qrcode
import random

def generar_color_pastel():
    """Genera un color pastel aleatorio"""
    return (
        random.randint(180, 255),
        random.randint(180, 255),
        random.randint(180, 255)
    )

# Datos de contacto
nombre = "Felipe Sáenz"
telefono = "(55) 1234 5678"
correo = "hola@sitioincreible.com"
empresa = "@sitioincreible"
sitio_web = "www.sitioincreible.com"

# Texto para QR
qr_data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{nombre}\nTEL:{telefono}\nEMAIL:{correo}\nORG:{empresa}\nURL:{sitio_web}\nEND:VCARD"

# Configuración de diseño
color_fondo = generar_color_pastel()
color_acento = (70, 130, 180)  # Azul acero
color_texto = (50, 50, 50)     # Gris oscuro

# Crear el QR con estilo
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=2,
)
qr.add_data(qr_data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color=color_acento, back_color="white")
qr_img = qr_img.resize((180, 180))

# Añadir borde decorativo al QR
qr_with_border = ImageOps.expand(qr_img, border=8, fill=color_acento)

# Crear imagen base (700x350 px)
img = Image.new("RGB", (700, 350), color_fondo)
draw = ImageDraw.Draw(img)

# Cargar fuentes (intenta varias opciones)
try:
    fuente_titulo = ImageFont.truetype("arialbd.ttf", 32)
    fuente_normal = ImageFont.truetype("arial.ttf", 22)
    fuente_empresa = ImageFont.truetype("ariali.ttf", 24)
except:
    try:
        fuente_titulo = ImageFont.truetype("DejaVuSans-Bold.ttf", 32)
        fuente_normal = ImageFont.truetype("DejaVuSans.ttf", 22)
        fuente_empresa = ImageFont.truetype("DejaVuSans-Oblique.ttf", 24)
    except:
        fuente_titulo = ImageFont.load_default()
        fuente_normal = ImageFont.load_default()
        fuente_empresa = ImageFont.load_default()

# Dibujar elementos decorativos
# Barra lateral
draw.rectangle([(0, 0), (30, 350)], fill=color_acento)
# Forma decorativa
draw.ellipse([(400, -100), (800, 200)], outline=color_acento, width=8)
# Línea decorativa
draw.line([(250, 300), (700, 300)], fill=color_acento, width=3)

# Dibujar texto con sombra para mejor legibilidad
shadow_offset = 2
shadow_color = (220, 220, 220)

# Nombre con sombra
draw.text((300+shadow_offset, 60+shadow_offset), nombre, fill=shadow_color, font=fuente_titulo)
draw.text((300, 60), nombre, fill=color_texto, font=fuente_titulo)

# Información de contacto
contact_info = [
    (f"📞 {telefono}", 100),
    (f"✉️ {correo}", 140),
    (f"🌐 {sitio_web}", 180)
]

for text, y in contact_info:
    draw.text((300+shadow_offset, y+shadow_offset), text, fill=shadow_color, font=fuente_normal)
    draw.text((300, y), text, fill=color_texto, font=fuente_normal)

# Empresa
draw.text((300+shadow_offset, 270+shadow_offset), empresa, fill=shadow_color, font=fuente_empresa)
draw.text((300, 270), empresa, fill=color_acento, font=fuente_empresa)

# Pegar el QR con borde
img.paste(qr_with_border, (50, 85))

# Añadir pequeño texto decorativo
draw.text((350, 315), "ELECTRONICA APLICADA", fill=color_acento, font=fuente_normal)

# Guardar la imagen
img.save("tarjeta_contacto_mejorada.png")
img.show()