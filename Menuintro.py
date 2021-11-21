import pygame
import time
from pygame.locals import *

#Constantes para el codigo
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Labyrinth quest')

background_menu = pygame.image.load('Fondos/prueba.JPG').convert()

#Colores
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
plomo = (232,224,224)
yellow = (255,255,0)

#Inicializacion
pygame.init()

#Fuentes para la letra de menu
small_font = pygame.font.SysFont('comicsansms',15)
medium_font = pygame.font.SysFont('comicsansms',30)
large_font = pygame.font.SysFont('comicsansms',50)

#Datos para los botones en menu
size_button = [200,45]

button_levels = [300,200]
color_levels = [plomo,yellow]

button_options = [300,270]
color_options = [plomo,red]

button_controls = [300,340]
color_controls = [plomo,green]

#Datos para botones de niveles
size_but_lvl = [100,45]
color_but_lvl = [plomo,green]

#posciones de los botones
button_lvl1 = [75,235]
button_lvl2 = [212,235]
button_lvl3 = [349,235]
button_lvl4 = [486,235]
button_lvl5 = [625,235]
button_lvl6 = [75,325]
button_lvl7 = [212,325]
button_lvl8 = [349,325]
button_lvl9 = [486,325]
button_lvl10 = [625,325]

#Texto dentro del boton
def msg_button(msg,color,button_X,button_Y,width,height,size='small'):
    text_select, textRect = obj_text(msg,color,size)
    textRect.center = (button_X+(width/2),button_Y+(height/2))
    screen.blit(text_select,textRect)

#Para la creacion de los botones
def buttons(text,surface,state,posit,size_butt,id_button = None):
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

#Define si el cursor esta en el boton o no
    if posit[0] + size_butt[0] > cursor[0] > size_butt[0] and posit[0] + size_butt[0] < cursor[0] + size_butt[0] and posit[1] + size_butt[1] > cursor[1] > size_butt[1] and posit[1] + size_butt[1] < cursor[1] + size_butt[1]:

        if click[0] == 1:
            if id_button == 'niveles':
                menulevels()
            elif id_button == 'configuracion':
                options()
            elif id_button == 'detalles':
                controls()

        button = pygame.draw.rect(surface,state[1],(posit[0],posit[1],size_butt[0],size_butt[1]))
    else:
        button = pygame.draw.rect(surface,state[0],(posit[0],posit[1],size_butt[0],size_butt[1]))

    msg_button(text,black,posit[0],posit[1],size_butt[0],size_butt[1])
    return button

#Funcion para el tamaño de letra
def obj_text(text,color,size):
    if size == 'small':
        text_select = small_font.render(text,True,color)
    if size == 'medium':
        text_select = medium_font.render(text,True,color)
    if size == 'large':
        text_select = large_font.render(text,True,color)
    return text_select, text_select.get_rect()

#Funcion de caracteristicas del texto
def message(msg,color,despla_Y=0,size='small'):
    text_select, textRect = obj_text(msg,color,size)
    textRect.center = (screen_width/2), (screen_height/2)+despla_Y
    screen.blit(text_select,textRect)

#Menu principal, primera cara del juego
def intromenu():
    introgame = True

    while introgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background_menu,[0,0])

#Botones y sus textos en la pagina menu
        buttons('NIVELES',screen,color_levels,button_levels,size_button,id_button='niveles')
        buttons('OPCIONES',screen,color_options,button_options,size_button,id_button='configuracion')
        buttons('CONTROLES',screen,color_controls,button_controls,size_button,id_button='detalles')

#Mensajes libres en la pantalla
        message('LABYRINTH QUEST',black,-250,size='large')
        message('LABYRINTH QUEST',red,-246,size='large')
        message('Presionar X para ir hacia atras',white,200,size='medium')
        pygame.display.update()
        clock.tick(15)

#Para principalmente el volumen, si se puede ajuste de tamaño de pantalla
def options():
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                regres = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    intromenu()
                    regres = False

            screen.fill(white)
            message('Aqui iran las opciones',red,-100,size='medium')
            pygame.display.update()
            clock.tick(15)

#Dará los controles del juego
def controls():
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    intromenu()
                    regres = False

            screen.fill(white)
            message('Aqui iran los controles',red,-100,size='medium')
            pygame.display.update()
            clock.tick(15)

#Estaran todos los niveles para escoger
def menulevels():
    regres = True

    while regres:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    intromenu()
                    regres = False

            pygame.display.update()
            clock.tick(15)
        screen.blit(background_menu,[0,0])

        buttons('Nivel I',screen,color_but_lvl,button_lvl1,size_but_lvl,id_button='lvl1')
        buttons('Nivel II',screen,color_but_lvl,button_lvl2,size_but_lvl,id_button='lvl2')
        buttons('Nivel III',screen,color_but_lvl,button_lvl3,size_but_lvl,id_button='lvl3')
        buttons('Nivel IV',screen,color_but_lvl,button_lvl4,size_but_lvl,id_button='lvl4')
        buttons('Nivel V',screen,color_but_lvl,button_lvl5,size_but_lvl,id_button='lvl5')
        buttons('Nivel VI',screen,color_but_lvl,button_lvl6,size_but_lvl,id_button='lvl6')
        buttons('Nivel VII',screen,color_but_lvl,button_lvl7,size_but_lvl,id_button='lvl7')
        buttons('Nivel VIII',screen,color_but_lvl,button_lvl8,size_but_lvl,id_button='lvl8')
        buttons('Nivel IX',screen,color_but_lvl,button_lvl9,size_but_lvl,id_button='lvl9')
        buttons('Nivel X',screen,color_but_lvl,button_lvl10,size_but_lvl,id_button='lvl10')


# TODO botones de todos los niveles

#Ejecucion de los diferentes niveles
def gameloop():
    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit = True
            screen.fill(white)
            message('Ejecucion de los diferentes niveles',red,-100,size='medium')
            pygame.display.update()
            clock.tick(15)

intromenu()
quit()
gameloop()
