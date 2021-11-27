import pygame
import sys
from pygame.constants import FULLSCREEN
from config import *
from niveles import level
from pygame import mixer




pygame.init()
pygame.mixer.init()
pygame.font.init()
# Detecta la informacion de la pantalla
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Defina el tamaño de la pantalla del juego
screen = pygame.display.set_mode((800,600)) # Tamaño de la pantalla

clock = pygame.time.Clock()

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






pasos = "Sonidos\Pasos en arena.mp3"
Pasos = pygame.mixer.Sound(pasos)

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
                Pasos.play(-1)
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                Pasos.play(-1)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                Pasos.play(-1)
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                Pasos.play(-1)
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
                Pasos.stop()
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                Pasos.stop()
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                Pasos.stop()
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                Pasos.stop()
        # Fin modulo de sonido 2

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('grey')

    level_10.run()
    fps.render(screen, level_1.puntaje())

    fps.clock.tick(60)
    pygame.display.flip()
