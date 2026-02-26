#---------------------------------------------------------------------
"""
Projeto pessoal com o objetivo de desenvolver um simulador para testes de
logica e algoritimos PID para implementação em um robo seguidor de linhna.

Nome: Gabriel Pires Reimberg
Curso: Engenharia de controle e automação

Ano: 2026
"""
#---------------------------------------------------------------------
#importando as bibliotecas

import pygame
import math
from pygame.locals import *
from sys import exit
import pistas
import robo

#---------------------------------------------------------------------
#Inicio/Escolhendo a pista
print("="*20)
print("== Olá, bem vindo ==")
print("="*20)
p = 0
while p not in [1, 2, 3]:
    p = int(input("Digite o numero do pista [1, 2 ou 3]: "))


#---------------------------------------------------------------------
#Iniciando o pygame
pygame.init()


#---------------------------------------------------------------------
#Variaveis
altura = 680
largura = 680
pi = math.pi
nome = "Simulador"

#---------------------------------------------------------------------
#Definindo a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(nome)
frame = pygame.time.Clock()


#---------------------------------------------------------------------
#Loop principal da simulação
while True:
    frame.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if p ==1:
        pistas.pista_1(tela)
    elif p == 2:
        pistas.pista_2(tela)
    elif p == 3:
        pistas.pista_3(tela)

    pygame.display.update()
#Fim
#---------------------------------------------------------------------








