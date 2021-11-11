
import pygame
from pygame import event

pygame.init()

reloj = pygame.time.Clock()
dimnesions = (800, 500)

pantalla = pygame.display.set_mode(dimnesions)
pygame.display.set_caption("Juego de prueba")
BLANCO = (255, 255, 255)
pantalla.fill(BLANCO)


salir = False

while not salir:
    reloj.tick(60)
    
    
    
    
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            salir = True
        
        if evento.type == pygame.KEYDOWN:
            player=pygame.draw.circle(pantalla, (0,0,0), (50,50), (9))
            pygame.display.flip()
            

        if evento.type == pygame.MOUSEBUTTONDOWN:
            line=pygame.draw.line(pantalla, (0, 255, 0), [0, 0], [100, 100], 80)
            pygame.display.flip()
    
            

        

pygame.quit