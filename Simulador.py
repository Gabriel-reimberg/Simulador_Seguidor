#importando as bibliotecas
import pygame
import math
from pygame.locals import *
from sys import exit

#iniciando o pygame
pygame.init()

#Variaveis
altura = 680
largura = 680
pi = math.pi

tela = pygame.display.set_mode((largura, altura))

nome = "Simulador"
pygame.display.set_caption(nome)

def gera_reta(x, y, tamanho, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param tamanho: Tamanho da reta
    :param a: Indica qual direção estara a reta

     """
    if a == (0, 1):
        pygame.draw.line(tela, (255, 255, 255), (x, y), (x + tamanho, y), 5 )

    elif a == (0, -1):
        pygame.draw.line(tela, (255, 255, 255), (x, y), (x - tamanho, y), 5)

    elif a == (1, 0):
        pygame.draw.line(tela, (255, 255, 255), (x, y), (x, y + tamanho), 5)

    elif a == (-1, 0):
        pygame.draw.line(tela, (255, 255, 255), (x, y), (x, y - tamanho), 5)


def gera_arco(x, y, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param a: Indica qual direção estara o arco

    """
    if a == (0, 1):
        pygame.draw.arc(tela, (255, 255, 255), (x, y - 75, 150, 150), pi/2, -pi, 5)

    elif a == (0, -1):
        pygame.draw.arc(tela, (255, 255, 255), (x - 150, y - 75, 150, 150), 0, pi / 2, 5)

    elif a == (1, 0):
        pygame.draw.arc(tela, (255, 255, 255), (x - 150, y - 75, 150, 150), (3*pi)/2, 0, 5)

    elif a == (-1, 0):
        pygame.draw.arc(tela, (255, 255, 255), (x, y - 75, 150, 150), pi, 3*pi/2, 5)

def pista_simples():
    gera_reta(150,150,400,(0,1))
    gera_reta(150,450,400,(0,1))
    gera_reta(617, 220, 170, (1, 0))
    gera_reta(91, 220, 170, (1, 0))
    gera_reta(400, 430, 40, (1, 0))
    gera_reta(300, 430, 40, (1, 0))
    gera_arco(88,378,(-1, 0))
    gera_arco(88, 222, (0, 1))
    gera_arco(620, 222, (0, -1))
    gera_arco(620, 378, (1, 0))

frame = pygame.time.Clock()

#Loop principal da simulação
while True:
    frame.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pista_simples()

    pygame.display.update()



