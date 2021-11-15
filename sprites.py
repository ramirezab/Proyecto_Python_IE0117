import pygame
pygame.init()

# Definicion de la clase paredes
class wall(pygame.sprite.Sprite):
    def __init__(self, pos, sprite):
        super().__init__()
        self.image = pygame.image.load(sprite).convert()
        
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shif, y_shift): # Posicion de los sprites para su movimiento
        self.rect.x += x_shif
        self.rect.y += y_shift

# Definicion de la clase player
class ply(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

    # def direccion_sprite(self):

        # player_de
        # player_iz
        # player_up
        # plaer_down

        # keys = pygame.key.get_pressed()

        # if keys == pygame.K_a:

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


