
import pygame
from sprites import *
from config import *
from Mapas_pruebas import *

class level:
    def __init__(self, nivel, surface):

        self.diplay_surface = surface
        self.set_walls(nivel)

    def set_walls(self, layout):
        self.walls = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell == "b":
                    x = row_index*5
                    y = col_index*5
                    tile = wall((x,y), tile_size)
                    self.walls.add(tile)



    def run(self):
        self.walls.draw(self.diplay_surface)
        