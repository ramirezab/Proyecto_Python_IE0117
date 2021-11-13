
import pygame

from sprites import *
from config import *
from Mapas_pruebas import *
from PIL import Image
pygame.init()
display_info = pygame.display.Info()

class level:
    def __init__(self, nivel, surface, wall_type):
        self.diplay_surface = surface
        self.set_walls(nivel, wall_type)
        self.set_player()

        self.world_x_shift = 0
        self.world_y_shift = 0
        

    def set_walls(self, layout, wall_type):
        im = Image.open(wall_type)
        
        

        self.walls = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):

                if cell == "b":
                    x = row_index*im.size[0]-((display_info.current_h-150)//2)
                    y = col_index*im.size[1]-((display_info.current_h-150)//2)
                    tile = wall((x,y), wall_type)
                    self.walls.add(tile)
        

    def set_player(self):


        self.player = ply(((display_info.current_h-150)//2, (display_info.current_h)//2-150))
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player)
        self.player.speed=0

    def scroll_world(self):

        keys = pygame.key.get_pressed()
        
        # Controles del jugador van aqui
        if keys[pygame.K_a]:
            
            if pygame.sprite.spritecollide(self.player, self.walls, False):
                self.world_x_shift =-1
                    
            else:
                self.world_x_shift=1
                if keys[pygame.K_LSHIFT]:
                    self.world_x_shift +=3
                    
                
        elif keys[pygame.K_d]:
            
            if pygame.sprite.spritecollide(self.player, self.walls, False):
                    self.world_x_shift += 1
                    
            else:
                self.world_x_shift=-1
                if keys[pygame.K_LSHIFT]:
                    self.world_x_shift +=-3


        elif keys[pygame.K_w]:
            if pygame.sprite.spritecollide(self.player, self.walls, False):
                    self.world_y_shift+=-1
                    
            else:
                self.world_y_shift=1
                if keys[pygame.K_LSHIFT]:
                    self.world_y_shift +=3


        elif keys[pygame.K_s]:
            if pygame.sprite.spritecollide(self.player, self.walls, False):
                    self.world_y_shift+= 1
                    
            else:
                self.world_y_shift=-1
                if keys[pygame.K_LSHIFT]:
                    self.world_y_shift +=-3

        
        
        

        else:
            self.world_x_shift=0
            self.world_y_shift=0
        
        
        
        

        




    def run(self):
        
        self.walls.update(self.world_x_shift, self.world_y_shift)
        self.walls.draw(self.diplay_surface)
        self.player_list.draw(self.diplay_surface)
        self.scroll_world()




