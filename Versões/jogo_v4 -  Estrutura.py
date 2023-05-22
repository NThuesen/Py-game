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
BackMenu= pygame.image.load('Imagens/BackGround Menu.jpg').convert_alpha()
BackMenu = pygame.transform.scale(BackMenu, (900, 600))
Blackhole= pygame.image.load('Imagens/BlackHole.jpg').convert_alpha()
Blackhole = pygame.transform.scale(Blackhole, (900, 600))
Racket_img = pygame.image.load('Músicas/Suisei.jpg').convert_alpha()
Racket_img = pygame.transform.scale(Racket_img, (100, 100))


'''# Carrega os efeitos sonoros
pygame.mixer.music.load('Músicas/')
pygame.mixer.music.set_volume(0.4)
Som = pygame.mixer.Sound('assets/snd/expl3.wav')'''


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
                if texto_jogar_rect.collidepoint(event.pos):
                    return 'jogar'
                # Verifica se o clique foi no botão "como jogar"
                if texto_como_jogar_rect.collidepoint(event.pos):
                    return 'como jogar'
        
        # Desenha o fundo na tela
        window.fill((0, 0, 0))
        window.blit(BackMenu, (0, 0))

        
        # Configurações do botão "Jogar"
        cor_botao = (0 , 0, 0 )  # preto
        largura_botao = 200
        altura_botao = 50
        x_botao = largura // 2 - largura_botao // 2
        y_botao = altura // 2
       
        
        # Configurações do texto do botão "Jogar"
        fonte = pygame.font.Font(None, 36)
        texto_jogar = fonte.render("Jogar", True, (0, 0, 0))  # Preto
        texto_jogar_rect = texto_jogar.get_rect(center=(x_botao + largura_botao // 2, y_botao + altura_botao // 2))
        
        # Desenha o texto do botão "Jogar"
        window.blit(texto_jogar, texto_jogar_rect)
        
        # Configurações do botão "como jogar"
        cor_botao = (255, 255, 255)  # branco
        largura_botao = 10
        altura_botao = 50
        x_botao_como_jogar = largura // 2 - largura_botao // 2
        y_botao_como_jogar = altura // 1.6

        # Configurações do texto do botão "como jogar"
        fonte = pygame.font.Font(None, 36)
        texto_como_jogar = fonte.render("Como jogar", True, (0, 0, 0))  # Preto
        texto_como_jogar_rect = texto_como_jogar.get_rect(center=(x_botao_como_jogar + largura_botao // 3, y_botao_como_jogar + altura_botao // 2))

        # Desenha o texto do botão "como jogar"
        window.blit(texto_como_jogar, texto_como_jogar_rect)

        # Configurações do texto "Ultimate Pong"
        fonte = pygame.font.Font(None, 90)
        texto_Ultimate_pong = fonte.render("Ultimate Pong", True, (255, 255, 255))  # Branco
        
        # Desenha o texto "Ultimate_pong"
        window.blit(texto_Ultimate_pong, (250,130))
        
        # Atualiza a tela
        pygame.display.flip()

# ----- Inicia estruturas de dados
Menu = True

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
    else:
        Menu = False

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
    
    def update(self):
        # Atualização da posição da nave
        self.rect.y += self.speed

        # Especifica bordas da tela
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura

               
# ===== Criando os jogadores =====
Player1 = Racket(Racket_img, [75, (altura/2) + 50]) # Jogador 1
Player2 = Racket(Racket_img, [largura - 75,(altura/2) + 50]) # Jogador 2

Rackets = pygame.sprite.Group()  # Criando um grupo com as raquetes
Rackets.add(Player1, Player2)

# ===== Loop principal =====
game = True

#  ===== FPS do jogo  =====
clock = pygame.time.Clock()
FPS = 30

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    # ////// Movimento Player 1 //////
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_w:
                Player1.speed -= 2
            if event.key == pygame.K_s:
                Player1.speed += 2
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_w:
                Player1.speed += 2
            if event.key == pygame.K_s:
                Player1.speed -= 2
    # ////// Movimento Player 2 //////
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player2.speed -= 2
            if event.key == pygame.K_DOWN:
                Player2.speed += 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player2.speed += 2
            if event.key == pygame.K_DOWN:
                Player2.speed -= 2
    
    # ----- Gera saídas
    Rackets.update() # Atualiza posição dos players
    
    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(Blackhole, (0, 0)) # Preenche o Wallpaper do jogo

    # ----- Desenha as raquetes
    Rackets.draw(window)
   
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

