import pygame
from math import pi



def gera_reta(superficie, x, y, tamanho, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param tamanho: Tamanho da reta
    :param a: Indica qual direção estara a reta
    """
    if a == (0, 1):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x + tamanho, y), 5 )
    elif a == (0, -1):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x - tamanho, y), 5)
    elif a == (1, 0):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x, y + tamanho), 5)
    elif a == (-1, 0):
        pygame.draw.line(superficie, (255, 255, 255), (x, y), (x, y - tamanho), 5)

def gera_arco(superficie, x, y, a):
    """
    :param x: Posição inicial no eixo X
    :param y: Posição inicial no eixo Y
    :param a: Indica qual direção estara o arco

    """

    if a == (0, 1):
        pygame.draw.arc(superficie, (255, 255, 255), (x, y - 75, 150, 150), pi/2, -pi, 5)
    elif a == (0, -1):
        pygame.draw.arc(superficie, (255, 255, 255), (x - 150, y - 75, 150, 150), 0, pi / 2, 5)
    elif a == (1, 0):
        pygame.draw.arc(superficie, (255, 255, 255), (x - 150, y - 75, 150, 150), (3*pi)/2, 0, 5)
    elif a == (-1, 0):
        pygame.draw.arc(superficie, (255, 255, 255), (x, y - 75, 150, 150), pi, 3*pi/2, 5)



def pista_simples(superficie):

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

def pista_circular(superficie):
    pygame.draw.circle(superficie, (255, 255, 255), (340, 340), 200, 5)
    gera_reta(superficie, 340, 515, 40, (1, 0))
    gera_reta(superficie, 340, 123, 40, (1, 0))

def pista_complexa(superficie):
    gera_reta(superficie, 150,450,400,(0,1))


