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
    
    im2 = im.resize((screen_size.current_h-150,screen_size.current_h-150))
    
    pix = im2.load()
    mapa=[]
    x = 5
    for row in range(0,im2.size[0],5):
        a=[]
        for column in range(0,im2.size[1],5):
            
            if pix[row, column][0] in range(x) and pix[row, column][1] in range(x) and pix[row, column][2] in range(x):
                
                a.append("b")
            else:
                a.append(" ")
            
        
            
        b = "".join(a)
        mapa.append(b) 
    
    return mapa
