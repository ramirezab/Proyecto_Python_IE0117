import pygame
pygame.init()
from pygame import mixer
pygame.init()
pygame.mixer.init()

# Definicion de la clase paredes
class wall(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite).convert()

        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shif, y_shift): # Posicion de los sprites para su movimiento
        self.rect.x += x_shif
        self.rect.y += y_shift

class items(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites\coin.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


class lock_door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites\lock_door.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


class door_key(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites\key.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift

class finish(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites\lag.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


