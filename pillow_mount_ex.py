pip install pillow

from PIL import Image

## base --
# Cargar imagen base (foto del depa)
base_img = Image.open("foto_departamento.jpg").convert("RGBA")

# Cargar el ícono PNG con fondo transparente (por ejemplo, el xolo o Zapata)
overlay_img = Image.open("icono.png").convert("RGBA")

# Redimensionar ícono si es necesario
overlay_resized = overlay_img.resize((150, 150))  # Tamaño en px

# Establecer coordenadas donde aparecerá el ícono (x, y)
position = (50, 50)

# Superponer ícono sobre la imagen base
base_img.paste(overlay_resized, position, overlay_resized)

# Guardar resultado
base_img.save("foto_con_icono.png")

## ejemplo --
# Cargar imágenes
base = Image.open("sala.jpg").convert("RGBA")
zapata = Image.open("zapata.png").convert("RGBA")

# Escalar y aplicar opacidad
zapata = zapata.resize((180, 180))
zapata.putalpha(180)  # 255 es opaco, 0 es invisible

# Colocar en esquina inferior derecha
x = base.width - zapata.width - 30
y = base.height - zapata.height - 30

base.paste(zapata, (x, y), zapata)
base.save("sala_con_zapata.png")
