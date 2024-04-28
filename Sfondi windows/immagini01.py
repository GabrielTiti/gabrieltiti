import os
import time
from PIL import Image, ImageDraw, ImageFont
import ctypes
from datetime import datetime

def generate_image(image_folder, interval_minutes):
    while True:
        # Crea un'immagine vuota
        width, height = 1980, 1050
        image = Image.new("RGB", (width, height), color="black")
        draw = ImageDraw.Draw(image)
        # Aggiungi testo all'immagine
        font = ImageFont.truetype("arial.ttf", size=36)
        text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        text_width, text_height = 100, 100
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        draw.text((x, y), text, fill="white", font=font)

        # Salva l'immagine
        image_path = os.path.join(image_folder, "custom_background.bmp")
        image.save(image_path)

        # Imposta lo sfondo
        #os.system(f"reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d \"{image_path}\" /f")
        #os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")

        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

        # print(f"Sfondo cambiato con l'immagine generata: {image_path}")

        time.sleep(interval_minutes)

if __name__ == "__main__":
    image_folder = r"C:\Users\andic\Documents"
    interval_minutes = 1  # Cambia ogni minuto
    generate_image(image_folder, interval_minutes)
