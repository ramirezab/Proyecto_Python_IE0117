import pygame
import sys
    

from config import *

from niveles import level

pygame.init()


display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_width-150, screen_height-150)) # Tamaño de la pantalla

clock = pygame.time.Clock()

level_1 = level(level_map_1, screen, "sprites\wall_2_front.png")
level_2 = level(level_map_2, screen, "sprites\wall_2_front.png")

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
    clock.tick(1200)
