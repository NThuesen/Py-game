# Aqui definiremos as imagens e sons
import pygame
from operator import itemgetter
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

BackMenu= pygame.image.load('Imagens\Menu.png').convert_alpha()
BackMenu = pygame.transform.scale(BackMenu, (900, 600))
Blackhole= pygame.image.load('Imagens/BlackHole.jpg').convert_alpha()
Blackhole = pygame.transform.scale(Blackhole, (900, 600))
Racket_img = pygame.image.load('Imagens/barra.png').convert_alpha()
Racket_img = pygame.transform.scale(Racket_img, (100, 100))
ball_img = pygame.image.load('Imagens/Bola.png').convert_alpha()
ball_img = pygame.transform.scale(ball_img, (75, 75))
rulesmenu = pygame.image.load('Imagens/rules_v2.png').convert_alpha()
rule_smenu = pygame.transform.scale(rulesmenu, (900, 600))

# Carrega os efeitos sonoros
pygame.mixer.music.load('Músicas/Cornfield_Chase.mp3')
pygame.mixer.music.set_volume(1)
batida = pygame.mixer.Sound("Músicas/PongSound.wav")