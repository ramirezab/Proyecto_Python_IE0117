import pygame
pygame.init()

class wall(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("sprites\wall_1_front.png").convert()
        
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shif, y_shift):
        self.rect.x += x_shif
        self.rect.y += y_shift


class ply(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((20,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)
        


    def update(self):
        self.get_input()
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y
