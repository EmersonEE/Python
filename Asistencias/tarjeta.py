from PIL import Image, ImageDraw, ImageFont

# Abre la imagen principal
imagen = Image.open("1.png").convert("RGBA")
dibujo = ImageDraw.Draw(imagen)

# Usa una fuente en negrita
fuente_path = "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"
fuente = ImageFont.truetype(fuente_path, 38)

# Función para dibujar texto con sombra
def texto_con_sombra(draw, posicion, texto, fuente, color_texto="white", color_sombra="black", desplazamiento=(2, 2)):
    x, y = posicion
    dx, dy = desplazamiento
    draw.text((x + dx, y + dy), texto, font=fuente, fill=color_sombra)
    draw.text((x, y), texto, font=fuente, fill=color_texto)

# Dibuja textos con sombra
texto_con_sombra(dibujo, (50, 100), "Emerson Perez", fuente)
texto_con_sombra(dibujo, (125, 275), "Electronica", fuente)
texto_con_sombra(dibujo, (125, 360), "49964191", fuente)
texto_con_sombra(dibujo, (125, 450), "202512345", fuente)

# 🖼️ Cargar imagen a superponer (ejemplo: logo)
logo = Image.open("qr.png").convert("RGBA")
logo = logo.resize((325, 325))  # Ajusta tamaño si es necesario

# Posición donde se va a pegar el logo (esquina superior derecha)
posicion_logo = (725, 50)

# Pega el logo con transparencia
imagen.paste(logo, posicion_logo, logo)

# Guarda la imagen final
imagen.save("imagen_con_texto_y_logo.png")
print("✅ Imagen con texto y logo guardada.")
