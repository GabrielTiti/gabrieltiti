import time
import ctypes
from ctypes import windll, c_int, byref
from ctypes.wintypes import RGB

def cicla_colore_sfondo():    
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "", 3)
    COLOR_BACKGROUND = 1 # from winuser.h or win32con
    SetSysColors = ctypes.windll.user32.SetSysColors
    which_color = RGB(255,255,255)
    while which_color > 0:
        SetSysColors(1, byref(c_int(COLOR_BACKGROUND)), byref(c_int(which_color)))
        time.sleep(1)
        which_color-=RGB(16,16,16)

if __name__ == "__main__":
    cicla_colore_sfondo()
