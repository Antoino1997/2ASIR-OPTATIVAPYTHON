from PIL import Image

CHARS = "@%#*+=-:. "

def imagen_a_ascii(ruta, ancho=100):
    img = Image.open(ruta)
    img = img.convert("L")

    ratio = img.height / img.width
    alto = int(ancho * ratio * 0.55)
    img = img.resize((ancho, alto))

    resultado = ""
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            char = CHARS[pixel * len(CHARS) // 256]
            resultado += char
        resultado += "\n"

    return resultado

print(imagen_a_ascii("foto.jpg"))