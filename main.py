import pygame
import sys
    
from pygame import sprite
from pygame import display
from config import *
from sprites import wall
from niveles import level

pygame.init()


display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_height, screen_height)) # Tamaño de la pantalla

clock = pygame.time.Clock()

level_1 = level(level_map_1, screen)

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                
    
    screen.fill('grey')
    level_1.run()

    pygame.display.flip()
print(type(scree_height))