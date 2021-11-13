import pygame
import sys
from pygame.constants import FULLSCREEN
from config import *
from niveles import level

pygame.init()


display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((0,0), FULLSCREEN) # Tamaño de la pantalla

clock = pygame.time.Clock()

level_1 = level(level_map_1, screen, "sprites\wall_1_front.png")
level_2 = level(level_map_2, screen, "sprites\wall_2_front.png")
level_3 = level(level_map_3, screen, "sprites\wall_3_front.png")

while True:
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                

            
        if event.type == pygame.QUIT:
            sys.exit()
            
                
    
    screen.fill('black')
    level_2.run()
   
    pygame.display.flip()
    
