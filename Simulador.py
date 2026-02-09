#importando as bibliotecas

import pygame
import math

from pygame.locals import *
from sys import exit

import pistas


print("="*20)
print("== Olá, bem vindo ==")
print("="*20)

#Variaveis importantes antes de iniciar
p = 0

while p not in [1, 2]:
    p = int(input("Digite o numero do pista [1 ou 2]: "))

#iniciando o pygame
pygame.init()

#Variaveis

altura = 680
largura = 680
pi = math.pi

tela = pygame.display.set_mode((largura, altura))


nome = "Simulador"
pygame.display.set_caption(nome)
frame = pygame.time.Clock()



#Loop principal da simulação
while True:
    frame.tick(60)
    tela.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if p ==1:
        pistas.pista_simples(tela)
    elif p ==2:
        pistas.pista_circular(tela)


    pygame.display.update()