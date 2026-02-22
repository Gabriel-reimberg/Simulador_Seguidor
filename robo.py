import pygame.draw


def corpo(superficie, x_robo, y_robo):
    pygame.draw.rect(superficie, (0,255,255), (x_robo-25, y_robo - 25, 25, 50), 50 )
