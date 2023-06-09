# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import os
import random
import json
from operator import itemgetter
# Força o diretório a ser o mesmo independentemente do computador
diretorio = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretorio)

pygame.init()

# ----- Gera tela principal
largura = 900
altura = 600
window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Ultimate Pong')

# Variáveis de texto
texto_digitado = ""
cor_texto = (255, 255, 255)  # branco
posicao_texto = (largura // 2, altura // 2 - 60)

# Carrega as imagens e sons

from FullLoad import *
# ----------------------------------

# função para a leaderboard
def atualizar_ranking(nome_jogador):
    with open('ranking.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)

    jogadores = dados['players']

    # Verifica se o jogador já existe no ranking
    jogador_existente = next((j for j in jogadores if j['nome'] == nome_jogador), None)
    if jogador_existente:
        jogador_existente['vitorias'] += 1
    else:
        novo_jogador = {'nome': nome_jogador, 'vitorias': 1}
        jogadores.append(novo_jogador)

    # Ordena os jogadores por número de vitórias (ordem decrescente)
    jogadores = sorted(jogadores, key=itemgetter('vitorias'), reverse=True)

    # Limita a lista aos top 5 jogadores
    top10_jogadores = jogadores[:10]

    # Atualiza os dados no arquivo JSON
    dados['players'] = top10_jogadores
    with open('ranking.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json)

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

def tela_rules():
        # Loop para exibir a tela de início
    inicio = True
    while inicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o clique foi no botão "Jogar"
                if botao_return.collidepoint(event.pos):
                    return 'menu'
                
        # Desenha o fundo na tela
        window.fill((0, 0, 0))
        window.blit(rule_smenu, (0, 0))  

           # Configuração do botão "Return"
        cor_botao = (255, 255, 255)  # branco
        largura_botao_return = 200
        altura_botao_return = 50
        x_botao_return = 60
        y_botao_return = 520
        botao_return = pygame.Rect(x_botao_return, y_botao_return, largura_botao_return, altura_botao_return)  

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

# ===== Criando os jogadores =====
Player1 = Racket(Racket_img, [35, (altura/2) + 50]) # Jogador 1
Player2 = Racket(Racket_img, [largura - 35,(altura/2) + 50]) # Jogador 2


Rackets = pygame.sprite.Group()  # Criando um grupo com as raquetes
Rackets.add(Player1, Player2)

bola = ball(ball_img,[largura/2,(altura/2) + 50])
bolas = pygame.sprite.Group()  # Criando um grupo com a bola
bolas.add(bola)

# ----- Inicia estruturas de dados
game = True
Menu = True
space_pressed = False
Tela = 'menu'  # Estado inicial do jogo

while game:
    while Menu:
        if Tela == 'menu':
            Tela = tela_de_inicio()
            if Tela == 'como jogar':
                Tela = tela_rules()
        
        elif Tela == 'como jogar':
            # Loop para exibir a tela de instruções
            while Tela == 'como jogar':
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    window.blit(rule_smenu,(0,0))


                    
                # ----- Atualiza estado do jogo
                    pygame.display.update()  # Mostra o novo frame para o jogador
        elif Tela == 'sair':
            Tela_final = False
            jogando = False
            game = False
            Menu = False
        else:
            space_pressed = False
            jogando = True
            Menu = False

    #  ===== FPS do jogo  =====
    clock = pygame.time.Clock()
    FPS = 60

    # Pontuação e  música
    pygame.mixer.music.play(loops=-1)

    font = pygame.font.SysFont(None,48)
    PontosP1 = 0
    PontosP2 = 0

    while jogando:

        # ---FPS ---
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                jogando = False
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
                batida.play()
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

        if PontosP1 == 3 or PontosP2 == 3:
            Tela_final = True
            jogando = False
    
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    while Tela_final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                else:
                    texto_digitado += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if texto_confirmar_rect.collidepoint(event.pos):
                    atualizar_ranking(texto_digitado)
                    leaderboard = True
                    Tela_final = False

        # Desenha o fundo na tela
        window.fill((0, 0, 0))

        # Configurações do texto "Digite seu nome"
        fonte = pygame.font.Font(None, 58)
        texto_digite_seu_nome = fonte.render("Digite seu nome:", True, (255, 255, 255))
        texto_digite_seu_nome_rect = texto_digite_seu_nome.get_rect(center=(largura // 2, 50))

        # Desenha o texto "Digite seu nome"
        window.blit(texto_digite_seu_nome, texto_digite_seu_nome_rect)

        # Configurações do texto digitado que aparece na tela
        fonte = pygame.font.Font(None, 36)
        texto_digitado_render = fonte.render(texto_digitado, True, (255, 255, 255))
        texto_digitado_rect = texto_digitado_render.get_rect(center=(largura // 2, altura // 2 - 60))

        # Desenha o texto digitado
        window.blit(texto_digitado_render, texto_digitado_rect)

        # Configuração do botão "confirmar"
        cor_botao = (255, 255, 255)
        largura_botao = 200
        altura_botao = 50
        x_botao = largura // 2 - largura_botao // 2
        y_botao = altura // 2

        # Desenha o retângulo do botão "confirmar"
        confirmar = pygame.draw.rect(window, cor_botao, pygame.Rect(x_botao, y_botao, largura_botao, altura_botao))

        # Configurações do texto do botão "confirmar"
        fonte = pygame.font.Font(None, 36)
        texto_confirmar = fonte.render("Confirmar", True, (0, 0, 0))
        texto_confirmar_rect = texto_confirmar.get_rect(center=(x_botao + largura_botao // 2, y_botao + altura_botao // 2))

        # Desenha o texto do botão "confirmar"
        window.blit(texto_confirmar, texto_confirmar_rect)

        pygame.display.flip()

    while leaderboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if texto_confirmar_rect.collidepoint(event.pos):
                    Menu = True
                    Tela = 'menu'
                    leaderboard = False

        # Configuração do leaderboard
        fonte_liderboard = pygame.font.Font(None, 36)
        y_posicao_liderboard = 100
        espaco_entre_jogadores = 50

        # Desenha o fundo na tela
        window.fill((0, 0, 0))

        # Desenha o título do leaderboard
        titulo_liderboard = fonte_liderboard.render("Leaderboard", True, (255, 255, 255))
        titulo_liderboard_rect = titulo_liderboard.get_rect(center=(largura // 2, 50))
        window.blit(titulo_liderboard, titulo_liderboard_rect)

        # Carrega os jogadores do arquivo JSON
        with open('ranking.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)

        jogadores = dados['players']

        # Desenha os jogadores no leaderboard
        for i, jogador in enumerate(jogadores):
            nome = jogador['nome']
            vitorias = jogador['vitorias']

            texto_jogador = f"{i + 1}. {nome} - {vitorias} vitórias"
            texto_jogador_render = fonte_liderboard.render(texto_jogador, True, (255, 255, 255))
            texto_jogador_rect = texto_jogador_render.get_rect(midtop=(largura // 2, y_posicao_liderboard + i * espaco_entre_jogadores))
            window.blit(texto_jogador_render, texto_jogador_rect)


        # Configuração do botão "confirmar"
        cor_botao = (255, 255, 255)
        largura_botao = 200
        altura_botao = 50
        x_botao = largura // 2 - largura_botao // 2
        y_botao = 500

        # Desenha o retângulo do botão "confirmar"
        confirmar = pygame.draw.rect(window, cor_botao, pygame.Rect(x_botao, y_botao, largura_botao, altura_botao))

        # Configurações do texto do botão "confirmar"
        fonte = pygame.font.Font(None, 36)
        texto_confirmar = fonte.render("Confirmar", True, (0, 0, 0))
        texto_confirmar_rect = texto_confirmar.get_rect(center=(x_botao + largura_botao // 2, y_botao + altura_botao // 2))

        # Desenha o texto do botão "confirmar"
        window.blit(texto_confirmar, texto_confirmar_rect)

        pygame.display.flip()


# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados