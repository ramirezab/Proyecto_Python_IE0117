import pygame
import sys
import time
from pygame.constants import FULLSCREEN
from config import *
from niveles import level
from pygame import mixer
from pygame.locals import *

#Constantes para el codigo
clock = pygame.time.Clock()
pygame.display.set_caption('Labyrinth quest')

#tamaño de la pantalla
screen = pygame.display.set_mode((800, 600))

background_menu = pygame.image.load('Fondos\prueba.jpg').convert()

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
pygame.mixer.init()
pygame.font.init()

# Detecta la informacion de la pantalla
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Creación de niveles
level_1 = level(level_map_1, screen, "sprites\Sprite lvl 1.png")
level_2 = level(level_map_2, screen, "sprites\Sprite lvl 2.png")
level_3 = level(level_map_3, screen, "sprites\Sprite lvl 3.png")
level_4 = level(level_map_4, screen ,"sprites\Sprite lvl 4.png")
level_5 = level(level_map_5, screen ,"sprites\Sprite lvl 5.png")
level_6 = level(level_map_6, screen ,"sprites\Sprite lvl 6.png")
level_7 = level(level_map_7, screen ,"sprites\Sprite lvl 7.png")
level_8 = level(level_map_8, screen ,"sprites\Sprite lvl 8.png")
level_9 = level(level_map_9, screen ,"sprites\Sprite lvl 9.png")
level_10 = level(level_map_10, screen ,"sprites\Sprite lvl 10.png")

# Con esto se puede identificar la musica, los pasos de cada nivel
# Y elegir el nivel mismo
nivel = level_2

if (nivel == level_1):
    cancion = "Sonidos\Musica playa.mp3"
elif(nivel == level_2):
    cancion = "Sonidos\Musica bosque.mp3"
elif(nivel == level_3):
    cancion = "Sonidos\Musica selva.mp3"
elif(nivel == level_4):
    cancion = "Sonidos\Musica nieve.mp3"
elif (nivel == level_5):
    cancion = "Sonidos\Musica mazmorra.mp3"
elif (nivel == level_6):
    cancion = "Sonidos\Musica dungeon.mp3"
elif (nivel == level_7):
    cancion = "Sonidos\Musica luna.mp3"
elif (nivel == level_8):
    cancion = "Sonidos\Musica inferno.mp3"
elif (nivel == level_9):
    cancion = "Sonidos\Musica marte.mp3"
elif (nivel == level_10):
    cancion = "Sonidos\Musica cielo.mp3"

#pasos
if (nivel == level_2):
    pasos = "Sonidos\pasos en arena.mp3"
elif (nivel == level_1):
    pasos = "Sonidos\pasos metal.mp3"

#Fuentes para la letra de menu
small_font = pygame.font.SysFont('comicsansms',15)
medium_font = pygame.font.SysFont('comicsansms',30)
large_font = pygame.font.SysFont('comicsansms',50)

#Datos para los botones en menu principal
size_button = [200,45]

button_levels = [300,200]
color_levels = [plomo,yellow]

button_score = [300,270]
color_score = [plomo,yellow]

button_options = [300,340]
color_options = [plomo,red]

button_controls = [300,410]
color_controls = [plomo,green]

button_exit = [300,480]
color_exit = [plomo,yellow]

button_regress = [625,500]
color_regress = [plomo,yellow]

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
            elif id_button == 'puntajes':
                score()
            elif id_button == 'configuracion':
                options()
            elif id_button == 'detalles':
                controls()
            elif id_button == 'regresar':
                intromenu()
            elif id_button == 'salir':
                pygame.quit()
                quit()

            #Para los niveles
            elif id_button == 'lvl1':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_1.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False

            elif id_button == 'lvl2':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_2.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl3':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_3.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl4':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_4.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl5':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_5.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl6':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_6.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl7':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_7.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl8':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_8.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl9':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_9.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False
            elif id_button == 'lvl10':
                game_state = True
                while game_state:
                    screen.fill('grey')
                    level_10.run()
                    fps.render(screen, level_1.puntaje())
                    fps.clock.tick(60)
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if (event.key == pygame.K_ESCAPE):
                                game_state = False

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

        # Botones y sus textos en la pagina menu
        buttons('NIVELES',screen,color_levels,button_levels,size_button,id_button='niveles')
        buttons('MEJORES PUNTAJES',screen,color_score,button_score,size_button,id_button='puntajes')
        buttons('OPCIONES',screen,color_options,button_options,size_button,id_button='configuracion')
        buttons('CONTROLES',screen,color_controls,button_controls,size_button,id_button='detalles')
        buttons('SALIR',screen,color_exit,button_exit,size_button,id_button='salir')

        #Mensajes libres en la pantalla
        message('LABYRINTH QUEST',black,-250,size='large')
        message('LABYRINTH QUEST',red,-246,size='large')

        pygame.display.update()
        clock.tick(60)

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

            buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')
            message('Aqui iran las opciones',red,-100,size='medium')
            pygame.display.update()
            clock.tick(60)

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

            buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')
            message('Aqui iran los controles',red,-100,size='medium')
            pygame.display.update()
            clock.tick(60)

def score():
    scores = True

    while scores:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    intromenu()
                    regres = False

            screen.fill(white)

            buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')
            message('Aqui iran los mejores puntajes',red,-100,size='medium')
            pygame.display.update()
            clock.tick(60)

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
            clock.tick(60)
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

        buttons('ATRAS',screen,color_regress,button_regress,size_but_lvl,id_button='regresar')

# Muestra FPS
class FPS:
    def __init__ (self, puntaje):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.text = self.font.render(str(puntaje), True, (0,0,0))
        screen.blit(self.text, (10,10))
    def render(self, screen, puntaje):
        self.text = self.font.render(str(puntaje), True, (0,0,0))
        screen.blit(self.text, (10,10))
fps = FPS(level_1.puntaje())

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        # Inicio del modulo de sonido 1
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                pasos.play(-1)
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                pasos.play(-1)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                pasos.play(-1)
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                pasos.play(-1)
                # Con este modulo si se apreta m se pausa la musica
                # Con n se reanuda donde se dejo pausada
            elif (event.key == pygame.K_m):
                pygame.mixer.music.pause()
            elif (event.key == pygame.K_n):
                pygame.mixer.music.unpause()
        # Fin del modulo de sonido

        # Con este comando si apretas ESC el juego se cerrará
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Inicio modulo de sonido 2
        if (event.type == pygame.KEYUP):
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                pasos.stop()
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                pasos.stop()
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                pasos.stop()
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                pasos.stop()
        # Fin modulo de sonido 2

        if event.type == pygame.QUIT:
            sys.exit()


    intromenu()
    menulevels()
    #level_10.run()

    fps.render(screen, level_10.puntaje())
    fps.clock.tick(60)
    pygame.display.flip()
