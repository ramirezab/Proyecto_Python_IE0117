from PIL import Image
import pygame

pygame.init()

def mapeo(image):

    screen_size= pygame.display.Info()
    """
    Crea una lista donde cada entrada es una cadena de caracteres
    que representa los pixeles negros de la imagen con la letra b
    """

    im = Image.open(image)
    im2 = im.resize((screen_size.current_h,screen_size.current_h))

    pix = im2.load()
    mapa=[]

    for row in range(im2.size[0]):
        a=[]
        for column in range(im2.size[1]):
            
            if pix[row, column] == (0,0,0):
                
                a.append("b")
            else:
                a.append(" ")
            
        
            
        b = "".join(a)
        mapa.append(b) 
    
    return mapa
