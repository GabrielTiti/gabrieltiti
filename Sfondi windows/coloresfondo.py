import time
import ctypes
from ctypes import windll, c_int, byref
from ctypes.wintypes import RGB
NUMERO_COLORI = 255
def imposta_colore_sfondo(r, g, b):
    r=int(r)
    g=int(g)
    b=int(b)
    colore=RGB(r, g, b)
    COLOR_BACKGROUND = 1 # from winuser.h or win32con
    print(r,g,b)
    SetSysColors = ctypes.windll.user32.SetSysColors
    SetSysColors(1, byref(c_int(COLOR_BACKGROUND)), byref(c_int(colore)))
    time.sleep(1)

def cicla_colore_sfondo():    
    #tolgo immagine sfondo
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "", 3)
    
    #valori iniziali rosso, verde, blu
    r = 0
    g = 0
    b = 0
    #direzione dei delta
    direzioner = 1
    direzioneg = 1
    direzioneb = 1
    
    numeroSaltir = 4
    numeroSaltig = 4
    numeroSaltib = 4

    #parto con questo colore 
    imposta_colore_sfondo(r,g,b)
    
    
    bloop = True
    while bloop:

        if (r==NUMERO_COLORI and direzioner==1) or (r==0 and direzioner==-1) :
            direzioner=-direzioner
            if (g==NUMERO_COLORI and direzioneg==1) or (g==0 and direzioneg==-1) :
                direzioneg=-direzioneg
                if (b==NUMERO_COLORI and direzioneb==1) or (b==0 and direzioneb==-1) :
                    direzioneb=-direzioneb
                    r+=direzioner*(NUMERO_COLORI/numeroSaltir)
                else:
                    b+=direzioneb*(NUMERO_COLORI/numeroSaltib)
            else:
                g+=direzioneg*(NUMERO_COLORI/numeroSaltig)
        else:
            r+=direzioner*(NUMERO_COLORI/numeroSaltir)
        
        imposta_colore_sfondo(r, g, b)
        bloop = r+g+b>0

if __name__ == "__main__":
    cicla_colore_sfondo()
