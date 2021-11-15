from PIL import Image
import pygame

pygame.init()

def mapeo(image):

    screen_size= pygame.display.Info()
    """
    Crea una lista donde cada entrada es una cadena de caracteres
    que representa los pixeles negros de la imagen con la letra b
    """

    im = Image.open(image) # Carga la imagen
    
    # Cambia el tamaño de la imagen para que se ajuste a la
    # pantalla del juego
    im2 = im.resize((screen_size.current_h-150,screen_size.current_h-150)) 
    
    # Crea una lista con todos los pixeles en RGB de a imagen
    pix = im2.load()
    mapa=[] # Lista que guarda la posicion de los ixeles relevantes de la imagen

    x = 20 # Variacion aceptable de pixeles negres
    for row in range(0,im2.size[0],5): # Revision de filas de pixeles de la imagen
        a=[]
        for column in range(0,im2.size[1],5): # Revision de columnas de pixeles de la imagen
            
            # Comprobación de rango aceptable de tonos de negro
            if pix[row, column][0] in range(x) and pix[row, column][1] in range(x) and pix[row, column][2] in range(x):
                
                a.append("b")

            elif pix[row, column][0] in range(x) and pix[row, column][1] in range(255-x,255,1) and pix[row, column][2] in range(x):
                a.append("g")

            elif pix[row, column][0] in range(255-x,255,1) and pix[row, column][1] in range(x) and pix[row, column][2] in range(x):
                a.append("r")

            elif pix[row, column][0] in range(x) and pix[row, column][1] in range(x) and pix[row, column][2] in range(255-x,255,1):
                a.append("a")
            else:
                a.append(" ")
            
    
            
        b = "".join(a) # Definicion de str ue contiene 1 fila de pixeles de la imagen
        mapa.append(b) 
    
    return mapa
