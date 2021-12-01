import pygame
pygame.init()
pygame.mixer.init()

# Definicion de las clases de lo
# objetos del juego


class wall(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()

        # Carga de la imagen correspondiente al spirte
        self.image = pygame.image.load(sprite).convert()

        self.rect = self.image.get_rect(topleft=pos)

    # Posicion de los sprites para su movimiento

    def update(self, x_shif, y_shift):
        self.rect.x += x_shif
        self.rect.y += y_shift


class items(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Carga de la imagen correspondiente al spirte
        self.image = pygame.image.load("sprites\coin.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    # Posicion de los sprites para su movimiento

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


class lock_door(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Carga de la imagen correspondiente al spirte
        self.image = pygame.image.load("sprites\lock_door.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    # Posicion de los sprites para su movimiento

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


class door_key(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Carga de la imagen correspondiente al spirte
        self.image = pygame.image.load("sprites\key.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    # Posicion de los sprites para su movimiento

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift


class finish(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # Carga de la imagen correspondiente al spirte
        self.image = pygame.image.load("sprites\lag.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)

    # Posicion de los sprites para su movimiento

    def update(self, x_shif, y_shift):

        self.rect.x += x_shif
        self.rect.y += y_shift
