#!usr/bin/python3

import pygame
from pygame import mixer
pygame.init()
tamano = (800,600)
negro = (0,0,0)
pantalla = pygame.display.set_mode(tamano)

pygame.display.set_caption("Prueba de musica")
icon = pygame.image.load("Icono.png") # El icono es un placeholder
pygame.display.set_icon(icon)

# Personaje
Mono = pygame.image.load("mono.png")  # El mono es un placeholder
MonoX = 370
MonoY = 480

# Velocidad del Mono
movimientoX = 0
movimientoY = 0

def jugador():
    pantalla.blit(Mono, (MonoX, MonoY))
#Sonido de los pasos en la playa (Pueden recomendar otra cancion)
pasos = pygame.mixer.Sound("Pasos en arena.mp3")
# El sonido esta un poco alto

#sonido del nivel de la playa
mixer.music.load("Musica playa.mp3")
mixer.music.play(-1) # En -1 la cancion se repite infinitamente

Juego = True

while (Juego):
    pantalla.fill(negro)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            Juego = False
        if (event.type == pygame.KEYDOWN):
            # Movimiento del personaje
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                movimientoX = -0.1
                pasos.play(-1)
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                movimientoX = 0.1
                pasos.play(-1)
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                movimientoY = 0.1
                pasos.play(-1)
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                movimientoY = -0.1
                pasos.play(-1)
            # El juego pausa la musica con m y la reanuda con n
            elif (event.key == pygame.K_m):
                pygame.mixer.music.pause()
            elif (event.key == pygame.K_n):
                pygame.mixer.music.unpause()
        if (event.type == pygame.KEYUP):
            if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                movimientoX = 0
                pasos.stop()
            elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                movimientoX = 0
                pasos.stop()
            elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                movimientoY = 0
                pasos.stop()
            elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                movimientoY = 0
                pasos.stop()
    MonoX += movimientoX
    MonoY += movimientoY
    jugador()
    pygame.display.update()
