import pygame
import sys
from pygame.constants import FULLSCREEN
from config import *
from niveles import level

pygame.init()

# Detecta la informacion de la pantalla
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

#Defina el tamaño de la pantalla del juego
screen = pygame.display.set_mode((800,600)) # Tamaño de la pantalla

clock = pygame.time.Clock()

#Creación de niveles
level_1 = level(level_map_1, screen, "sprites\wall_1_front.png")
level_2 = level(level_map_2, screen, "sprites\wall_2_front.png")
level_3 = level(level_map_3, screen, "sprites\wall_3_front.png")

#Bucle principal del juego
while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                

            
        if event.type == pygame.QUIT:
            sys.exit()
            
                
    
    screen.fill('grey')
    level_2.run()
   
    pygame.display.flip()
    
