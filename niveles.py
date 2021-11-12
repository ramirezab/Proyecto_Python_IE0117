
import pygame
from sprites import *
from config import *
from Mapas_pruebas import *


class level:
    def __init__(self, nivel, surface):

    

        self.diplay_surface = surface
        self.set_walls(nivel)
        self.set_player()

        self.world_x_shift = 0
        self.world_y_shift = 0
        self.player = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()


    def set_walls(self, layout):
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "b":
                    x = row_index*10
                    y = col_index*10
                    tile = wall((x,y))
                    self.walls.add(tile)
                

    def set_player(self):
        
        player = ply()

        self.player.add(player)



    def run(self):
        self.player.update()
        self.walls.update(self.world_x_shift, self.world_y_shift)
        self.walls.draw(self.diplay_surface)
        self.player.draw(self.diplay_surface)
        
        