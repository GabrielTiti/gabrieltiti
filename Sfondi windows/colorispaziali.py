from PIL import Image, ImageDraw, ImageFont
from ctypes import windll, c_int, byref
from ctypes.wintypes import RGB
import os
import math

def immagine_spettacolare():
    width, height = 1980, 1050
    image = Image.new("RGB", (width, height), color="black")
    draw = ImageDraw.Draw(image)
    draw.point([100, 100], RGB(255, 255, 255))
    for x in range(0, width):
        for y in range(0, height):
            r = 100 + 30.0 * math.tan(x/200*y/700) * math.tan(x/300+y/2000) * math.cos((x-y)/1000)
            g = 100 + 30.0 * math.tan(x/300*y/300) * math.tan(x/300+y/1000) * math.cos((x-y)/2000)
            b = 100 + 30.0 * math.tan(x/100*y/400) * math.tan(x/300+y/500) * math.cos((x-y)/3000)
            draw.point([x, y], RGB(int(r), int(g), int(b)))

    #image_path = os.path.join(r"C:\Users\andic\Documents", "TEST.bmp")
    #image.save(image_path)
    image.show()

if __name__ == "__main__":
    immagine_spettacolare()
