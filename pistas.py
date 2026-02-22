#---------------------------------------------------------------------
#importando as bibliotecas

import pygame
from math import pi

comprimento_linha = 4


def gera_reta(superficie, x, y, tamanho, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param tamanho: Tamanho da reta
    :param a: Indica qual direção estara a reta
    """
    if a == (0, 1):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x + tamanho, y), comprimento_linha )
    elif a == (0, -1):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x - tamanho, y), comprimento_linha)
    elif a == (1, 0):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x, y + tamanho), comprimento_linha)
    elif a == (-1, 0):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x, y - tamanho), comprimento_linha)

def gera_arco(superficie, x, y, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param a: Indica qual direção estara o arco

    """

    if a == (0, 1):
        pygame.draw.arc(superficie, (255, 255, 255), (x, y - 75, 150, 150), pi/2, -pi, comprimento_linha)
    elif a == (0, -1):
        pygame.draw.arc(superficie, (255, 255, 255), (x - 150, y - 75, 150, 150), 0, pi / 2, comprimento_linha)
    elif a == (1, 0):
        pygame.draw.arc(superficie, (255, 255, 255), (x - 150, y - 75, 150, 150), (3*pi)/2, 0, comprimento_linha)
    elif a == (-1, 0):
        pygame.draw.arc(superficie, (255, 255, 255), (x, y - 75, 150, 150), pi, 3*pi/2, comprimento_linha)

def inicio(superficie, x_inicio, y_inicio):
    """
    Função que marca o inicio da pista para delimitar onde o robo deve aparecer em cada pista
    """
    pygame.draw.rect(superficie, (0,255,0), (x_inicio,y_inicio,2,2), 5)

def pista_simples(superficie):
    """
        Função que gera uma pista retangular com bordas curvadas
    """
    gera_reta(superficie, 150,150,400,(0,1))
    gera_reta(superficie, 150,450,400,(0,1))
    gera_reta(superficie, 617, 220, 170, (1, 0))
    gera_reta(superficie, 91, 220, 170, (1, 0))
    gera_reta(superficie, 400, 430, 40, (1, 0))
    gera_reta(superficie, 300, 430, 40, (1, 0))
    gera_arco(superficie, 88,378,(-1, 0))
    gera_arco(superficie, 88, 222, (0, 1))
    gera_arco(superficie, 620, 222, (0, -1))
    gera_arco(superficie, 620, 378, (1, 0))
    inicio(superficie, 350, 450)

def pista_circular(superficie):
    """
           Função que gera uma pista totalmente circular
    """
    pygame.draw.circle(superficie, (255, 255, 255), (340, 340), 200, comprimento_linha)
    gera_reta(superficie, 340, 515, 40, (1, 0))
    gera_reta(superficie, 340, 123, 40, (1, 0))
    inicio(superficie, 340, 535 )

def pista_complexa(superficie):
    gera_reta(superficie, 150,450,400,(0,1))



