ball_img = pygame.image.load('Imagens/Bola.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (75, 75))

class ball (pygame.sprite.Sprite):
    def __init__(self, img, coord):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.mask = pygame.mask.from_surface(self.image) # Essa é a hitbox da bola
        self.rect = self.image.get_rect()
        self.rect.centerx = coord[0]
        self.rect.bottom =  coord[1]
        self.speedx = 5
        self.speedy = 5
    
    def update(self):
        # Atualização da posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Especifica bordas da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura

bolas = pygame.sprite.Group()  # Criando um grupo com a bola
bolas.add(bola)