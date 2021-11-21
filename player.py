from numpy import imag
import pygame
pygame.init()
# Definicion de la clase player
class ply(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.animation = False

        self.front = []
        self.back = []
        self.left = []
        self.right = []

        self.front.append(pygame.image.load("Personaje\down1.png"))
        self.front.append(pygame.image.load("Personaje\down2.png"))
        self.front.append(pygame.image.load("Personaje\down3.png"))

        self.back.append(pygame.image.load("Personaje\espalda1.png"))
        self.back.append(pygame.image.load("Personaje\espalda2.png"))
        self.back.append(pygame.image.load("Personaje\espalda3.png"))

        self.left.append(pygame.image.load("Personaje\iz1.png"))
        self.left.append(pygame.image.load("Personaje\iz2.png"))
        self.left.append(pygame.image.load("Personaje\iz3.png"))

        self.right.append(pygame.image.load("Personaje\de1.png"))
        self.right.append(pygame.image.load("Personaje\de2.png"))
        self.right.append(pygame.image.load("Personaje\de3.png"))

        self.current_sprite = 0
        self.image = self.front[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft =[pos[0], pos[1]]

    def update(self):
        self.current_sprite += 0.15

        if self.current_sprite >= len(self.front):
            self.current_sprite = 0
        self.keys = pygame.key.get_pressed() # Obtención de teclas



        
        if self.keys[pygame.K_a] and not self.keys[pygame.K_d] and not self.keys[pygame.K_w] and not self.keys[pygame.K_s]:
            self.image = self.left[int(self.current_sprite)]
           
            return
        elif self.keys[pygame.K_d] and not self.keys[pygame.K_a] and not self.keys[pygame.K_w] and not self.keys[pygame.K_s]:
            self.image = self.right[int(self.current_sprite)]
            

            return
        elif self.keys[pygame.K_w] and not self.keys[pygame.K_a] and not self.keys[pygame.K_d] and not self.keys[pygame.K_s]:
            self.image = self.back[int(self.current_sprite)]

            return
        
        elif self.keys[pygame.K_s] and not self.keys[pygame.K_a] and not self.keys[pygame.K_d] and not self.keys[pygame.K_w]:
            self.image = self.front[int(self.current_sprite)]
            return

        else:
            self.image = self.front[0]
           