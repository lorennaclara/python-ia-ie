# Importando a biblioteca Pygame
from sys import exit
import pygame
from pygame.locals import *

#=============================
#----1. Criando a janela------
#=============================

pygame.init() # 1.Inicializa o Pygame

# 1. Configura as dimensões da janela e cria a tela 
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption("Snake Game") # 1. Define o título do jogo

# 1. Cria o relógio para controlar os FPS
relogio = pygame.time.Clock()

#==================================================
#---2. Definindo o Tamanho dos Blocos e o Fundo---
#==================================================
TAMANHO_GRAMADO = 20 # largura x altura em pixels

COR_FUNDO = (170,215,81) # (R,G,B)
COR_GRAMA = (162,209,73)

#=================================================
#---4. A Estrutura e o Estado Inicial da Cobra ---
#=================================================

inicio = [
    pygame.Rect(x,200,TAMANHO_GRAMADO,TAMANHO_GRAMADO)
    for x in (80,60,40)
]
cobra = inicio.copy()

#========================================
#---5. Movimento Automático da Cobra ---
#========================================

velocidade_x = TAMANHO_GRAMADO
velocidade_y = 0

# 1. Looping que mantém a janela aberta
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False

    #========================================
    #---6. Controles do Teclado (Setas) ---
    #========================================
        elif evento.type == KEYDOWN:
            if evento.key == K_LEFT and velocidade_x == 0:
                velocidade_x = -TAMANHO_GRAMADO
                velocidade_y = 0

            elif evento.key == K_RIGHT and velocidade_x == 0:
                velocidade_x = TAMANHO_GRAMADO
                velocidade_y = 0

            elif evento.key == K_UP and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = -TAMANHO_GRAMADO

            elif evento.key == K_DOWN and velocidade_y == 0:
                velocidade_x = 0
                velocidade_y = TAMANHO_GRAMADO



    #========================================
    #---5. Atualizando a Posição da Cobra ---
    #========================================
    cabeca = pygame.Rect(
        cobra[0].x + velocidade_x,
        cobra[0].y + velocidade_y,
        TAMANHO_GRAMADO,
        TAMANHO_GRAMADO
    )

    cobra.insert(0,cabeca) # Insere novo elemento na cabeça
    cobra.pop() # Remove o último item da lista cobra

    # 2. Pintando toda a tela com a cor de fundo
    tela.fill(COR_FUNDO)

    #==================================================
    #---3. Desenhando o Fundo Quadriculado (Grama) ---
    #==================================================

    for x in range(0,LARGURA,TAMANHO_GRAMADO):
        for y in range(x % 40,ALTURA,40):
            pygame.draw.rect(tela,COR_GRAMA,(x,y,TAMANHO_GRAMADO,TAMANHO_GRAMADO))

    #==================================================
    #---4. A Estrutura e o Estado Inicial da Cobra ---
    #==================================================
    for parte in cobra:
        pygame.draw.rect(tela,"purple", parte,0,6)

    # 1. Atualiza o que aparece na tela
    pygame.display.flip()

    # 1. Manter a taxa de 10 quadros por segundo
    relogio.tick(10)

# 1. Encerra o Pygame corretamente
pygame.quit()
exit()

