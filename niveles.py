
import pygame
from pygame import sprite

from sprites import *
from config import *
from Mapas_pruebas import *
from PIL import Image
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
display_info = pygame.display.Info()

#Clase nivel
class level:
    def __init__(self, nivel, surface, wall_type):
        self.diplay_surface = surface
        self.set_walls(nivel, wall_type)    # Se llaman surface y wall_type como los argumentos de entrada de set_walls
        self.set_player()
        self.moneda = pygame.mixer.Sound("Sonidos\Moneda.mp3")

        self.score = 0
        self.world_x_shift = 0
        self.world_y_shift = 0

    # Se Itera una lista y se colocan sprites en el mapa según la posicion
    # de los caracteres encontrados
    def set_walls(self, layout, wall_type):
        self.im = Image.open(wall_type)

        self.walls = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.door_keys = pygame.sprite.Group()
        self.lock_doors = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):

                if cell == "b": # Deteccion de pixeles negros
                    x = row_index*self.im.size[0]-(400)
                    y = col_index*self.im.size[1]-(300)
                    tile = wall((x,y), wall_type)
                    self.walls.add(tile)

                elif cell == "g": # Deteccion de pixeles negros
                    j = row_index*self.im.size[0]-(400)
                    k = col_index*self.im.size[1]-(300)
                    item = items((j, k))

                    self.items.add(item)

                elif cell == "r": # Deteccion de pixeles rojos
                    if len(self.door_keys) < 1:
                        j = row_index*self.im.size[0]-(400)
                        k = col_index*self.im.size[1]-(300)
                        key = door_key((j, k))
                        self.door_keys.add(key)
                    else:
                        pass

                elif cell == "a": # Deteccion de pixeles negros
                    j = (row_index)*self.im.size[0]-(400)
                    k = (col_index)*self.im.size[1]-(300)
                    door = lock_door((j, k))
                    self.lock_doors.add(door)



    # Posicion del jugador e la pantalla
    def set_player(self):


        self.player = ply((400, 300))
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.player)


    # Movimiento del mundo
    def scroll_world(self):
        if self.world_y_shift > 3 or self.world_x_shift > 3:
            self.world_x_shift=0
            self.world_y_shift=0
        elif self.world_y_shift < 3 or self.world_x_shift < 3:
            self.world_x_shift=0
            self.world_y_shift=0

        self.keys = pygame.key.get_pressed()



        # Controles del jugador van aqui
        if self.keys[pygame.K_a] :
            if self.player.rect.x < 400:
                self.player.speed =0
                self.world_x_shift=1
                if self.keys[pygame.K_LSHIFT]:
                    self.world_x_shift += 3
            else:
                self.player.rect.x -= 1
                if self.keys[pygame.K_LSHIFT]:
                    self.player.rect.x -= 3
            return
        elif self.keys[pygame.K_d] :
            if self.player.rect.x > 400:
                self.player.speed =0
                self.world_x_shift=-1
                if self.keys[pygame.K_LSHIFT]:
                    self.world_x_shift -= 3
            else:
                self.player.rect.x += 1
                if self.keys[pygame.K_LSHIFT]:
                    self.player.rect.x += 3

            return
        elif self.keys[pygame.K_w] :
            if self.player.rect.y < 300:
                self.player.speed =0
                self.world_y_shift=1
                if self.keys[pygame.K_LSHIFT]:
                    self.world_y_shift += 3
            else:
                self.player.rect.y -= 1
                if self.keys[pygame.K_LSHIFT]:
                    self.player.rect.y -= 3

            return
        elif self.keys[pygame.K_s]:
            if self.player.rect.y > 300:
                self.player.speed =0
                self.world_y_shift=-1
                if self.keys[pygame.K_LSHIFT]:
                    self.world_y_shift -= 3
            else:
                self.player.rect.y += 1
                if self.keys[pygame.K_LSHIFT]:
                    self.player.rect.y += 3
            return
        else:
            self.world_x_shift=0
            self.world_y_shift=0
            return


    def colisiones(self):
        for i in self.items:
            i.speed = 0
        for k in self.door_keys:
            k.speed = 0
        for d in self.lock_doors:
            d.speed = 0

        for wall in self.walls:
            if wall.rect.colliderect(self.player):

                if self.keys[pygame.K_a]:
                    self.player.speed =0
                    self.world_x_shift -=10


                if self.keys[pygame.K_d]:
                    self.player.speed =0
                    self.world_x_shift +=10


                if self.keys[pygame.K_w]:
                    self.player.speed =0
                    self.world_y_shift -=10


                if self.keys[pygame.K_s]:
                    self.player.speed =0
                    self.world_y_shift +=10

    def puntaje(self):

        for i in self.items:
            if i.rect.colliderect(self.player):
                self.items.remove(i)
                self.score += 100
                self.moneda.play()
        return self.score

    # Activacion de todas las funciones de esta clase
    def run(self):

        self.walls.update(self.world_x_shift, self.world_y_shift)
        self.walls.draw(self.diplay_surface)
        self.items.update(self.world_x_shift, self.world_y_shift)
        self.items.draw(self.diplay_surface)
        self.lock_doors.update(self.world_x_shift, self.world_y_shift)
        self.lock_doors.draw(self.diplay_surface)
        self.door_keys.update(self.world_x_shift, self.world_y_shift)
        self.door_keys.draw(self.diplay_surface)
        self.player_list.draw(self.diplay_surface)
        self.scroll_world()
        self.colisiones()
        self.puntaje()
