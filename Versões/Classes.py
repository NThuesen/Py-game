import pygame
import random
pygame.init

# ========== Classes ==========
class Racket (pygame.sprite.Sprite):
    def __init__(self, img, coord):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image) # Essa é a hitbox da Racket
        self.rect = self.image.get_rect()
        self.rect.centerx = coord[0]
        self.rect.bottom =  coord[1]
        self.speed = 0
        ColisãoX = 1000
    
    def update(self):
        # Atualização da posição da nave
        self.rect.y += self.speed

        # Especifica bordas da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura

class ball(pygame.sprite.Sprite):
    def __init__(self, img, coord):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image)  # Essa é a hitbox da bola
        self.rect = self.image.get_rect()
        self.rect.centerx = coord[0]
        self.rect.bottom = coord[1]
        self.speedx = random.choice([-6, -5, -4, 4, 5, 6])  # Sentido inicial aleatório em X
        self.speedy = random.choice([-6, -5, -4, 4, 5, 6])  # Sentido inicial aleatório em Y
        self.ColisãoX = 1000

    def update(self, boleano):
        # Atualização da posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Especifica bordas da tela
        if self.rect.top < 0 or self.rect.bottom > altura:
            self.speedy = -self.speedy
        
         # Para colisões com os jogadores
        if boleano and (abs(self.ColisãoX - self.rect.x) > 100): # Limita uma única colisão, por jogador, por 'vez', com base na posição da bola.
            self.ColisãoX = self.rect.centerx
            if self.speedx < 0:
                self.speedx -= 0.25
            else:
                self.speedx += 0.25
            if self.speedy < 0:
                self.speedy -= 0.25
            else:
                self.speedy += 0.25
                  
            self.speedx = - self.speedx 