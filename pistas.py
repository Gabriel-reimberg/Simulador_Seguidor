#---------------------------------------------------------------------
#importando as bibliotecas

import pygame
import math
from math import pi

#---------------------------------------------------------------------
#Definindo Variaveis da pista

comprimento_linha = 4
pontos1 = []
pontos2 = []


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

def pista_1(superficie):
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
    inicio(superficie, 350, 450) #Marcação do inicio do robô

def pista_2(superficie):
    """
           Função que gera uma pista totalmente circular
    """
    pygame.draw.circle(superficie, (255, 255, 255), (340, 340), 200, comprimento_linha)
    gera_reta(superficie, 340, 515, 40, (1, 0)) #Marcação
    gera_reta(superficie, 340, 123, 40, (1, 0)) #Marcação
    inicio(superficie, 340, 535 ) #Marcação do inicio do robô

def pista_3(superficie):
    gera_reta(superficie, 200, 480, 40, (1, 0))   #Marcação de Fim
    gera_reta(superficie, 300, 480 , 40, (1, 0))  #Marcação de inicio

    gera_reta(superficie, 150, 500, 218, (0, 1))  # Reta Horizontal (1)
    gera_reta(superficie, 370, 231, 150, (0, 1))  # Reta Horizontal (2)
    gera_reta(superficie, 370, 443, 40, (0, 1))  # Reta Horizontal (3)
    gera_reta(superficie, 150, 77, 255, (0, 1))  # Reta Horizontal (3)

    gera_reta(superficie, 585, 504,200,(-1,0))  #Reta Vertical (1)
    gera_reta(superficie, 302, 370,75,(-1, 0))  #Reta Vertical (2)
    gera_reta(superficie, 302, 370,75,(-1, 0))  #Reta Vertical (3)
    gera_reta(superficie, 477, 370,220,(-1, 0)) #Reta Vertical (4)
    gera_reta(superficie, 82, 150, 40, (1, 0))  #Reta Vertical (5)
    gera_reta(superficie, 82, 380, 50, (1, 0))  #Reta Vertical (6)

    gera_arco(superficie, 588, 304, (0,-1))  #Arco (1)
    gera_arco(superficie, 300, 304, (0, 1))  #Arco (2)
    gera_arco(superficie, 300, 370, (-1, 0)) #Arco (3)
    gera_arco(superficie, 480, 370, (1, 0))  #Arco (4)
    gera_arco(superficie, 480, 150, (0, -1)) #Arco (5)
    gera_arco(superficie, 80, 150, (0, 1))   #Arco (6)
    gera_arco(superficie, 80, 428, (-1, 0))  #Arco (7)


    #Senoide (1)
    if len(pontos1) == 0:
        for x in range(368, 586):
            y = 500 + 15 * math.sin((x-368) * 0.1)
            pontos1.append((x, y))
    if len(pontos1) > 1:
        pygame.draw.lines(superficie, (255, 255, 255), False, pontos1, 5)

    # Senoide (2)
    if len(pontos2) == 0:
        for y in range(190, 380):
            x = 98 + 15 * math.sin((y-82) * 0.1)
            pontos2.append((x, y))
    if len(pontos1) > 1:
        pygame.draw.lines(superficie, (255, 255, 255), False, pontos2, 5)




