# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import os
# Força o diretório a ser o mesmo independentemente do computador
diretorio = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio)

pygame.init()

# ----- Gera tela principal
largura = 900
altura = 600
window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Ultimate Pong')

# Carrega as imagens

Seta= pygame.image.load('Imagens/Seta.webp').convert_alpha()
Seta = pygame.transform.scale(Seta, (100, 100))
BackMenu= pygame.image.load('Imagens\Menu.png').convert_alpha()
BackMenu = pygame.transform.scale(BackMenu, (900, 600))
Blackhole= pygame.image.load('Imagens/BlackHole.jpg').convert_alpha()
Blackhole = pygame.transform.scale(Blackhole, (900, 600))
Racket_img = pygame.image.load('Imagens/barra.png').convert_alpha()
Racket_img = pygame.transform.scale(Racket_img, (100, 100))
ball_img = pygame.image.load('Imagens/Bola.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (75, 75))

# Carrega os efeitos sonoros
pygame.mixer.music.load('Músicas/Cornfield_Chase.mp3')
pygame.mixer.music.set_volume(1)

# Tela de Início

def tela_de_inicio():
    # Loop para exibir a tela de início
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi no botão "Jogar"
                if botao_jogar.collidepoint(event.pos):
                    return 'jogar'
                # Verifica se o clique foi no botão "como jogar"
                if botao_rules.collidepoint(event.pos):
                    return 'como jogar'
                if botao_exit.collidepoint(event.pos):
                    return 'sair'
               
        # Desenha o fundo na tela
        window.fill((0, 0, 0))
        window.blit(BackMenu, (0, 0))
      
        # Configurações do botão "Jogar"
        cor_botao = (0 , 0, 0, 0)  # preto
        largura_botao = 200
        altura_botao = 50
        x_botao = 60
        y_botao = 320
        botao_jogar = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)

        # Configurações do botão "Exit"
        cor_botao = (255, 255, 255)  # branco
        largura_botao_exit = 150
        altura_botao_exit = 50
        x_botao_exit = 60
        y_botao_exit = 420
        botao_exit = pygame.Rect(x_botao_exit, y_botao_exit, largura_botao_exit, altura_botao_exit)

        # Configuração do botão "Rules"
        cor_botao = (255, 255, 255)  # branco
        largura_botao_rules = 200
        altura_botao_rules = 50
        x_botao_rules = 60
        y_botao_rules = 520
        botao_rules = pygame.Rect(x_botao_rules, y_botao_rules, largura_botao_rules, altura_botao_rules)
        
        # Atualiza a tela
        pygame.display.flip()

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
        self.speedx = 9
        self.speedy = 9
        self.ColisãoX = 1000

    def update(self, boleano):
        # Atualização da posição da bola
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Especifica bordas da tela
        if self.rect.top < 0 or self.rect.bottom > altura:
            self.speedy = -self.speedy
        
         # Para colisões com os jogadores
        if boleano and (abs(self.ColisãoX - self.rect.x) > 50):
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

# ===== Criando os jogadores =====
Player1 = Racket(Racket_img, [35, (altura/2) + 50]) # Jogador 1
Player2 = Racket(Racket_img, [largura - 35,(altura/2) + 50]) # Jogador 2


Rackets = pygame.sprite.Group()  # Criando um grupo com as raquetes
Rackets.add(Player1, Player2)

bola = ball(ball_img,[largura/2,(altura/2) + 50])
bolas = pygame.sprite.Group()  # Criando um grupo com a bola
bolas.add(bola)

# ----- Inicia estruturas de dados
Menu = True
game = True
space_pressed = False

Tela = 'menu'  # Estado inicial do jogo

while Menu:
    if Tela == 'menu':
        Tela = tela_de_inicio()
    
    elif Tela == 'como jogar':
        # Loop para exibir a tela de instruções
        while Tela == 'como jogar':
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                Seta_rect = Seta.get_rect() # Cria um retângulo com mesmas dimensões da Seta
                Seta_rect.topleft = (750, 30)  # Define as coordenadas do retângulo

                if event.type == pygame.MOUSEBUTTONDOWN and Seta_rect.collidepoint(event.pos):  # Verifica se clicaram na Seta
                    Tela = 'menu'
                
                # ----- Gera saídas
                window.fill((0, 0, 0))  # Preenche com a cor preta

                # Desenha a Suisei
                window.blit(Seta, (750, 30))


            # ----- Atualiza estado do jogo
                pygame.display.update()  # Mostra o novo frame para o jogador
    elif Tela == 'sair':
        game = False
        Menu = False
    else:
        space_pressed = False
        Menu = False




#  ===== FPS do jogo  =====
clock = pygame.time.Clock()
FPS = 60

 # Pontuação e  música
pygame.mixer.music.play(loops=-1)

font = pygame.font.SysFont(None,48)
PontosP1 = 0
PontosP2 = 0

while game:

    # ---FPS ---
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se algum jogador pressionou a barra de espaço
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space_pressed = True

    # ////// Movimento Player 1 //////
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_w:
                Player1.speed -= 7
            if event.key == pygame.K_s:
                Player1.speed += 7
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_w:
                Player1.speed += 7
            if event.key == pygame.K_s:
                Player1.speed -= 7
    # ////// Movimento Player 2 //////
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player2.speed -= 7
            if event.key == pygame.K_DOWN:
                Player2.speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player2.speed += 7
            if event.key == pygame.K_DOWN:
                Player2.speed -= 7
    
    # ----- Gera saídas
    if space_pressed:    
        hit = pygame.sprite.groupcollide(Rackets,bolas,False,False,pygame.sprite.collide_mask)
        if hit != {}:
            bolas.update(True)
        bolas.update(False)
    Rackets.update() # Atualiza posição da bola , requer arg player1, player2

    # Verifica se a bola saiu da tela, concede pontos se é o caso e cria outra bola.
    if bola.rect.x > largura:
        PontosP1 += 1
        bola.kill()
        bola = ball(ball_img,[largura/2,(altura/2) + 50])
        bolas.add(bola)
        space_pressed = False

    elif bola.rect.x < 0:
        PontosP2 += 1
        bola.kill()
        bola = ball(ball_img,[largura/2,(altura/2) + 50])
        bolas.add(bola)
        space_pressed = False
    
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(Blackhole, (0, 0)) # Preenche o Wallpaper do jogo

    # ----- Desenha os objetos
    Rackets.draw(window)
    bolas.draw(window)

    # ----- Desenha as pontuações

    # Desenhando o score
    PontosP1txt = font.render(f'{PontosP1}', True, (255, 255, 255))
    PontosP2txt = font.render(f'{PontosP2}', True, (255, 255, 255))
    P1text_rect = PontosP1txt.get_rect()
    P2text_rect = PontosP2txt.get_rect()
    P1text_rect.midtop = (50, 25)
    P2text_rect.midtop = (largura-50, 25)
    window.blit(PontosP1txt, P1text_rect)
    window.blit(PontosP2txt, P2text_rect)
   
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados