from PIL import Image
import pygame

pygame.init()


def mapeo(image):

    """
    Crea una lista donde cada entrada es una cadena de caracteres
    que representa los pixeles negros de la imagen con la letra b
    """

    im = Image.open(image).convert()  # Carga la imagen

    # Cambia el tamaño de la imagen para que se ajuste a la
    # pantalla del juego
    im2 = im.resize((800, 600))

    # Crea una lista con todos los pixeles en RGB de a imagen
    pix = im2.load()

    # Lista que guarda la posicion de los ixeles relevantes de la imagen
    mapa = []

    x = 20  # Variacion aceptable de pixeles negres

    # Revision de filas de pixeles de la imagen
    for row in range(0, im2.size[0], 5):
        a = []

        # Revision de columnas de pixeles de la imagen
        for column in range(0, im2.size[1], 5):

            # Comprobación de rango aceptable de tonos de negro
            if (pix[row, column][0] in range(x)
               and pix[row, column][1] in range(x)
               and pix[row, column][2] in range(x)):
                a.append("b")

            elif (pix[row, column][0] in range(x)
                  and pix[row, column][1] in range(255-x, 255, 1)
                  and pix[row, column][2] in range(x)):
                a.append("g")

            elif (pix[row, column][0] in range(255-x, 255, 1)
                  and pix[row, column][1] in range(x)
                  and pix[row, column][2] in range(x)):
                a.append("r")

            elif (pix[row, column][0] in range(x)
                  and pix[row, column][1] in range(x)
                  and pix[row, column][2] in range(0, 255, 1)):
                a.append("a")

            elif (pix[row, column][0] == 255
                  and pix[row, column][1] == 255
                  and pix[row, column][2] == 0):
                a.append("y")
            else:
                a.append(" ")

        # Definicion de str que contiene 1 fila de pixeles de la imagen
        b = "".join(a)  
        mapa.append(b)

    return mapa
