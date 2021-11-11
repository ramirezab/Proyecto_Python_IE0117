import pygame

class wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("sprites\wall_1_front.png").convert()
        
        self.rect = self.image.get_rect(topleft = pos)