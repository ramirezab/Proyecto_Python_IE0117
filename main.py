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
level_1 = level(level_map_1, screen, "sprites\wall_1_front.png")
level_2 = level(level_map_2, screen, "sprites\wall_2_front.png")
level_3 = level(level_map_3, screen, "sprites\wall_3_front.png")

# Con esto se puede identificar la musica y pasos de cada nivel
nivel = level_2

if (nivel == level_2):
    cancion = "Sonidos\Musica playa.mp3"
elif (nivel == level_1):
    cancion = "Sonidos\Musica mazmorra.mp3"

if (nivel == level_2):
    pasos = "Sonidos\Pasos en arena.mp3"
elif (nivel == level_1):
    pasos = "Sonidos\Pasos metal.mp3"


# music = pygame.mixer.music.load(cancion)
# pygame.mixer.music.play(-1)

Pasos = pygame.mixer.Sound(pasos)

# Muestra FPS
class FPS:
    def __init__ (self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.text = self.font.render(str(level_2.puntaje()), True, (0,0,0))
        screen.blit(self.text, (10,10))
    def render(self, screen):
        self.text = self.font.render(str(level_2.puntaje()), True, (0,0,0))
        screen.blit(self.text, (10,10))
fps = FPS()

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        # Inicio del modulo de sonido 1
        if event.type == pygame.KEYDOWN:
            Pasos.play(-1)
            # if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
            #     Pasos.play(-1)
            # elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
            #     Pasos.play(-1)
            # elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
            #     Pasos.play(-1)
            # elif (event.key == pygame.K_UP or event.key == pygame.K_w):
            #     Pasos.play(-1)
                # Con este modulo si se apreta m se pausa la musica
                # Con n se reanuda donde se dejo pausada
            # elif (event.key == pygame.K_m):
            #     pygame.mixer.music.pause()
            # elif (event.key == pygame.K_n):
            #     pygame.mixer.music.unpause()
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
    fps.render(screen)
    level_2.run()
    fps.clock.tick(60)
    pygame.display.flip()
