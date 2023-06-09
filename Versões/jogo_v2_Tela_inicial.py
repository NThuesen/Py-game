# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
largura = 900
altura = 600
window = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Ultimate Pong')

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
                    inicio = False
                # Verifica se o clique foi no botão "como jogar"
                if botao_como_jogar.collidepoint(event.pos):
                    inicio = False
        
        # Desenha o fundo na tela
        window.fill((0, 0, 0))
        
        # Configurações do botão "Jogar"
        cor_botao = (255, 255, 255)  # branco
        largura_botao = 200
        altura_botao = 50
        x_botao = largura // 2 - largura_botao // 2
        y_botao = altura // 2
        
        # Desenha o retângulo do botão "Jogar"
        botao_jogar = pygame.draw.rect(window, cor_botao, pygame.Rect(x_botao, y_botao, largura_botao, altura_botao))
        
        # Configurações do texto do botão "Jogar"
        fonte = pygame.font.Font(None, 36)
        texto_jogar = fonte.render("Jogar", True, (0, 0, 0))  # Preto
        texto_jogar_rect = texto_jogar.get_rect(center=(x_botao + largura_botao // 2, y_botao + altura_botao // 2))
        
        # Desenha o texto do botão "Jogar"
        window.blit(texto_jogar, texto_jogar_rect)
        
        # Configurações do botão "como jogar"
        cor_botao = (255, 255, 255)  # branco
        largura_botao = 200
        altura_botao = 50
        x_botao_como_jogar = largura // 2 - largura_botao // 2
        y_botao_como_jogar = altura // 1.5

        # Desenha o retângulo do botão "como jogar"
        botao_como_jogar = pygame.draw.rect(window, cor_botao, pygame.Rect(x_botao_como_jogar, y_botao_como_jogar, largura_botao, altura_botao))

        # Configurações do texto do botão "como jogar"
        fonte = pygame.font.Font(None, 36)
        texto_como_jogar = fonte.render("como jogar", True, (0, 0, 0))  # Preto
        texto_como_jogar_rect = texto_jogar.get_rect(center=(x_botao_como_jogar + largura_botao // 3, y_botao_como_jogar + altura_botao // 2))

        # Desenha o texto do botão "como jogar"
        window.blit(texto_como_jogar, texto_como_jogar_rect)

        # Configurações do texto do botão "Ultimate Pong"
        fonte = pygame.font.Font(None, 90)
        texto_Ultimate_pong = fonte.render("Ultimate Pong", True, (255, 255, 255))  # Preto
        
        # Desenha o texto do botão "Ultimate_pong"
        window.blit(texto_Ultimate_pong, (250,130))
        
        # Atualiza a tela
        pygame.display.flip()

# ----- Inicia estruturas de dados
game = True

tela_de_inicio()

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((255, 0, 0))  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados